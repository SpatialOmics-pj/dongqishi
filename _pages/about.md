---
permalink: /
title: "Introduction"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---

I am an Assistant Professor in the College of Big Data and Internet at Shenzhen Technology University. I received my Ph.D. in Statistics from Hong Kong Baptist University in 2023.

## Research Areas

Spatial omics analysis, statistical learning and biostatistics, AI for Science, and agentic AI.

## Academic Experience

- **Nov 2024–Present** — Assistant Professor, Shenzhen Technology University
- **Sep 2023–Sep 2024** — Postdoctoral Fellow, HKU Business School, The University of Hong Kong
- **Jun 2023–Nov 2024** — Research Assistant, The Chinese University of Hong Kong (Shenzhen)
- **2019–2023** — Ph.D. in Statistics, Hong Kong Baptist University

## Industry Experience

- **Nov 2021–Jun 2022** — Huawei Noah's Ark Lab, Hong Kong

## Openings

Students interested in data modeling, AI for Science, large language models, or agentic AI are welcome to contact me at [dongqishi@sztu.edu.cn](mailto:dongqishi@sztu.edu.cn).

## Recent Updates

{% assign recent_publications = site.publications | sort: "date" | reverse %}
<ul>
{% for post in recent_publications limit: 3 %}
  <li><strong>{{ post.date | date: "%Y" }}</strong> — {% if post.paperurl %}<a href="{{ post.paperurl }}">{{ post.title }}</a>{% else %}{{ post.title }}{% endif %}. <em>{{ post.venue }}</em>.</li>
{% endfor %}
  <li><strong>2026</strong> — Principal investigator, <strong>2025年度深圳市基础研究专项青年项目C类</strong> (2026-05-26 至 2028-05-25).</li>
</ul>
