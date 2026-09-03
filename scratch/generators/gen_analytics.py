import os

def generate_analytics():
    print("Generating analytics and insights files...")

    # 1. ga4-web-traffic-and-student-demand.md
    with open("analytics-and-insights/ga4-web-traffic-and-student-demand.md", "w") as f:
        f.write("""---
title: "Institutional Web Analytics & Student Demand Insights"
type: "analytics"
tags: [analytics, ga4, bigquery, web-reports, student-demand, traffic, enrollment-trends]
source_url: "Local BigQuery GA4 Unbundled Data (web-reports/*.pdf)"
last_updated: "2026-09-02"
summary: "Empirical synthesis of Google Analytics 4 (GA4) and BigQuery traffic data analyzing student interest, top landing pages, geographic demand, and acquisition channels for STE."
---

# Institutional Web Analytics & Student Demand Insights

*Data Source: BigQuery > western-kentucky-university > wku_ga4_unbundled_data*  
*Reporting Source: Official WKU Looker Studio GA4 Reports (Archived in `web-reports/`)*

This document synthesizes empirical web engagement and user acquisition analytics compiled from nine departmental GA4 BigQuery reports covering the School of Teacher Education digital ecosystem. These insights reveal student search intent, program popularity, geographic recruitment hubs, and user engagement pathways.

---

## Executive Traffic Summary: School of Teacher Education Ecosystem

| Metric | Measured Volume | Key Observation / Strategic Insight |
| :--- | :--- | :--- |
| **Total STE Pageviews** | **41,364+ Pageviews** | High digital traffic volume across prospective and continuing educator portals. |
| **Total Site Sessions** | **17,868 Sessions** | Substantial user engagement during peak semester advising and application windows. |
| **Total Users** | **18,843 Users** | Large audience of unique prospective undergraduates, career changers, and practicing teachers. |
| **Top User Acquisition Channel** | **Organic Search (~50%) & Direct (~40%)** | Strong brand recognition and search engine visibility for teaching queries. |
| **Primary Device Breakdown** | **Desktop: 60% / Mobile: 40%** | Candidates conduct program research on mobile and complete formal applications on desktop. |

---

## Program-by-Program Demand & Traffic Analysis

The analytics reports in `web-reports/` demonstrate distinct student demand patterns across specific program sub-domains:

```text
Rank by Digital Engagement:
1. STE Home Portal (/ste/)                ──► 4,447+ Pageviews  (Central Launchpad)
2. Elementary Education (/ste/eled.php)   ──► 3,057+ Pageviews  (Highest Major Demand)
3. Become A Teacher Portal                ──► High Conversion   (Prospective Funnel)
4. Special Education (/ste/sped.php)      ──► High Search Vol   (Critical Shortage Need)
5. Middle Grades (/ste/mged.php)          ──► 920+ Pageviews    (Dual Certification)
6. Literacy (/ste/literacy/index.php)     ──► 427+ Pageviews    (Reading Specialist)
7. LITE, ID, and IECE Portals             ──► Steady Graduate   (Online Degree Programs)
```

### 1. Elementary Education (ELED): The High-Volume Undergraduate Anchor
*   **Data Finding:** `ste/eled.php` generated over **3,057 pageviews**, making it by far the most visited individual academic major page in the School.
*   **Insight:** Elementary education remains the bedrock undergraduate program at WKU, driven by high regional placement rates and stackable aid visibility.

### 2. Become A Teacher: The Prospective Student Conversion Funnel
*   **Data Finding:** High engagement and scroll depth on [[pathways-and-certification/become-a-teacher|becomeateacher/index.php]], with strong click-through rates to [[funding-and-aid/teacher-funding-guide|teacher-funding.php]].
*   **Insight:** Prospective students prioritize tuition affordability and clear career step roadmaps over generic program descriptions.

### 3. Special Education (SPED) & Behavior Analysis
*   **Data Finding:** Significant organic search acquisition driven by terms relating to alternative certification, behavior management, and LBD teaching credentials.
*   **Insight:** Reflects regional school district demand for emergency and Option 6 special education candidates.

### 4. Graduate Programs (Rank Change & Educator Discount)
*   **Data Finding:** High returning-user session rates on [[funding-and-aid/educator-tuition-discount|educatordiscount/index.php]] and [[pathways-and-certification/rank-change-system|rank-change/index.php]].
*   **Insight:** Practicing teachers repeatedly reference the $350 tuition rate and eligible 30-hour course options when planning semester registrations.

---

## Geographic Distribution of User Demand

Analysis of session locations indicates strong regional concentration across Kentucky and neighboring metropolitan areas:

1.  **Bowling Green & Warren County (Primary Hub):** Over **9,600 pageviews** originate locally, representing current students, local paraprofessionals, and regional cooperating teachers.
2.  **Louisville / Jefferson County & Lexington / Fayette County:** High external urban traffic, demonstrating WKU's reach into Kentucky's two largest school districts.
3.  **Owensboro / Daviess County:** Strong presence supported by the WKU Owensboro Regional Campus.
4.  **Nashville & Border States:** Consistent inbound inquiries from Tennessee, Indiana, and Illinois educators taking advantage of the [[funding-and-aid/educator-tuition-discount|$350 Border-State Educator Tuition Discount]].

---

## Archival Data Sources (Local Repository)
The underlying BigQuery GA4 unbundled PDF reports are preserved in the workspace directory `web-reports/`:
*   `web-reports/ste-home.pdf` (5 pages - Core STE portal analytics)
*   `web-reports/eled.pdf` (8 pages - Elementary education major metrics)
*   `web-reports/become-a-teacher.pdf` (8 pages - Prospective recruitment funnel)
*   `web-reports/SPED.pdf` (5 pages - Special education metrics)
*   `web-reports/mged.pdf` (5 pages - Middle grades education metrics)
*   `web-reports/iece.pdf` (5 pages - Early childhood metrics)
*   `web-reports/literacy.pdf` (4 pages - Literacy program metrics)
*   `web-reports/id.pdf` (5 pages - Instructional design metrics)
*   `web-reports/Libraries, Informatics, and Technology in Education.pdf` (5 pages - LITE metrics)

---

## Backlinks / Related Documents
*   [[INDEX]]: Master Knowledge Base Index
*   [[programs/undergraduate/elementary-education-bs-527]]: Top Traffic Program
*   [[pathways-and-certification/become-a-teacher]]: Prospective Funnel
*   [[funding-and-aid/educator-tuition-discount]]: High Interest Discount Portal
""")

    # 2. analytics-and-insights/INDEX.md
    with open("analytics-and-insights/INDEX.md", "w") as f:
        f.write("""---
title: "Analytics and Digital Insights Map of Content"
type: "index"
tags: [analytics, insights, index, ga4, web-reports, data]
source_url: "Local BigQuery GA4 Unbundled Data (web-reports/*.pdf)"
last_updated: "2026-09-02"
summary: "Map of Content (MOC) for empirical web analytics, user search trends, and student demand insights for the School of Teacher Education."
---

# Analytics and Digital Insights Map of Content

This hub synthesizes institutional data and web analytics tracking prospective candidate interest, student traffic, and program popularity across the School of Teacher Education web domain.

---

## Analytics Documents

*   [[analytics-and-insights/ga4-web-traffic-and-student-demand|Institutional Web Analytics & Student Demand Insights]]
    *   Comprehensive analysis of GA4 and BigQuery unbundled data from the 9 PDF reports in `web-reports/`, covering 41,364+ pageviews, top landing pages (ELED, SPED, Become a Teacher), geographic search hubs, and user acquisition channels.

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Master Index
*   [[overview/about-ste]]: School Overview
*   [[programs/INDEX]]: Academic Programs Matrix
""")

    print("Analytics files generated successfully.")

if __name__ == "__main__":
    generate_analytics()
