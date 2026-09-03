---
title: "School of Teacher Education Knowledge Base - Architecture & Guide"
type: "overview"
tags: [wku, ste, readme, guide, architecture, llm-wiki, karpathy]
source_url: "https://www.wku.edu/ste/"
last_updated: "2026-09-02"
summary: "Architectural overview, conventions, and instructions for how autonomous AI agents should navigate the STE Knowledge Base."
---

# School of Teacher Education (STE) Knowledge Base

## Overview
This repository contains a comprehensive, highly interconnected Markdown Knowledge Base representing the **School of Teacher Education (STE)** in the College of Education and Behavioral Sciences (CEBS) at Western Kentucky University (WKU).

Built in the style of **Andrej Karpathy's LLM Knowledge Bases / Personal Wikis**, this repository acts as a persistent, high-density, authoritative source of truth for autonomous AI agents and educator workflows.

---

## Architectural Principles

1.  **Knowledge Compilation:** Rather than querying dispersed web pages and 80,000-character course catalogs repeatedly, institutional knowledge has been distilled into structured, atomic Markdown documents.
2.  **Standardized Metadata:** Every file features a YAML frontmatter block containing:
    ```yaml
    ---
    title: "Document Title"
    type: "overview | person | program | certificate | pathway | funding | curriculum | center | analytics | index"
    tags: [tag1, tag2, tag3]
    source_url: "Official source URL or archival reference"
    last_updated: "2026-09-02"
    summary: "Dense 1-2 sentence executive summary."
    ---
    ```
3.  **Dual Link Architecture:** Notes utilize both **Obsidian-style wikilinks** (`[[path/to/note|Anchor Text]]` or `[[note]]`) and standard relative Markdown links (`[Anchor Text](path/to/note.md)`), allowing seamless graph traversal in Obsidian, IDEs, and LLM text parsers.
4.  **Bidirectional Backlinks:** Every document includes a dedicated `## Backlinks / Related Documents` section at the end of the file, establishing explicit relational links across people, programs, policies, and facilities.
5.  **No Placeholders:** Deep, factual, institutional details are fully articulated, including exact degree reference codes (e.g., Ref 527, 0500, 0495), course prefixes and numbers, clinical clock hours, state certification requirements (EPSB / CAEP), faculty credentials, office numbers, emails, phone numbers, and tuition dollar amounts.
6.  **Active Linting & Health Checks:** Includes a dedicated verification script (`tools/lint_kb.py`) to validate link integrity, metadata presence, and zero orphan files.

---

## Directory Organization

```text
_STE-knowledgebase/
├── INDEX.md                                # Master Map of Content (MOC) & Quick Reference
├── README.md                               # Architecture Guide and Conventions
├── web-reports/                            # 9 Historical GA4 / BigQuery PDF Reports (Dated Snapshot: 2026-09-02)
├── overview/                               # Institutional Identity, Mission, Governance, Facilities
│   ├── INDEX.md
│   ├── about-ste.md
│   ├── leadership-and-governance.md
│   ├── contact-and-facilities.md
│   └── accreditation-and-standards.md
├── people/                                 # Directory of All 41 Faculty and Staff Members
│   ├── INDEX.md
│   ├── dr-susan-keesey.md                  # STE Director
│   ├── dr-corinne-murphy.md                # CEBS Dean
│   ├── dr-janet-tassell.md                 # Assistant Director & Math Lead
│   └── [38 other individual profiles]
├── programs/                               # Academic Degrees, Rank Programs, and Certificates
│   ├── INDEX.md                            # Master Program Matrix
│   ├── undergraduate/                      # BS in ELED (527), IECE (526), MGED (5001), SMED (774), SPED (5003)
│   ├── graduate/                           # MAE 0500, MAT 0495, SPED MAT 0456, LITE 0497, ID 0428, EdS 0503, Rank I
│   └── certificates-and-endorsements/      # Elementary Math (0485), Gifted (1764), AI (1796), Endorsements Guide
├── pathways-and-certification/             # Recruitment, Admissions, Rank Change, Option 6, Field Hours
│   ├── INDEX.md
│   ├── become-a-teacher.md
│   ├── admission-to-teacher-education.md
│   ├── rank-change-system.md
│   ├── stackable-pathways.md
│   ├── alternative-certification-option-6.md
│   └── clinical-experiences-and-student-teaching.md
├── funding-and-aid/                        # Financial Aid, Stackable Funding, $350 Discount, Scholarships
│   ├── INDEX.md
│   ├── teacher-funding-guide.md
│   ├── educator-tuition-discount.md
│   └── scholarships-and-grants.md
├── courses-and-curriculum/                 # Catalog Prefixes and Teacher Leader Core
│   ├── INDEX.md
│   ├── course-prefixes-and-descriptions.md
│   └── teacher-leader-core-curriculum.md
├── centers-and-partnerships/               # Clinical Complexes, Literacy Clinic, SKyTeach, Districts
│   ├── INDEX.md
│   ├── suzanne-vitale-clinical-education-complex.md
│   ├── center-for-literacy.md
│   ├── skyteach-stem-program.md
│   └── regional-school-district-partnerships.md
├── analytics-and-insights/                 # Synthesis of BigQuery GA4 Reports & Institutional Census
│   ├── INDEX.md
│   ├── enrollment-and-retention-trends.md
│   └── ga4-web-traffic-and-student-demand.md
├── opes/                                   # Office of Professional Educator Services (Supporting Unit)
│   ├── INDEX.md                            # OPES Master Map of Content
│   ├── overview-and-staff.md               # Administrative Operations & Staff in GRH 1092
│   ├── teacher-admissions.md               # Orientation, 2.75 GPA, Praxis CORE, Clearances
│   ├── field-experience.md                 # 200-Hour Pre-Service Clinical Protocol (16 KAR 5:040)
│   ├── student-teaching-procedures.md      # Watermark SL&L Application, Deadlines, 70 Days
│   ├── co-teaching-model.md                # 16 KAR 5:040 Cooperating Teacher Training & Tuition Waiver
│   ├── teacher-certification-services.md   # CA-1 Application, EPSB/OELE, Statement of Eligibility
│   ├── proficiency-evaluations-alternative-route.md # 16 KAR 5:030 Portfolio Review ($500 Fee, ELP)
│   └── praxis-exams-and-support.md         # Praxis Core/II Passing Scores, Codes 1901 & 7283
└── tools/
    └── lint_kb.py                          # Link Verifier and Knowledge Base Auditor
```

---

## Running the Knowledge Base Linter

To audit the knowledge base for broken links, missing metadata, or orphaned files, execute:
```bash
python3 tools/lint_kb.py
```

---

## Primary Institutional Contacts
*   **Physical Office:** Gary A. Ransdell Hall, Suite 1005, Bowling Green, KY 42101
*   **Phone:** (270) 745-5414
*   **Prospective Student Text Line:** (270) 721-8539
*   **Department Website:** [https://www.wku.edu/ste/](https://www.wku.edu/ste/)
