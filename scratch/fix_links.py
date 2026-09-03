import re

# 1. Fix overview/about-ste.md
path = "overview/about-ste.md"
with open(path, "r", encoding="utf-8") as f:
    text = f.read()
text = text.replace("[[Western Kentucky University]]", "**Western Kentucky University**")
with open(path, "w", encoding="utf-8") as f:
    f.write(text)
print("Fixed overview/about-ste.md")

# 2. Fix README.md frontmatter
path = "README.md"
with open(path, "r", encoding="utf-8") as f:
    readme_text = f.read()

fm = """---
title: "School of Teacher Education Knowledge Base - Architecture & Guide"
type: "overview"
tags: [wku, ste, readme, guide, architecture, llm-wiki, karpathy]
source_url: "https://www.wku.edu/ste/"
last_updated: "2026-09-02"
summary: "Architectural overview, conventions, and instructions for how autonomous AI agents should navigate the STE Knowledge Base."
---

"""
if not readme_text.startswith("---"):
    with open(path, "w", encoding="utf-8") as f:
        f.write(fm + readme_text)
    print("Added frontmatter to README.md")

