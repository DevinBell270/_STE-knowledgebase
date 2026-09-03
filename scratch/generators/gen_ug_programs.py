import os

def generate_ug_programs():
    print("Generating undergraduate program files...")

    # 1. elementary-education-bs-527.md
    with open("programs/undergraduate/elementary-education-bs-527.md", "w") as f:
        f.write("""---
title: "Elementary Education, Bachelor of Science (Ref: 527)"
type: "program"
tags: [undergraduate, eled, degree, bachelor-of-science, elementary-education, p-5-certification]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/elementary-education-bs/"
last_updated: "2026-09-02"
summary: "128-credit hour undergraduate degree leading to Kentucky initial certification in Elementary Education (Grades P-5)."
---

# Elementary Education, Bachelor of Science (Ref: 527)

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Bachelor of Science in Elementary Education (Reference # 527)** is a nationally accredited, 128-credit hour degree program designed to prepare candidates to teach children in kindergarten through fifth grade (Grades P-5). Grounded in evidence-based pedagogical practice, structured literacy, and inquiry mathematics, this program integrates over 200 clock hours of field experience prior to a culminating 16-week student teaching semester.

---

## Program Summary & Key Facts

| Feature | Specification |
| :--- | :--- |
| **Degree Awarded** | Bachelor of Science (B.S.) |
| **WKU Catalog Reference Number** | **527** |
| **Total Credit Hours Required** | **128 Hours** |
| **Kentucky Certification Issued** | Elementary School, Grades P–5 (Kentucky Provisional Certificate) |
| **Delivery Mode** | On-Campus (Bowling Green) with local school clinical placements |
| **Accreditation** | CAEP Accredited; Approved by Kentucky EPSB |
| **Primary Faculty Contacts** | [[people/dr-janet-tassell|Dr. Janet L. Tassell]], [[people/dr-pamela-jukes|Dr. Pamela Jukes]], [[people/dr-jeanine-huss|Dr. Jeanine Huss]], [[people/dr-erin-coffield-feeney|Dr. Erin Coffield-Feeney]] |
| **Academic Advisor** | [[people/meredith-stewart|Meredith Stewart]] (GRH 1005) |

---

## Admission Requirements to Teacher Education

Prior to enrolling in upper-division restricted methods courses (ELED 355, 365, 405, 406, 465), students must gain formal admission to the Professional Education Unit through the [[pathways-and-certification/admission-to-teacher-education|Office of Professional Educator Services (OPES)]]:

1.  **Academic Standing:** Minimum overall cumulative GPA of **2.75** or higher (or 3.0 on last 30 credit hours).
2.  **State-Mandated Testing (EPSB):**
    *   **Praxis Core Academic Skills for Educators (CASE):** Reading (156), Writing (162), Math (150); OR
    *   **Qualifying ACT Scores:** Composite 22, OR individual scores: Reading 20, English 18, Math 19.
3.  **Foundational Coursework:** Grade of "C" or higher in **EDU 250** (Introduction to Teacher Education) and ENG 100 / COMM 145.
4.  **Clearances:** Current state and federal criminal background check, signed Kentucky Teacher Code of Ethics commitment, and physical/TB assessment.

---

## Curriculum Structure (128 Hours)

The curriculum combines WKU Colonnade general education, teacher education foundations, elementary content requirements, and a professional education block.

### 1. Colonnade General Education (39 Hours)
*   **Foundations:** College Composition (ENG 100), Writing in the Disciplines (ENG 300), Human Communication (COMM 145), Quantitative Reasoning (MATH 116 or higher), Literary Studies (ENG 200), World History (HIST 101 or 102).
*   **Explorations:** Arts & Humanities, Social & Behavioral Sciences (GEOG 110 recommended), Natural & Physical Sciences with Lab (BIOL 113/114 or GEOL 102).
*   **Connections:** Systems (GEOG 380), Social & Cultural, Local to Global.

### 2. Elementary Content & Related Core (24–27 Hours)
*   **MATH 205:** Number Systems and Number Theory for Elementary Teachers (3 hrs)
*   **MATH 206:** Fundamentals of Geometry for Elementary Teachers (3 hrs)
*   **MATH 308:** Rational Numbers & Data for Elementary Teachers (3 hrs)
*   **GEOG 110:** World Regional Geography (3 hrs)
*   **HIST 240 / HIST 241:** United States History to / since 1865 (3 hrs)
*   **Physical Science Requirement:** (e.g., ASTR 104, PHYS 105, or CHEM 105) (3 hrs)
*   **Biological Science Requirement:** (e.g., BIOL 113 or GEOL 111) (3 hrs)

### 3. Professional Education Sequence (62 Hours)
*   **EDU 250:** Introduction to Teacher Education (3 hrs)
*   **PSY 310:** Educational Psychology: Development and Learning (3 hrs)
*   **SPED 330:** Introduction to Exceptional Education: Diversity in Learning (3 hrs)
*   **LTCY 320:** Foundations of Literacy Instruction (3 hrs)
*   **LTCY 420:** Reading in the Primary Grades (3 hrs)
*   **ELED 345:** Foundations of Elementary Educational Practice (3 hrs)
*   **ELED 355:** Student Diversity in the Elementary Classroom (3 hrs)
*   **ELED 365:** Teaching Science in the Elementary School (3 hrs)
*   **ELED 405:** Teaching Mathematics in the Elementary School (3 hrs)
*   **ELED 406:** Teaching Social Studies in the Elementary School (3 hrs)
*   **ELED 465:** Senior Projects in Elementary Education (3 hrs)
*   **EDU 489:** Student Teaching Seminar (3 hrs)
*   **ELED 490:** Student Teaching - Elementary (10 hrs) *(Full-time 16-week placement)*

---

## Clinical Experience Milestones

*   **Pre-Student Teaching:** Candidates complete **200+ documented clock hours** across diverse school settings, engaging in classroom observation, one-on-one tutoring, small-group remediation, and family engagement events.
*   **Student Teaching Semester:** A full-time, 16-week clinical immersive internship in an accredited public elementary school under the joint guidance of a cooperating mentor teacher and a WKU clinical supervisor (see [[people/katie-decker|Katie Decker]], [[people/kim-taylor|Kim Taylor]]).

---

## Financial Aid & Stackable Scholarships

Students majoring in Elementary Education are eligible for comprehensive stackable aid:
*   **KHEAA Teacher Scholarship:** Up to $5,000/year for Kentucky residents committing to teach in Kentucky.
*   **Federal TEACH Grant:** Up to $4,000/year for candidates who agree to teach in high-need fields/schools.
*   **Kentucky Teacher Recruitment Loan Program (TRLP):** Forgivable loans for education majors.
*   **Full details:** See [[funding-and-aid/teacher-funding-guide|Stackable Teacher Funding Guide]].

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[pathways-and-certification/become-a-teacher]]: Prospective Elementary Educator Overview
*   [[pathways-and-certification/admission-to-teacher-education]]: OPES Admission Guidelines
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: 200-Hour Clinical Protocol
*   [[people/dr-janet-tassell]]: Elementary Math Lead & Assistant Director
*   [[people/dr-pamela-jukes]]: Elementary Education Professor
*   [[funding-and-aid/teacher-funding-guide]]: Funding and Scholarships
""")

    # 2. interdisciplinary-early-childhood-education-bs-526.md
    with open("programs/undergraduate/interdisciplinary-early-childhood-education-bs-526.md", "w") as f:
        f.write("""---
title: "Interdisciplinary Early Childhood Education, Bachelor of Science (Ref: 526)"
type: "program"
tags: [undergraduate, iece, degree, early-childhood, birth-to-primary, bachelor-of-science]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/interdisciplinary-early-childhood-education-bs/"
last_updated: "2026-09-02"
summary: "Undergraduate degree program leading to Kentucky initial teaching certification in Interdisciplinary Early Childhood Education (Birth to Primary / Age 5)."
---

# Interdisciplinary Early Childhood Education, Bachelor of Science (Ref: 526)

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Bachelor of Science in Interdisciplinary Early Childhood Education (IECE) (Reference # 526)** prepares specialists to work with young children, both typically developing and those with disabilities or developmental delays, from **birth through primary (kindergarten / age 5)**, and their families. Graduates are qualified to teach in public school preschool and kindergarten classrooms, state early intervention programs (First Steps), Head Start, and inclusive community child care settings.

---

## Program Summary & Key Facts

| Feature | Specification |
| :--- | :--- |
| **Degree Awarded** | Bachelor of Science (B.S.) |
| **WKU Catalog Reference Number** | **526** |
| **Total Credit Hours Required** | **120 Hours** |
| **Kentucky Certification Issued** | Interdisciplinary Early Childhood Education, Birth to Primary (B-P) |
| **Delivery Mode** | On-Campus with extensive preschool and clinical field placements |
| **Accreditation** | CAEP Accredited; Approved by Kentucky EPSB; Aligned with NAEYC / DEC standards |
| **Primary Faculty Contact** | [[people/dr-trudy-little|Dr. Trudy M. Little, Ph.D., BCBA]] |
| **Academic Advisor** | [[people/meredith-stewart|Meredith Stewart]] (GRH 1005) |

---

## Core Philosophical Foundations

The IECE program is built on four core commitments:
1.  **Family-Centered Practice:** Partnering with parents and caregivers as the primary decision-makers in young children's development.
2.  **Inclusive Early Education:** Embedding developmental interventions and positive behavior supports within natural, play-based learning environments.
3.  **Interdisciplinary Collaboration:** Working alongside speech-language pathologists, occupational therapists, physical therapists, and pediatric medical specialists.
4.  **Individualized Planning:** Developing Individualized Family Service Plans (IFSPs) for infants/toddlers and Individualized Education Programs (IEPs) for preschoolers.

---

## Curriculum Requirements (120 Hours)

### 1. Colonnade General Education (39 Hours)
Foundational writing, communication, quantitative reasoning, social sciences (PSY 100 recommended), and natural sciences.

### 2. Early Childhood & Child Development Core (21 Hours)
*   **FACS 191:** Child Development (3 hrs)
*   **FACS 192:** Working with Young Children and Families (3 hrs)
*   **FACS 294:** Assessment of Young Children (3 hrs)
*   **FACS 297:** Family Relations (3 hrs)
*   **COMM 145:** Fundamentals of Public Speaking (3 hrs)
*   **PSY 310:** Educational Psychology: Development and Learning (3 hrs)
*   **SPED 330:** Introduction to Exceptional Education (3 hrs)

### 3. Professional IECE Education Sequence (51 Hours)
*   **IECE 321:** Family Partnerships in Early Childhood (3 hrs)
*   **IECE 322:** Infant/Toddler Curriculum and Assessment (3 hrs)
*   **IECE 323:** Preschool Curriculum and Methods (3 hrs)
*   **IECE 324:** Advanced Early Childhood Assessment and Intervention (3 hrs)
*   **IECE 325:** Creative Arts and Movement in Early Childhood (3 hrs)
*   **IECE 326:** Health, Safety, and Nutrition in Early Learning Settings (3 hrs)
*   **IECE 421:** Advanced Curriculum and Instruction in IECE (3 hrs)
*   **IECE 422:** Clinical Practicum in Infant/Toddler Settings (3 hrs)
*   **IECE 423:** Interdisciplinary Teaming in Early Intervention (3 hrs)
*   **IECE 489:** Student Teaching Seminar in IECE (3 hrs)
*   **IECE 490:** Student Teaching in Interdisciplinary Early Childhood (10 hrs)

---

## Clinical Placements & Partners
*   **Renshaw Early Childhood Center (Big Red School):** Located at the [[centers-and-partnerships/suzanne-vitale-clinical-education-complex|Suzanne Vitale CEC]], providing candidates with hands-on practice in an inclusive developmental preschool setting.
*   **First Steps (Kentucky Early Intervention System):** In-home and community clinical visits with credentialed early intervention specialists.
*   **Public School Preschools:** Placements in Warren County Public Schools and Bowling Green Independent Schools Title I preschool and Head Start classrooms.

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[people/dr-trudy-little]]: IECE Assistant Professor & Faculty Lead
*   [[centers-and-partnerships/suzanne-vitale-clinical-education-complex]]: Clinical Partner Site
*   [[programs/graduate/interdisciplinary-early-childhood-mat-0460]]: Graduate Initial Certification Route
*   [[programs/graduate/interdisciplinary-early-childhood-mae-0461]]: Advanced IECE Master's Degree
""")

    # 3. middle-level-education-bs-5001.md
    with open("programs/undergraduate/middle-level-education-bs-5001.md", "w") as f:
        f.write("""---
title: "Middle Level Education in Social Studies and Language Arts, Bachelor of Science (Ref: 5001)"
type: "program"
tags: [undergraduate, mged, middle-school, language-arts, social-studies, grades-5-9]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/middle-level-education-social-studies-language-arts-bs/"
last_updated: "2026-09-02"
summary: "Undergraduate degree preparing candidates for dual Kentucky teaching certification in Middle Grades (5-9) English/Language Arts and Social Studies."
---

# Middle Level Education in Social Studies and Language Arts, Bachelor of Science (Ref: 5001)

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Bachelor of Science in Middle Level Education in Social Studies and Language Arts (Reference # 5001)** prepares educators tailored specifically for the cognitive, emotional, and social needs of young adolescents in **grades 5 through 9**. Candidates complete dual disciplinary concentrations in English/Language Arts and Social Studies, graduating with dual teaching credentials.

---

## Program Summary & Key Facts

| Feature | Specification |
| :--- | :--- |
| **Degree Awarded** | Bachelor of Science (B.S.) |
| **WKU Catalog Reference Number** | **5001** |
| **Total Credit Hours Required** | **120–128 Hours** |
| **Kentucky Certification Issued** | Middle School (Grades 5–9): Dual Certification in English/Language Arts & Social Studies |
| **Accreditation** | CAEP Accredited; Kentucky EPSB Approved; Aligned with AMLE Standards |
| **Primary Faculty Contacts** | [[people/dr-erin-margarella|Dr. Erin Margarella]], [[people/dr-julia-mittelberg|Dr. Julia Mittelberg]] |
| **Academic Advisor** | [[people/meredith-stewart|Meredith Stewart]] (GRH 1005) |

---

## Dual Content Concentration Requirements

### 1. Middle Grades English / Language Arts Concentration (24 Hours)
*   **ENG 100:** Introduction to College Writing (3 hrs)
*   **ENG 200:** Introduction to Literature (3 hrs)
*   **ENG 300:** Writing in the Disciplines (3 hrs)
*   **ENG 302:** Language and Communication (3 hrs)
*   **ENG 391:** Survey of American Literature I or II (3 hrs)
*   **ENG 392:** Survey of British Literature (3 hrs)
*   **LTCY 421:** Literacy in the Content Areas (3 hrs)
*   **Young Adult Literature Requirement:** (ENG 381 or equivalent) (3 hrs)

### 2. Middle Grades Social Studies Concentration (24 Hours)
*   **HIST 101 or 102:** World History I or II (3 hrs)
*   **HIST 240:** United States History to 1865 (3 hrs)
*   **HIST 241:** United States History since 1865 (3 hrs)
*   **GEOG 110:** World Regional Geography (3 hrs)
*   **PS 110:** American National Government (3 hrs)
*   **ECON 150 or 202:** Introduction to Economics / Principles of Microeconomics (3 hrs)
*   **Upper-Division History Elective:** (Kentucky History HIST 310 recommended) (3 hrs)
*   **Social Sciences Elective:** (Sociology, Anthropology, or Political Science) (3 hrs)

---

## Professional Middle Education Sequence (43 Hours)
*   **EDU 250:** Introduction to Teacher Education (3 hrs)
*   **PSY 310:** Educational Psychology: Development and Learning (3 hrs)
*   **SPED 330:** Introduction to Exceptional Education (3 hrs)
*   **MGE 275:** Foundations of Middle Level Education (3 hrs)
*   **MGE 385:** Middle Grades Teaching Strategies (3 hrs)
*   **MGE 475:** Teaching Language Arts in Middle Grades (3 hrs)
*   **MGE 481:** Teaching Social Studies in Middle Grades (3 hrs)
*   **LTCY 421:** Literacy in Middle and Secondary Grades (3 hrs)
*   **EDU 489:** Student Teaching Seminar (3 hrs)
*   **MGE 490:** Student Teaching - Middle Grades (10 hrs)

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[people/dr-erin-margarella]]: Associate Professor of Middle & Secondary English
*   [[people/dr-julia-mittelberg]]: Associate Professor of Middle & Secondary Social Studies
*   [[pathways-and-certification/become-a-teacher]]: Prospective Teacher Portal
*   [[pathways-and-certification/admission-to-teacher-education]]: Admission Criteria
""")

    # 4. science-and-mathematics-education-bs-774.md
    with open("programs/undergraduate/science-and-mathematics-education-bs-774.md", "w") as f:
        f.write("""---
title: "Science and Mathematics Education (SMED / SKyTeach), Bachelor of Science (Ref: 774)"
type: "program"
tags: [undergraduate, smed, skyteach, stem, math-education, science-education, uteach, secondary]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/science-mathematics-education-bs/"
last_updated: "2026-09-02"
summary: "Undergraduate STEM teacher preparation program based on the national UTeach model, preparing secondary (8-12) math and science teachers."
---

# Science and Mathematics Education (SMED / SKyTeach), Bachelor of Science (Ref: 774)

*School of Teacher Education (CEBS) & Ogden College of Science and Engineering*  
*Western Kentucky University*

The **Bachelor of Science in Science and Mathematics Education (Reference # 774)**, known universally as **SKyTeach**, is an innovative STEM educator preparation initiative replicated from the nationally acclaimed **UTeach** model at the University of Texas at Austin.

Candidates in SKyTeach earn a double major: a full disciplinary major in a STEM field (Mathematics, Biology, Chemistry, Physics, or Earth/Space Science) through the Ogden College of Science and Engineering, paired with the SMED major through the School of Teacher Education.

---

## Program Summary & Key Facts

| Feature | Specification |
| :--- | :--- |
| **Degree Awarded** | Bachelor of Science (B.S.) |
| **WKU Catalog Reference Number** | **774** |
| **Total Credit Hours Required** | **34–37 Professional Education Hours** (Paired with 45–60 STEM Content Hours) |
| **Kentucky Certification Issued** | Secondary Mathematics, Biology, Chemistry, Physics, or Earth/Space Science (Grades 8–12) |
| **Accreditation** | CAEP Accredited; Kentucky EPSB Approved; National UTeach Network Affiliate |
| **Education Co-Director** | [[people/dr-martha-day|Dr. Martha M. Day, Ed.D.]] (KTH 1011C) |
| **Master Teachers** | [[people/melanie-owens|Melanie Owens]], [[people/emily-perkins|Emily Perkins]], [[people/mr-rico-tyler|Rico Tyler]] |

---

## The SKyTeach Difference

*   **Try Teaching Early (Tuition-Reimbursed):** Freshmen and sophomores enroll in **SMED 101** (Step 1) and **SMED 102** (Step 2), planning and teaching inquiry lessons in real elementary and middle school classrooms. Tuition for Step 1 is frequently reimbursed upon course completion.
*   **Inquiry-Based Pedagogy (5E Model):** Focus on inquiry-based learning, student investigation, hands-on laboratory modeling, and the BSCS 5E Instructional Model (Engage, Explore, Explain, Elaborate, Evaluate).
*   **Instruction by Master Teachers:** Clinical courses are taught by dedicated, veteran public school math and science teachers stationed in Kelly Thompson Hall (KTH 1011).

---

## SMED Professional Education Coursework (34–37 Hours)

*   **SMED 101:** Step 1: Inquiry Approaches to Teaching (1 hr) *(Elementary school clinical visits)*
*   **SMED 102:** Step 2: Inquiry-Based Lesson Design (2 hrs) *(Middle school clinical visits)*
*   **SMED 310:** Knowing and Learning in Mathematics and Science (3 hrs)
*   **SMED 320:** Classroom Interactions in Mathematics and Science (3 hrs)
*   **SMED 340:** Perspectives on Science and Mathematics (3 hrs)
*   **SMED 360:** Research Methods in Science and Mathematics (3 hrs)
*   **SMED 470:** Project-Based Instruction in Mathematics and Science (3 hrs)
*   **SPED 330:** Introduction to Exceptional Education (3 hrs)
*   **LTCY 421:** Literacy in the Content Areas (3 hrs)
*   **SMED 489:** Student Teaching Seminar (3 hrs)
*   **SEC 490:** Student Teaching in Secondary Education (10 hrs)

---

## Approved Content Majors (Ogden College)
*   **Mathematics (B.S.):** Ref # 728
*   **Biology (B.S.):** Ref # 617
*   **Chemistry (B.S.):** Ref # 623
*   **Physics (B.S.):** Ref # 754
*   **Geology / Earth Science (B.S.):** Ref # 577

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[centers-and-partnerships/skyteach-stem-program]]: SKyTeach Program History & Facilities
*   [[people/dr-martha-day]]: SKyTeach Education Co-Director
*   [[people/melanie-owens]]: SKyTeach Mathematics Master Teacher
*   [[people/emily-perkins]]: SKyTeach Science Master Teacher
*   [[people/mr-rico-tyler]]: SKyTeach Physics Master Teacher
""")

    # 5. special-education-and-elementary-education-bs-5003.md
    with open("programs/undergraduate/special-education-and-elementary-education-bs-5003.md", "w") as f:
        f.write("""---
title: "Special Education & Elementary Education Dual Certification, Bachelor of Science (Ref: 5003)"
type: "program"
tags: [undergraduate, sped, eled, dual-certification, lbd, learning-behavior-disorders, bachelor-of-science]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/special-education-learning-behavior-disorders-elementary-bs/"
last_updated: "2026-09-02"
summary: "High-demand 128-credit hour undergraduate dual certification degree in Elementary Education (P-5) and Special Education: LBD (P-12)."
---

# Special Education & Elementary Education Dual Certification, Bachelor of Science (Ref: 5003)

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Bachelor of Science in Special Education: Learning and Behavior Disorders and Elementary Education (Reference # 5003)** is one of the most versatile and marketable education degrees in the Commonwealth of Kentucky. Candidates complete requirements for **two distinct teaching licenses**:
1.  **Elementary Education (Grades P–5)**
2.  **Special Education: Learning and Behavior Disorders (LBD) (Grades P–12)**

---

## Program Summary & Key Facts

| Feature | Specification |
| :--- | :--- |
| **Degree Awarded** | Bachelor of Science (B.S.) |
| **WKU Catalog Reference Number** | **5003** |
| **Total Credit Hours Required** | **128 Hours** |
| **Kentucky Certifications Issued** | 1) Elementary Education (P–5) & 2) Special Education: LBD (P–12) |
| **Job Market Demand** | Extremely high; SPED and dual-certified teachers are in critical shortage across Kentucky |
| **Accreditation** | CAEP Accredited; Kentucky EPSB Approved; Council for Exceptional Children (CEC) aligned |
| **Primary Faculty Contacts** | [[people/dr-christina-noel|Dr. Christina R. Noel]], [[people/dr-ellen-casale|Dr. Ellen G. Casale]], [[people/dr-shannon-pardue|Dr. Shannon Pardue]], [[people/dr-brooke-royalty|Dr. Brooke Royalty]] |
| **Academic Advisor** | [[people/meredith-stewart|Meredith Stewart]] (GRH 1005) |

---

## Curriculum Structure (128 Hours)

### 1. Colonnade General Education (39 Hours)
General education foundations including quantitative reasoning (MATH 116), writing, communication, and natural sciences.

### 2. Elementary Content Courses (18 Hours)
*   **MATH 205:** Number Systems and Number Theory for Elementary Teachers (3 hrs)
*   **MATH 206:** Fundamentals of Geometry for Elementary Teachers (3 hrs)
*   **MATH 308:** Rational Numbers & Data for Elementary Teachers (3 hrs)
*   **GEOG 110:** World Regional Geography (3 hrs)
*   **HIST 240 or 241:** United States History (3 hrs)
*   **Biological / Physical Science Content Elective:** (3 hrs)

### 3. Professional Education Core (71 Hours)

#### Foundations Block
*   **EDU 250:** Introduction to Teacher Education (3 hrs)
*   **PSY 310:** Educational Psychology: Development and Learning (3 hrs)
*   **LTCY 320:** Foundations of Literacy Instruction (3 hrs)

#### Elementary Methods Block
*   **ELED 345:** Foundations of Elementary Educational Practice (3 hrs)
*   **ELED 355:** Student Diversity in the Elementary Classroom (3 hrs)
*   **ELED 365:** Teaching Science in Elementary Schools (3 hrs)
*   **ELED 405:** Teaching Mathematics in Elementary Schools (3 hrs)
*   **ELED 406:** Teaching Social Studies in Elementary Schools (3 hrs)
*   **LTCY 420:** Reading in the Primary Grades (3 hrs)

#### Special Education (LBD) Block
*   **SPED 330:** Introduction to Exceptional Education: Diversity in Learning (3 hrs)
*   **SPED 335:** Foundations of Special Education: Legal, Ethical, and Historical (3 hrs)
*   **SPED 340:** Classroom and Behavior Management in Special Education (3 hrs)
*   **SPED 345:** Assessment and Program Planning in Special Education (3 hrs)
*   **SPED 424:** Inclusion, Collaboration, and Co-Teaching in P-12 Settings (3 hrs)
*   **SPED 480:** Instructional Methods for Students with Learning and Behavior Disorders (3 hrs)

#### Clinical Capstone & Student Teaching
*   **EDU 489:** Student Teaching Seminar (3 hrs)
*   **ELED 490:** Student Teaching in Elementary Education (5 hrs)
*   **SPED 490:** Student Teaching in Special Education: LBD (5 hrs)  
    *(Split clinical student teaching: 8 weeks in a general elementary classroom and 8 weeks in an LBD resource/collaborative setting).*

---

## Career Outcomes & Market Value
Dual-certified graduates possess distinct competitive advantages in hiring. School districts frequently prioritize dual-certified educators because they can transition flexibly between general education classrooms, co-taught inclusive settings, and special education resource rooms.

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[programs/undergraduate/elementary-education-bs-527]]: Standalone Elementary Major
*   [[people/dr-christina-noel]]: Professor of Special Education & Director, CEC
*   [[people/dr-ellen-casale]]: Assistant Professor of Special Education & BCBA
*   [[centers-and-partnerships/suzanne-vitale-clinical-education-complex]]: Clinical Partner
*   [[funding-and-aid/teacher-funding-guide]]: Funding and High-Need Grants
""")

    # 6. secondary-education-certification.md
    with open("programs/undergraduate/secondary-education-certification.md", "w") as f:
        f.write("""---
title: "Secondary Education Teacher Certification (Grades 8-12 & P-12)"
type: "program"
tags: [undergraduate, secondary-education, high-school, grades-8-12, teacher-certification]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/"
last_updated: "2026-09-02"
summary: "Teacher certification pathways for secondary education (Grades 8-12) and P-12 specialty areas paired with content majors across WKU colleges."
---

# Secondary Education Teacher Certification (Grades 8-12 & P-12)

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

At Western Kentucky University, undergraduate candidates preparing to teach at the high school level (**Grades 8 through 12**) or in comprehensive specialty subjects (**Grades P through 12**) complete an academic major in their teaching discipline paired with the Professional Secondary Education sequence in the School of Teacher Education.

---

## Certified Subject Areas & Partner Colleges

### 1. High School Grades 8–12 Certification
*   **English for Secondary Teachers (B.A.):** Potter College of Arts and Letters (PCAL)
*   **Social Studies / History for Secondary Teachers (B.A.):** PCAL
*   **Mathematics (B.S.):** Ogden College of Science & Engineering (via [[programs/undergraduate/science-and-mathematics-education-bs-774|SKyTeach]])
*   **Biology (B.S.):** Ogden College (via [[programs/undergraduate/science-and-mathematics-education-bs-774|SKyTeach]])
*   **Chemistry (B.S.):** Ogden College (via [[programs/undergraduate/science-and-mathematics-education-bs-774|SKyTeach]])
*   **Physics (B.S.):** Ogden College (via [[programs/undergraduate/science-and-mathematics-education-bs-774|SKyTeach]])
*   **Earth and Space Science / Geology (B.S.):** Ogden College (via [[programs/undergraduate/science-and-mathematics-education-bs-774|SKyTeach]])
*   **Agriculture Education (B.S.):** Ogden College (Grades 5–12)

### 2. Comprehensive P–12 Certification
*   **Visual Art (B.F.A. / B.A. in Art Education):** PCAL
*   **Music Education (B.M. - Instrumental or Vocal):** PCAL
*   **Physical Education & Health (B.S.):** College of Health and Human Services (CHHS)
*   **Spanish / Modern Languages (B.A.):** PCAL

---

## Secondary Professional Education Sequence (34–37 Hours)

Candidates in non-SKyTeach secondary tracks (such as English, Social Studies, Art, Music) complete the following pedagogical core:
*   **EDU 250:** Introduction to Teacher Education (3 hrs)
*   **PSY 310:** Educational Psychology: Development and Learning (3 hrs)
*   **SPED 330:** Introduction to Exceptional Education (3 hrs)
*   **SEC 351:** Teaching Strategies for Secondary Schools (3 hrs)
*   **SEC 352:** Planning for Student Diversity in Secondary Classrooms (3 hrs)
*   **LTCY 421:** Literacy in the Content Areas (3 hrs)
*   **Discipline-Specific Methods Course:** (e.g., ENG 476, HIST 490, ART 411, MUS 412) (3 hrs)
*   **SEC 453:** Senior Projects in Secondary Education (3 hrs)
*   **EDU 489:** Student Teaching Seminar (3 hrs)
*   **SEC 490:** Student Teaching in Secondary Schools (10 hrs)

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[programs/undergraduate/science-and-mathematics-education-bs-774]]: STEM Secondary Track (SKyTeach)
*   [[people/dr-erin-margarella]]: Secondary English Lead
*   [[people/dr-julia-mittelberg]]: Secondary Social Studies Lead
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Student Teaching Details
""")

    # 7. interactive-training-and-leadership-certificate-1752.md
    with open("programs/undergraduate/interactive-training-and-leadership-certificate-1752.md", "w") as f:
        f.write("""---
title: "Interactive Training and Leadership, Certificate (Ref: 1752)"
type: "certificate"
tags: [undergraduate, certificate, interactive-training, instructional-technology, leadership]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/interactive-training-design-certificate/"
last_updated: "2026-09-02"
summary: "12-credit hour undergraduate certificate in interactive workplace training, digital instructional design, and educational technology leadership."
---

# Interactive Training and Leadership, Certificate (Ref: 1752)

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Undergraduate Certificate in Interactive Training and Leadership (Reference # 1752)** is a 12-credit hour credential designed for undergraduate students interested in learning design, corporate training, educational technology, and organizational leadership.

---

## Program Summary & Key Facts

| Feature | Specification |
| :--- | :--- |
| **Credential Awarded** | Undergraduate Certificate |
| **WKU Catalog Reference Number** | **1752** |
| **Total Credit Hours Required** | **12 Hours** |
| **Target Audience** | Education, business, communications, and health sciences majors seeking training credentials |
| **Format** | Available online and hybrid |
| **Primary Department** | School of Teacher Education |

---

## Curriculum (12 Hours)

*   **ID 201:** Foundations of Instructional Design and Learning Technology (3 hrs)
*   **ID 301:** Interactive Multimedia Authoring and Simulation (3 hrs)
*   **ID 310:** Workplace Learning, Performance Improvement, and Needs Assessment (3 hrs)
*   **LEAD 200 or LEAD 300:** Elements of Leadership / Leadership Theory and Practice (3 hrs)

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Master Program Matrix
*   [[programs/graduate/instructional-design-ms-0428]]: Graduate MS in Instructional Design
*   [[programs/certificates-and-endorsements/instructional-design-certificate-0418]]: Graduate Certificate
""")

    print("Undergraduate program files generated successfully.")

if __name__ == "__main__":
    generate_ug_programs()
