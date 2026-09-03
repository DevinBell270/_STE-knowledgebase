import os

def generate_overview():
    print("Generating overview files...")
    
    # 1. overview/about-ste.md
    with open("overview/about-ste.md", "w") as f:
        f.write("""---
title: "About the School of Teacher Education (STE)"
type: "overview"
tags: [wku, ste, mission, accreditation, cebs, history, ransdell-hall]
source_url: "https://www.wku.edu/ste/"
last_updated: "2026-09-02"
summary: "Comprehensive overview of the School of Teacher Education at Western Kentucky University, including its institutional identity, mission, leadership, and role within CEBS."
---

# About the School of Teacher Education (STE)

The **School of Teacher Education (STE)** at [[Western Kentucky University]] (WKU) is the foundational academic and clinical preparation unit for educators within the [[overview/leadership-and-governance|College of Education and Behavioral Sciences (CEBS)]]. Tracing its roots directly to the Western Kentucky State Normal School established in 1906, STE has prepared thousands of classroom teachers, school leaders, instructional specialists, and curriculum directors across the Commonwealth of Kentucky and the nation.

Located in **[[overview/contact-and-facilities|Gary A. Ransdell Hall (GRH)]]**, the School operates with an enduring mission to prepare reflective decision-makers who foster inquiry, equity, and high academic achievement in diverse P-12 educational settings.

---

## Mission and Vision

### Mission Statement
> *"The School of Teacher Education prepares students to serve as reflective decision-makers in instructional settings for diverse learners. The professional education unit is a community of learners committed to life-long learning in their own lives, as well as fostering a spirit of inquiry in the lives of others."*

### Vision & Strategic Priorities
1. **Clinical Excellence:** Embedding teacher candidates in real-world school settings early and often, surpassing state requirements with 200+ documented clinical hours prior to student teaching (see [[pathways-and-certification/clinical-experiences-and-student-teaching|Clinical Experiences & Student Teaching]]).
2. **Accessible Pathways:** Developing affordable, high-return degree routes such as the **$350/credit hour [[funding-and-aid/educator-tuition-discount|Graduate Educator Tuition Discount]]** and [[pathways-and-certification/alternative-certification-option-6|Option 6 Alternative Certification]].
3. **Stackable Credentials:** Pioneering flexible 30-hour graduate models where practicing educators can earn a master's degree, achieve Kentucky Rank II or Rank I, and add high-demand endorsements simultaneously (see [[pathways-and-certification/rank-change-system|Rank Change System]] and [[pathways-and-certification/stackable-pathways|Stackable Pathways]]).
4. **Community and Regional Impact:** Serving as the primary workforce pipeline for regional school districts including Warren County Public Schools, Bowling Green Independent Schools, Daviess County, Jefferson County, and Fayette County (see [[centers-and-partnerships/regional-school-district-partnerships|Regional School District Partnerships]]).

---

## Accreditation and Quality Recognition

The School of Teacher Education and its professional education programs are fully accredited and recognized at both state and national levels:

*   **Council for the Accreditation of Educator Preparation (CAEP):** WKU's educator preparation programs meet rigorous national standards for clinical partnerships, candidate quality, candidate knowledge, and programmatic impact.
*   **Kentucky Education Professional Standards Board (EPSB):** All initial and advanced teacher certification programs are approved by the EPSB, leading directly to state teacher certification and rank progression.
*   **Southern Association of Colleges and Schools Commission on Colleges (SACSCOC):** Regional institutional accreditation for all conferred undergraduate (BS), graduate (MAT, MAE, MS), and specialist (Ed.S.) degrees.
*   **Association for Behavior Analysis International (ABAI):** Verified course sequence for the [[programs/graduate/applied-behavior-analysis-ms-0508|MS in Applied Behavior Analysis]].

For in-depth details on standard alignments, assessments, and continuous improvement systems, see [[overview/accreditation-and-standards|Accreditation & Standards]].

---

## Organizational Structure within CEBS

STE operates alongside partner units in the College of Education and Behavioral Sciences:
*   **School of Teacher Education (STE):** Initial and advanced P-12 teacher preparation, literacy, early childhood, special education, and instructional technology.
*   **School of Leadership and Professional Studies (SLPS):** Principal, superintendent, supervisor of instruction, and higher education administration programs.
*   **Department of Counseling and Student Affairs:** School counseling, mental health counseling, and student affairs administration.
*   **Department of Psychology:** School psychology (Ed.S.), clinical psychology, and psychological sciences.
*   **Office of Professional Educator Services (OPES):** Central administrative clearinghouse for teacher admissions, field placements, student teaching coordination, and state certification processing (CA-1 forms).

---

## Special Academic Initiatives and Centers

The School houses and partners with prominent research, clinical, and clinical preparation facilities:
*   **[[centers-and-partnerships/suzanne-vitale-clinical-education-complex|Suzanne Vitale Clinical Education Complex (CEC)]]:** Comprehensive facility housing the Kelly Autism Program and early childhood developmental clinics, serving individuals across the lifespan with autism and developmental delays.
*   **[[centers-and-partnerships/center-for-literacy|The Center for Literacy]]:** Directed by [[people/dr-jeremy-logsdon|Dr. Jeremy Logsdon]], providing specialized clinical reading interventions, diagnostic assessments, and community literacy outreach.
*   **[[centers-and-partnerships/skyteach-stem-program|SKyTeach STEM Program]]:** A premier math and science teacher preparation initiative co-administered with the Ogden College of Science and Engineering based on the national UTeach model.

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Index & Map of Content
*   [[README]]: Knowledge Base Architecture and Agent Usage Guide
*   [[overview/leadership-and-governance]]: Administrative Leadership and Coordinators
*   [[overview/contact-and-facilities]]: Physical Office, Building Maps, and Contact Info
*   [[overview/accreditation-and-standards]]: CAEP, EPSB, and KTPS Accreditation Details
*   [[pathways-and-certification/become-a-teacher]]: Prospective Student Portal & Career Paths
*   [[funding-and-aid/teacher-funding-guide]]: Complete Guide to Stackable Scholarships and Grants
""")

    # 2. overview/leadership-and-governance.md
    with open("overview/leadership-and-governance.md", "w") as f:
        f.write("""---
title: "STE Leadership and Governance"
type: "overview"
tags: [wku, ste, leadership, director, dean, governance, coordinators]
source_url: "https://www.wku.edu/ste/staff/"
last_updated: "2026-09-02"
summary: "Administrative leadership, governance committees, and program coordinator structure of the School of Teacher Education and CEBS."
---

# STE Leadership and Governance

The School of Teacher Education operates under a collaborative governance model led by the School Director, program coordinators, and the Dean's leadership team in the College of Education and Behavioral Sciences (CEBS).

---

## Executive Leadership

| Role | Leader | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| **Dean, College of Education and Behavioral Sciences** | [[people/dr-corinne-murphy|Dr. Corinne M. Murphy, Ph.D., BCBA-D]] | GRH 2038 | corinne.murphy@wku.edu | (270) 745-4664 |
| **Associate Dean, CEBS** | [[people/dr-jennifer-klemm|Dr. Jennifer P. Klemm, Ph.D.]] | GRH 2038 | jennifer.klemm@wku.edu | (270) 745-4664 |
| **Director, School of Teacher Education** | [[people/dr-susan-keesey|Dr. Susan Keesey, Ph.D.]] | GRH 1105 / 1005 | susan.keesey@wku.edu | (270) 745-5414 |
| **Assistant Director, STE & Program Coordinator** | [[people/dr-janet-tassell|Dr. Janet L. Tassell, Ph.D.]] | GRH 1105 / 1005 | janet.tassell@wku.edu | (270) 745-5306 |
| **Office Coordinator** | [[people/mandy-zeh|Mandy Zeh]] | GRH 1005 | mandy.zeh@wku.edu | (270) 745-5414 |
| **Academic Advisor** | [[people/meredith-stewart|Meredith Stewart]] | GRH 1005 | meredith.stewart@wku.edu | (270) 745-5414 |

---

## Program Leadership & Specialty Area Coordinators

*   **Elementary Education (Undergraduate & Graduate):**
    *   Coordinator / Contact: [[people/dr-janet-tassell|Dr. Janet L. Tassell]], [[people/dr-pamela-jukes|Dr. Pamela Jukes]], [[people/dr-jeanine-huss|Dr. Jeanine Huss]]
*   **Middle Grades & Secondary Education:**
    *   Faculty Leads: [[people/dr-erin-margarella|Dr. Erin Margarella]], [[people/dr-julia-mittelberg|Dr. Julia Mittelberg]]
*   **SKyTeach (STEM Teacher Education):**
    *   Education Co-Director: [[people/dr-martha-day|Dr. Martha M. Day]]
    *   Master Teachers: [[people/melanie-owens|Melanie Owens]], [[people/emily-perkins|Emily Perkins]], [[people/mr-rico-tyler|Rico Tyler]]
*   **Special Education (SPED / LBD / MSD):**
    *   Faculty Leads: [[people/dr-christina-noel|Dr. Christina R. Noel]], [[people/dr-ellen-casale|Dr. Ellen G. Casale]], [[people/dr-trudy-little|Dr. Trudy Little]], [[people/dr-shannon-pardue|Dr. Shannon Pardue]], [[people/dr-brooke-royalty|Dr. Brooke Royalty]], [[people/dr-leslee-bailey-tarbett|Dr. Leslee Bailey Tarbett]]
*   **Interdisciplinary Early Childhood Education (IECE):**
    *   Faculty Lead: [[people/dr-trudy-little|Dr. Trudy Little]]
*   **Literacy Program & Center for Literacy:**
    *   Director, Center for Literacy: [[people/dr-jeremy-logsdon|Dr. Jeremy Logsdon]]
    *   Literacy Faculty: [[people/dr-nancy-hulan|Dr. Nancy Hulan]], [[people/dr-kandy-smith|Dr. Kandy Smith]], [[people/sally-tooley|Sally Tooley]]
*   **Libraries, Informatics, and Technology in Education (LITE):**
    *   Faculty Lead: [[people/dr-andrea-paganelli|Dr. Andrea Paganelli]]
*   **Gifted Education and Talent Development:**
    *   Mahurin Professor & Executive Director: [[people/dr-julia-link-roberts|Dr. Julia Link Roberts]]
*   **Applied Behavior Analysis (MS):**
    *   Faculty: [[people/dr-ellen-casale|Dr. Ellen Casale]], [[people/bailey-payne|Bailey Payne]], [[people/dr-corinne-murphy|Dr. Corinne Murphy]]

---

## Governance Bodies & Committees

1.  **Professional Education Council (PEC):**
    *   University-wide curricular and policy body that governs all initial and advanced educator preparation programs across WKU. Approves new courses, program revisions, and candidate admission criteria.
2.  **Teacher Education Advisory Council:**
    *   Composed of regional P-12 superintendents, principals, clinical mentor teachers, and community stakeholders. Informs curriculum design, workforce alignment, and clinical placement policy.
3.  **School of Teacher Education Faculty Committee:**
    *   Internal body overseeing promotion and tenure, curriculum revisions, candidate assessment data, and CAEP continuous improvement metrics.

---

## Backlinks / Related Documents
*   [[overview/about-ste]]: Overview of STE History and Mission
*   [[overview/contact-and-facilities]]: Offices and Building Details
*   [[people/INDEX]]: Master Directory of all 39 Faculty and Staff Members
*   [[programs/INDEX]]: Academic Degree and Certificate Programs
*   [[centers-and-partnerships/INDEX]]: Centers and Research Facilities
""")

    # 3. overview/contact-and-facilities.md
    with open("overview/contact-and-facilities.md", "w") as f:
        f.write("""---
title: "STE Contact and Facilities"
type: "overview"
tags: [wku, ste, contact, facilities, ransdell-hall, phone, location]
source_url: "https://www.wku.edu/ste/"
last_updated: "2026-09-02"
summary: "Physical facilities, address, phone numbers, text line, office directories, and building locations for WKU STE."
---

# STE Contact and Facilities

The School of Teacher Education is headquartered in **Gary A. Ransdell Hall** on the main campus of Western Kentucky University in Bowling Green, Kentucky.

---

## Primary Contact Information

*   **Physical & Mailing Address:**
    ```text
    The School of Teacher Education
    Western Kentucky University
    Gary A. Ransdell Hall, Suite 1005
    1906 College Heights Blvd. #11030
    Bowling Green, KY 42101-1030
    ```
*   **Main Telephone:** [(270) 745-5414](tel:12707455414)
*   **Direct Student Text Line:** [(270) 721-8539](sms:+12707218539) *(SMS text only; cannot receive voice calls)*
*   **Departmental Website:** [https://www.wku.edu/ste/](https://www.wku.edu/ste/)
*   **Advising Inquiry Portal:** [[pathways-and-certification/become-a-teacher|Become a Teacher Portal]]
*   **Dean's Office (CEBS):** Gary A. Ransdell Hall 2038 | (270) 745-4664

---

## Facilities & Key Campus Locations

### 1. Gary A. Ransdell Hall (GRH)
Constructed in 2010 and LEED Gold certified, Gary A. Ransdell Hall is a modern 124,000-square-foot facility housing the College of Education and Behavioral Sciences.
*   **Suite 1005:** STE Central Administrative Office, Director's Office, Academic Advising, and Student Reception.
*   **Suite 1080–1089:** Faculty offices for Elementary, Middle Grades, Secondary, Literacy, Special Education, and LITE.
*   **Room 1019:** Center for Gifted Studies offices ([[people/dr-julia-link-roberts|Dr. Julia Link Roberts]]).
*   **Room 1033:** Educational Technology & Curriculum Specialists ([[people/christina-heady|Christina Heady]], [[people/mr-josiah-super|Dr. Josiah Super]]).
*   **Suite 2011:** **Office of Professional Educator Services (OPES)** — handles teacher admissions, field experience clearance, criminal background checks, student teaching applications, and CA-1 certification submissions.
*   **Classrooms & Labs:** High-tech classrooms equipped with smart interactive displays, flexible student pod seating, video recording suites for simulated teaching practice, and specialized early childhood curriculum rooms.

### 2. Suzanne Vitale Clinical Education Complex (CEC)
*   **Location:** 104 Alumni Ave, Bowling Green, KY 42101
*   **Purpose:** Houses the Kelly Autism Program, the Renshaw Early Childhood Center (Big Red School), and speech/behavioral clinics.
*   **Faculty Link:** Directed by [[people/dr-christina-noel|Dr. Christina R. Noel]]; provides vital clinical practice placements for [[programs/undergraduate/special-education-and-elementary-education-bs-5003|SPED]] and [[programs/graduate/applied-behavior-analysis-ms-0508|ABA]] candidates.

### 3. The Center for Literacy
*   **Location:** Gary A. Ransdell Hall (Ground Floor / Clinic Wing)
*   **Director:** [[people/dr-jeremy-logsdon|Dr. Jeremy Logsdon]]
*   **Phone:** (270) 745-4309
*   **Purpose:** Diagnostic reading evaluations, one-on-one reading clinic interventions for P-12 community children, and practical training labs for graduate candidates in the [[programs/graduate/literacy-education-mae-044|MAE in Literacy Education]].

### 4. Kelly Thompson Hall (KTH) - SKyTeach Suites
*   **Location:** Kelly Thompson Hall 1011
*   **Director:** [[people/dr-martha-day|Dr. Martha M. Day]]
*   **Staff:** Master Teachers [[people/melanie-owens|Melanie Owens]], [[people/emily-perkins|Emily Perkins]], and [[people/mr-rico-tyler|Rico Tyler]]
*   **Purpose:** Shared facility between CEBS and Ogden College housing inquiry-based STEM teaching equipment, robotics kits, and lesson planning workspaces for [[programs/undergraduate/science-and-mathematics-education-bs-774|SKyTeach candidates]].

---

## Social Media & Digital Channels

*   **X (formerly Twitter):** [@WKUSTE](https://x.com/WKUSTE)
*   **Facebook:** [WKU School of Teacher Education](https://www.facebook.com/wkuste/)
*   **University Directory:** [WKU TopNet Directory](https://topnet.wku.edu/pls/prod/dirpkg.prompt)

---

## Backlinks / Related Documents
*   [[overview/about-ste]]: Institutional background and mission
*   [[overview/leadership-and-governance]]: Departmental leadership and office directory
*   [[people/INDEX]]: Master Faculty & Staff Directory with individual office numbers
*   [[pathways-and-certification/admission-to-teacher-education]]: Professional Educator Services (OPES) Details
""")

    # 4. overview/accreditation-and-standards.md
    with open("overview/accreditation-and-standards.md", "w") as f:
        f.write("""---
title: "Accreditation and Professional Standards"
type: "overview"
tags: [wku, ste, accreditation, caep, epsb, intasc, ktps, standards]
source_url: "https://www.wku.edu/ste/"
last_updated: "2026-09-02"
summary: "Accreditation status, state approval by Kentucky EPSB, national accreditation by CAEP, and alignment with Kentucky Teacher Performance Standards (KTPS)."
---

# Accreditation and Professional Standards

Western Kentucky University's educator preparation programs are held to the highest state and national standards of rigor, clinical practice, and candidate performance.

---

## Accreditation Status

### 1. Council for the Accreditation of Educator Preparation (CAEP)
*   **Status:** Fully Accredited at both initial and advanced levels.
*   **Significance:** CAEP accreditation signifies that WKU's School of Teacher Education meets rigorous national peer-reviewed benchmarks for:
    *   Candidate content and pedagogical knowledge.
    *   Clinical partnerships and practice quality.
    *   Candidate selectivity and recruitment.
    *   Program impact on P-12 student learning.
    *   Continuous improvement supported by robust quality assurance systems.

### 2. Kentucky Education Professional Standards Board (EPSB)
*   **Status:** Approved Educator Preparation Provider (EPP).
*   **Authority:** Under Kentucky Revised Statutes (KRS 161.028), the EPSB is the state agency governing the licensing, certification, and rank change of all public school teachers and administrators in Kentucky.
*   **Outcome:** Graduates who successfully complete WKU degree programs and state-required assessments (Praxis Core, Praxis Subject Assessments, and PLT) qualify directly for Kentucky Provisional Teaching Certificates and Rank advancements.

### 3. Southern Association of Colleges and Schools Commission on Colleges (SACSCOC)
*   **Status:** Regional institutional accreditation covering all bachelor's, master's, specialist, and doctoral degrees granted by Western Kentucky University.

---

## Pedagogical Frameworks and Standard Alignments

All courses, field observation rubrics, and clinical evaluations in STE are built upon three interlocking standards frameworks:

### 1. Interstate Teacher Assessment and Support Consortium (InTASC) Model Core Teaching Standards
*   **The Learner and Learning:** Learner Development (Std 1), Learning Differences (Std 2), Learning Environments (Std 3).
*   **Content Knowledge:** Content Knowledge (Std 4), Application of Content (Std 5).
*   **Instructional Practice:** Assessment (Std 6), Planning for Instruction (Std 7), Instructional Strategies (Std 8).
*   **Professional Responsibility:** Professional Learning and Ethical Practice (Std 9), Leadership and Collaboration (Std 10).

### 2. Kentucky Teacher Performance Standards (KTPS)
Mandated by Kentucky Administrative Regulation (16 KAR 1:010), the KTPS mirrors the 10 InTASC standards and defines what every Kentucky educator must know and be able to demonstrate in the classroom. All student teaching candidate assessments and portfolio milestones evaluate mastery of KTPS indicators.

### 3. Specialty Professional Association (SPA) Standards
Individual programs within STE maintain national recognition through specialized national bodies:
*   **Elementary Education:** Association for Childhood Education International (ACEI) / National Association for the Education of Young Children (NAEYC).
*   **Middle Grades Education:** Association for Middle Level Education (AMLE).
*   **Special Education:** Council for Exceptional Children (CEC).
*   **Literacy / Reading Specialist:** International Literacy Association (ILA).
*   **Gifted Education:** National Association for Gifted Children (NAGC) / CEC Standards.
*   **School Media / LITE:** American Association of School Librarians (AASL) / ALA.
*   **Applied Behavior Analysis:** Association for Behavior Analysis International (ABAI) Verified Course Sequence (VCS).

---

## Title II State and Federal Reporting
Under Title II of the Higher Education Act, WKU STE annually publishes candidate enrollment, clinical field placement statistics, pass rates on state teacher certification licensure exams (Praxis), and employment placement data. WKU candidates consistently achieve high pass rates on Kentucky state licensure assessments.

---

## Backlinks / Related Documents
*   [[overview/about-ste]]: Institutional identity and background
*   [[overview/leadership-and-governance]]: Governance bodies and faculty committees
*   [[pathways-and-certification/admission-to-teacher-education]]: Praxis and GPA entry criteria
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: 200 clock hours and clinical rubrics
*   [[pathways-and-certification/rank-change-system]]: State rank advancement regulations
""")

    # 5. overview/INDEX.md
    with open("overview/INDEX.md", "w") as f:
        f.write("""---
title: "School Overview Map of Content"
type: "index"
tags: [wku, ste, overview, index, map-of-content]
source_url: "https://www.wku.edu/ste/"
last_updated: "2026-09-02"
summary: "Map of Content (MOC) for the School of Teacher Education overview, mission, leadership, facilities, and accreditation."
---

# School Overview Map of Content

This hub provides comprehensive institutional context for Western Kentucky University's School of Teacher Education.

## Overview Documents

*   [[overview/about-ste|About the School of Teacher Education]]
    *   Mission, vision, historical background, institutional home in CEBS, and core strategic priorities.
*   [[overview/leadership-and-governance|Leadership and Governance]]
    *   Executive administration (Dean, Director, Associate Dean), program coordinators, and governing councils (PEC).
*   [[overview/contact-and-facilities|Contact and Facilities]]
    *   Physical address in Gary A. Ransdell Hall, direct phone numbers, student text line (270-721-8539), and campus clinic sites.
*   [[overview/accreditation-and-standards|Accreditation and Standards]]
    *   CAEP national accreditation, Kentucky EPSB approval, InTASC/KTPS standards alignments, and SPA recognition.

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Master Index
*   [[README]]: Agent Architecture and Usage Standards
*   [[people/INDEX]]: Faculty and Staff Directory
*   [[programs/INDEX]]: Academic Degrees and Programs Matrix
*   [[pathways-and-certification/INDEX]]: Teacher Certification Pathways
""")

    print("Overview files generated successfully.")

if __name__ == "__main__":
    generate_overview()
