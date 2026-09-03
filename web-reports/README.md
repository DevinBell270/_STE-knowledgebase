# School of Teacher Education — Web Reports Archive

This directory preserves historical snapshots of institutional Google Analytics 4 (GA4) Looker Studio PDF reports generated from the BigQuery `wku_ga4_unbundled_data` dataset.

## Naming & Versioning Convention

All reports follow the dated suffix naming convention:
```text
<report-name>_<YYYY-MM-DD>.pdf
```

This ensures:
1. **Side-by-Side Comparison:** Files sort cleanly next to each other by report topic in alphabetical order (e.g., `eled_2026-09-02.pdf` sits directly beside future exports like `eled_2026-10-02.pdf`).
2. **Lossless Archival:** Existing data is never overwritten when new monthly or quarterly Looker Studio batches are downloaded.
3. **Longitudinal Analysis:** Agents and institutional researchers can easily compare traffic trends, session changes, and recruitment funnel progression across time periods.

## Baseline Snapshot: September 2, 2026 (`2026-09-02`)

The baseline dataset established on **September 2, 2026** consists of nine departmental PDF reports:

| Report Filename | Program / Domain Focus | Pages | Primary Metrics Tracked |
| :--- | :--- | :--- | :--- |
| `ste-home_2026-09-02.pdf` | STE Homepage / Main Portal (`/ste/`) | 5 | Overall school portal traffic, top cities, channels |
| `eled_2026-09-02.pdf` | Elementary Education B.S. (`/ste/eled.php`) | 8 | Top academic major traffic, user journeys, acquisition |
| `become-a-teacher_2026-09-02.pdf` | Become a Teacher Funnel (`/becomeateacher/`) | 8 | Prospective student landing pages, funding conversions |
| `SPED_2026-09-02.pdf` | Special Education (`/ste/sped.php`) | 5 | Undergraduate dual major & Option 6 demand |
| `mged_2026-09-02.pdf` | Middle Grades Education (`/ste/mged.php`) | 5 | Middle level major demand & regional traffic |
| `iece_2026-09-02.pdf` | Interdisciplinary Early Childhood (`/ste/iece.php`) | 5 | Birth-to-Primary early educator demand |
| `literacy_2026-09-02.pdf` | Literacy Program (`/ste/literacy/`) | 4 | Graduate reading specialist demand |
| `id_2026-09-02.pdf` | Instructional Design (`/ste/id.php`) | 5 | Online master's and certificate demand |
| `Libraries, Informatics, and Technology in Education_2026-09-02.pdf` | LITE Program (`/ste/lite/`) | 5 | School media and educational tech demand |

## Longitudinal Comparison Workflow

When downloading future Looker Studio export reports:
1. Append the new snapshot date suffix to the filename (e.g., `eled_<YYYY-MM-DD>.pdf`).
2. Deposit the file into this `web-reports/` directory.
3. Compare key metrics (Pageviews, Sessions, Users, Organic Search % vs Direct %, Top Cities) against the `2026-09-02` baseline.
4. Record comparative insights in [`analytics-and-insights/ga4-web-traffic-and-student-demand.md`](../analytics-and-insights/ga4-web-traffic-and-student-demand.md).
