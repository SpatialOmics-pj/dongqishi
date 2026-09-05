# Qishi Dong — academic website

Personal academic website for Qishi Dong, built with the
[Academic Pages](https://academicpages.github.io/) Jekyll template and hosted
as a GitHub Pages project site.

## Publication updates

Publications are synchronized from the OpenAlex author record
[`A5101217620`](https://openalex.org/A5101217620). A GitHub Actions workflow
runs every Monday and can also be started manually from the Actions tab.

The update script only replaces files named `_publications/auto-*.md`. Manual
publication files are never removed. Known metadata corrections, thumbnail
choices, and excluded duplicate records live in
`_data/publication_overrides.json`.

To refresh locally:

```bash
python3 scripts/update_publications.py
```

To preview the site locally:

```bash
bundle install
bundle exec jekyll serve
```

The repository lockfile also includes Linux so the same dependency set is used
by local previews and the website validation workflow.
