#!/usr/bin/env python3
"""Generate Academic Pages publication entries from an OpenAlex author record."""

from __future__ import annotations

import html
import json
import os
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "_publications"
OVERRIDES_PATH = ROOT / "_data" / "publication_overrides.json"
OPENALEX_AUTHOR_ID = os.environ.get("OPENALEX_AUTHOR_ID", "A5101217620")
OPENALEX_MAILTO = os.environ.get("OPENALEX_MAILTO", "dongqishi@sztu.edu.cn")
ALLOWED_TYPES = {
    "article",
    "book-chapter",
    "conference-paper",
    "preprint",
    "proceedings-article",
}
TYPE_LABELS = {
    "article": "Journal Article",
    "book-chapter": "Book Chapter",
    "conference-paper": "Conference Paper",
    "preprint": "Preprint",
    "proceedings-article": "Conference Paper",
}


def fetch_json(url: str) -> dict[str, Any]:
    request = urllib.request.Request(
        url,
        headers={
            "Accept": "application/json",
            "User-Agent": f"qishi-academic-site/1.0 (mailto:{OPENALEX_MAILTO})",
        },
    )
    for attempt in range(3):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                return json.load(response)
        except (urllib.error.URLError, TimeoutError, json.JSONDecodeError):
            if attempt == 2:
                raise
            time.sleep(2**attempt)
    raise RuntimeError("OpenAlex request failed")


def fetch_works() -> list[dict[str, Any]]:
    params = urllib.parse.urlencode(
        {
            "filter": f"author.id:{OPENALEX_AUTHOR_ID}",
            "per-page": "100",
            "sort": "publication_date:desc",
            "mailto": OPENALEX_MAILTO,
        }
    )
    payload = fetch_json(f"https://api.openalex.org/works?{params}")
    works = payload.get("results")
    if not isinstance(works, list) or not works:
        raise RuntimeError("OpenAlex returned no publications; refusing to erase existing files")
    return works


def clean_text(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


def doi_value(work: dict[str, Any]) -> str:
    value = clean_text(work.get("doi")).lower()
    return re.sub(r"^https?://(?:dx\.)?doi\.org/", "", value)


def normalized_title(value: str) -> str:
    value = unicodedata.normalize("NFKD", value).casefold()
    value = re.sub(r"\([^)]*\d{4}[^)]*\)\s*$", "", value)
    return re.sub(r"[^a-z0-9]+", "", value)


def yaml_value(value: Any) -> str:
    return json.dumps(value, ensure_ascii=False)


def display_authors(work: dict[str, Any]) -> str:
    authors: list[str] = []
    for authorship in work.get("authorships") or []:
        raw_name = clean_text(
            authorship.get("raw_author_name")
            or (authorship.get("author") or {}).get("display_name")
        )
        if not raw_name:
            continue
        safe_name = html.escape(raw_name)
        if raw_name.casefold() in {"qishi dong", "dong qishi", "q. dong"}:
            safe_name = f"<strong>{safe_name}</strong>"
        authors.append(safe_name)
    return "; ".join(authors)


def venue_name(work: dict[str, Any]) -> str:
    location = work.get("primary_location") or {}
    source = location.get("source") or {}
    return clean_text(source.get("display_name") or location.get("raw_source_name") or "Preprint")


def publication_date(work: dict[str, Any]) -> str:
    value = clean_text(work.get("publication_date"))
    if re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return value
    year = str(work.get("publication_year") or "1900")
    return f"{year}-01-01"


def paper_url(work: dict[str, Any], doi: str) -> str:
    if doi:
        return f"https://doi.org/{doi}"
    location = work.get("best_oa_location") or work.get("primary_location") or {}
    return clean_text(location.get("landing_page_url") or work.get("id"))


def render_entry(work: dict[str, Any], override: dict[str, Any]) -> tuple[str, str]:
    openalex_id = clean_text(work.get("id")).rstrip("/").split("/")[-1].lower()
    if not re.fullmatch(r"w\d+", openalex_id):
        raise ValueError(f"Unexpected OpenAlex work identifier: {openalex_id!r}")

    doi = doi_value(work)
    date = publication_date(work)
    year = date[:4]
    work_type = clean_text(work.get("type"))
    raw_title = override.get("title") or clean_text(work.get("display_name") or work.get("title"))
    raw_venue = override.get("venue") or venue_name(work)
    authors = override.get("authors") or display_authors(work)
    title = html.escape(clean_text(raw_title))
    venue = html.escape(clean_text(raw_venue))
    link = paper_url(work, doi)
    type_label = TYPE_LABELS.get(work_type, work_type.replace("-", " ").title())
    citation = f'{authors}. “{title}.” <em>{venue}</em>, {year}.'
    permalink = f"/publication/{date}-{openalex_id}/"

    lines = [
        "---",
        f"title: {yaml_value(title)}",
        "collection: publications",
        f"permalink: {yaml_value(permalink)}",
        f"date: {date}",
        f"venue: {yaml_value(venue)}",
        f"authors: {yaml_value(authors)}",
        f"type_label: {yaml_value(type_label)}",
        f"paperurl: {yaml_value(link)}",
        f"citation: {yaml_value(citation)}",
        f"openalex: {yaml_value(work.get('id'))}",
    ]
    if doi:
        lines.append(f"doi: {yaml_value(doi)}")
    teaser = clean_text(override.get("teaser"))
    if teaser:
        lines.extend(["header:", f"  teaser: {yaml_value(teaser)}"])
    lines.extend(
        [
            "---",
            "",
            f"<p>{authors}. <strong>{title}.</strong> <em>{venue}</em>, {year}.</p>",
            "",
            f"[View DOI / publication]({link}){{: target=\"_blank\" rel=\"noopener\" }}",
            "",
            f"Metadata source: [OpenAlex]({work.get('id')})",
            "",
        ]
    )
    return f"auto-{openalex_id}.md", "\n".join(lines)


def main() -> int:
    overrides = json.loads(OVERRIDES_PATH.read_text(encoding="utf-8"))
    excluded = {value.casefold() for value in overrides.get("exclude_dois", [])}
    per_work = {key.casefold(): value for key, value in overrides.get("works", {}).items()}

    selected: dict[str, dict[str, Any]] = {}
    for work in fetch_works():
        if clean_text(work.get("type")) not in ALLOWED_TYPES:
            continue
        doi = doi_value(work)
        if doi in excluded:
            continue
        title = clean_text(work.get("display_name") or work.get("title"))
        key = normalized_title(title)
        if not key:
            continue
        existing = selected.get(key)
        if existing is None or len(title) < len(clean_text(existing.get("display_name"))):
            selected[key] = work

    generated: dict[str, str] = {}
    for work in selected.values():
        doi = doi_value(work)
        filename, content = render_entry(work, per_work.get(doi, {}))
        generated[filename] = content

    if not generated:
        raise RuntimeError("No supported publications found; refusing to erase existing files")

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    for old_file in OUTPUT_DIR.glob("auto-*.md"):
        old_file.unlink()
    for filename, content in sorted(generated.items()):
        (OUTPUT_DIR / filename).write_text(content, encoding="utf-8")

    print(f"Generated {len(generated)} publication entries for {OPENALEX_AUTHOR_ID}.")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as error:
        print(f"Publication update failed: {error}", file=sys.stderr)
        raise
