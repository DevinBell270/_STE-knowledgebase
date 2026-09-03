# WKU Elementary Education B.S. — Recruitment Mockups

Two standalone designs live in this folder. Serve the directory and compare them.

```bash
cd web-template
python3 -m http.server 8765
```

| Option | URL | Intent |
| :--- | :--- | :--- |
| **A — Brochure** | http://localhost:8765/ | Wide desktop landing page: persona tabs, aid calculator, faculty grid. |
| **B — Phone recruiter** | http://localhost:8765/option-b/ | Built for ELED’s **34% mobile engagement** (vs 48% desktop). First screen is SMS. |

---

## Option B (new)

GA4 on `/ste/eled.php` (`web-reports/eled_2026-09-02.pdf`): ~40% of pageviews are mobile, mobile engagement is **34.22%**, direct traffic engages at **26.67%**, RFIs are up **152%** when people actually reach a form, and SMS on the live page sits thousands of pixels down. Chicago, Indianapolis, and Atlanta already show up in city tables next to Bowling Green and Louisville.

Option B is a **390px handset**, not a squashed brochure:

1. **One-screen cover** — P–5 promise + **Text STE** in the thumb zone. Direct visitors get an answer before they bounce.
2. **Geography first** — Kentucky / border / farther (Chicago–Atlanta). Tuition is $12,072 resident vs $13,500 non-resident per semester; TIP is $7,068. The page does not pretend everyone is in Warren County.
3. **Who are you** as stacked buttons, not tabs — freshman, KCTCS transfer, bachelor’s holder → MAT, certified teacher → $350 MAE.
4. **Aid as a tower**, not a checkbox spreadsheet.
5. **Tap-to-text thread** with Meredith Stewart. Prefills Messages. Primary mobile conversion; the two-field **Ask** sheet is secondary (analytics: mobile starts forms, desktop finishes them).
6. **Dock never leaves:** Text STE · Ask · Apply.

Do not ship Option B’s desktop “phone frame” to production. On a real phone it is full-bleed. The frame is only so reviewers see the mobile problem on a monitor.

---

## Option A (original)

Open `index.html` in a browser (or serve the folder) to review the wide template.

It is not a CMS export. Copy, CTAs, calculator math, faculty, and curriculum are sourced from the STE knowledge base and checked against the live page and the September 2, 2026 GA4 snapshot.

Files:

```text
web-template/
├── index.html              # Option A
├── styles.css
├── app.js
├── option-b/               # Option B (mobile recruiter)
│   ├── index.html
│   ├── styles.css
│   └── app.js
├── README.md
└── assets/images/
```

---

## What we audited on the live page

Live URL: [wku.edu/ste/eled-bs.php](https://www.wku.edu/ste/eled-bs.php)

GA4 snapshot: `web-reports/eled_2026-09-02.pdf` (filter on the ELED URL family; 3,057 of 3,064 pageviews still hit `eled.php`, so the `eled-bs.php` rename is a tracking split to fix in production).

| Metric | Finding | What the mockup does |
| :--- | :--- | :--- |
| **3,064 pageviews · 504 sessions · 42.1% engagement (−14.5%)** | Traffic is up; time-on-intent is down. Direct visits engage at **26.67% (−42%)**. | Hero states the credential, hours, aid, SMS, and advisor in the first screen. Persona tabs stop “everyone copy.” |
| **Desktop 59.5% / mobile ~40%**; mobile engagement **34%** vs desktop **48%**; conversions **62% desktop / 38% mobile** | Mobile researches; desktop converts. No sticky apply/text bar. SMS sits ~2,300px down. | Sticky Apply / Info / Text bar under 768px. SMS in the utility bar, hero, advising, FAQ, and footer. |
| **53 RFIs (+152%)**, almost all `rfi_sub_conv` | The form works when people find it. Hero CTA leaves the site (`apply.wku.edu/register/learnmore`). No on-page form. | Native `<dialog>` lead form plus the official apply link. Production should POST to the existing RFI endpoint. |
| **Organic ~ google 1,110 users**; Bing 128 | Search is the acquisition engine. Live H1/H2 duplicate “Earn Your Elementary Education B.S.” Four empty H2s in the chrome. | Search-shaped title and H1: P–5, hours, certification. FAQ answers GPA, hours, cost, online, contact. |
| **kctcs.edu and fcps.net referrals** | Transfers and certified teachers land on a freshman brochure. Graduate programs are stuffed into collapsed accordions. | Four personas: HS senior, KCTCS/transfer, career changer → MAT, certified → $350 MAE. Related programs are visible cards, not hidden accordions. |
| **Cities:** Bowling Green, Louisville, Chicago, Owensboro, Elizabethtown, Lexington, Indianapolis | Regional hiring story is a tab (`9.4%` vs employers). | Employers listed in one grid. City chips from the GA4 report. |
| **Funding mentioned, never itemized** | “Stackable scholarships” with no Pell/CAP/KHEAA/TEACH/KEES amounts. Become-a-Teacher analytics say cost is the conversion driver. | Interactive stack vs **$12,072** 2025–26 KY resident tuition. Graduate panel isolated so UG visitors are not sold $350/hour. |
| **Catalog errors on the live page** | ELED 365 labeled “teaching methods”; ELED 406 labeled science; ELED 490 listed as 5–10 hours. No 128-hour total, no 2.75 GPA, no Praxis/ACT, no Meredith Stewart. Faculty office listed as GRH 1104. Image alt leftover: “The Talley Family Counseling Center.” | Curriculum and admission match `programs/undergraduate/elementary-education-bs-527.md`. Advisor + four ELED faculty. Correct image alt text. |

---

## Knowledge-base facts used on the page

- Program: Elementary Education, B.S., Ref. 527, 128 hours, P–5, 441 majors (Fall 2026 Week −10), 115 FTFY orientation yield (+40.2% vs 2024).
- Clinicals: 200+ hours (16 KAR 5:040), ELED 490 = 10 hours / 16 weeks / 70 days, Watermark deadlines Oct 15 / Apr 15.
- Aid: Pell $7,395 · CAP $5,300 · KHEAA Teacher $5,000 · TEACH $4,000 · KEES up to $2,500 · FAFSA 002002.
- Graduate (off-ramp only): $350/hour through 2029–30; MAE 0500 30 hours.
- People: Meredith Stewart (GRH 1005), Dr. Janet Tassell, Dr. Pamela Jukes, Dr. Jeanine Huss, Dr. Erin Coffield-Feeney.
- Testimonial: Jayla Sharp (ELED) from `pathways-and-certification/become-a-teacher.md`.

---

## How to reuse this for another STE program

1. Duplicate `index.html`.
2. Replace title, H1, catalog ref, hours, certification band, curriculum tables, and faculty.
3. Keep the architecture: utility SMS, hero dual CTA, persona switcher, aid calculator, clinical milestones, named advisor, sticky mobile bar, on-page RFI dialog.
4. Do not put Rank I / MAE copy in the undergraduate hero.

Undergraduate advising stays **Meredith Stewart**. Graduate coordination stays **Dr. Janet Tassell**. SMS stays **(270) 721-8539** (text only).
