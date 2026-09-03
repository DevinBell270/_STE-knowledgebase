import os

def generate_curriculum():
    print("Generating courses and curriculum files...")

    # 1. course-prefixes-and-descriptions.md
    with open("courses-and-curriculum/course-prefixes-and-descriptions.md", "w") as f:
        f.write("""---
title: "STE Course Prefixes & Catalog Curriculum Guide"
type: "curriculum"
tags: [curriculum, courses, course-prefixes, catalog, edu, eled, iece, lite, ltcy, mge, sec, smed, sped, tchl]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/"
last_updated: "2026-09-02"
summary: "Comprehensive catalog reference guide detailing all departmental course prefixes, levels, and core sequences administered by the WKU School of Teacher Education."
---

# STE Course Prefixes & Catalog Curriculum Guide

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The School of Teacher Education administers an extensive catalog of undergraduate, post-baccalaureate, and graduate courses across 13 distinct academic prefixes. This guide provides a functional breakdown of each prefix and key curricular sequences.

---

## Master Table of Academic Course Prefixes

| Course Prefix | Full Subject Area | Level | Primary Academic Focus |
| :--- | :--- | :--- | :--- |
| **EDU** | Education (Foundations & Clinicals) | Undergrad & Grad | Introductory teaching foundations (EDU 250), instructional planning (EDU 520), and student teaching seminars (EDU 489, 589). |
| **ELED** | Elementary Education | Undergrad & Grad | Elementary pedagogy, methods of science (ELED 365), math (ELED 405), social studies (ELED 406), and elementary student teaching (ELED 490). |
| **IECE** | Interdisciplinary Early Childhood Ed | Undergrad & Grad | Infant/toddler development, family partnerships, early intervention, and preschool teaching methods (Birth through Primary). |
| **LITE** | Libraries, Informatics, and Technology | Undergrad & Grad | Digital literacy, educational technology, library media center administration, and emerging AI tools in education. |
| **LTCY** | Literacy Education | Undergrad & Grad | Foundational reading, phonics, content-area reading (LTCY 421), diagnostic assessments (LTCY 523), and clinical reading practicums. |
| **MGE** | Middle Grades Education | Undergrad & Grad | Young adolescent psychology, middle school curriculum, English/Language Arts methods (MGE 475), and social studies methods (MGE 481). |
| **SEC** | Secondary Education | Undergrad & Grad | High school teaching strategies (SEC 351), student diversity (SEC 352), secondary senior projects (SEC 453), and secondary student teaching (SEC 490). |
| **SMED** | Science and Mathematics Education | Undergraduate | The SKyTeach inquiry sequence (Step 1 SMED 101, Step 2 SMED 102, Knowing & Learning SMED 310, Project-Based Instruction SMED 470). |
| **SPED** | Special Education | Undergrad & Grad | Exceptional child foundations (SPED 330/516), behavior management (SPED 340/530), assessment (SPED 345/531), and LBD/MSD methods. |
| **TCHL** | Teacher Leadership | Graduate | Core master's sequence in teacher leadership, curriculum development, student assessment, and action research capstones (TCHL 500, 530, 555, 560). |
| **ID** | Instructional Design | Undergrad & Grad | Workplace performance improvement, multimedia learning design, e-learning authoring tools, and project management (ID 560, 570, 575). |
| **GTE** | Gifted and Talented Education | Graduate | Identification of high-ability learners, curriculum differentiation, creativity development, and gifted practicum (GTE 536, 537, 538, 539). |
| **ABA** | Applied Behavior Analysis | Graduate | Behavior principles, single-case design, behavioral assessment, ethics, and BCBA clinical supervision (ABA 501–590). |

---

## Core Undergraduate Pedagogical Sequences

### The Professional Education Core (Undergraduate)
All initial certification undergraduate majors (ELED, Middle, Secondary, Dual SPED) complete a shared foundational sequence before advancing to discipline-specific methods:
1.  **EDU 250:** Introduction to Teacher Education (3 hrs) *(Field observation prerequisite)*
2.  **PSY 310:** Educational Psychology: Development and Learning (3 hrs)
3.  **SPED 330:** Introduction to Exceptional Education: Diversity in Learning (3 hrs)
4.  **LTCY 320 or 421:** Foundations of Literacy Instruction or Literacy in Content Areas (3 hrs)
5.  **Senior Capstone & Student Teaching:** EDU 489 (Seminar, 3 hrs) + ELED/MGE/SEC/SPED 490 (Student Teaching, 10 hrs).

---

## Backlinks / Related Documents
*   [[programs/INDEX]]: Academic Programs Directory
*   [[courses-and-curriculum/teacher-leader-core-curriculum]]: Detailed TCHL Sequence
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Clinical Placement Requirements
""")

    # 2. teacher-leader-core-curriculum.md
    with open("courses-and-curriculum/teacher-leader-core-curriculum.md", "w") as f:
        f.write("""---
title: "Teacher Leader Framework & Core Graduate Curriculum"
type: "curriculum"
tags: [tchl, teacher-leader, action-research, graduate-core, curriculum, assessment]
source_url: "https://catalog.wku.edu/graduate/education-behavioral-sciences/teacher-education/"
last_updated: "2026-09-02"
summary: "Detailed overview of the Teacher Leader (TCHL) core curriculum, classroom action research capstone, and school improvement models in WKU graduate degrees."
---

# Teacher Leader Framework & Core Graduate Curriculum

*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Teacher Leader Framework** at WKU is designed around the belief that the classroom teacher is the most critical agent of instructional innovation and school transformation. Rather than training teachers to leave the classroom for administrative offices, the Teacher Leader curriculum empowers educators to lead from the classroom, driving instructional coaching, peer mentoring, professional learning communities (PLCs), and data-driven school reform.

---

## The Teacher Leader Core (TCHL) Sequence

Graduate candidates in the [[programs/graduate/advanced-teacher-education-mae-0500|MAE in Advanced Teacher Education (Ref # 0500)]] and specialized MAE programs complete coursework across key leadership domains:

### 1. TCHL 500: Foundations of Teacher Leadership (3 Hours)
*   **Focus:** Exploring the Teacher Leader Model Standards, professional ethics, school culture, adult learning theory, and effective peer collaboration.
*   **Key Deliverable:** Comprehensive teacher leadership self-assessment and school climate improvement proposal.

### 2. TCHL 530: Curriculum Development and Evaluation (3 Hours)
*   **Focus:** Examining national and state curriculum standards, backward design (UbD), curriculum mapping, and evaluating instructional materials for cultural and cognitive responsiveness.

### 3. TCHL 555: School and Classroom Assessment Strategies (3 Hours)
*   **Focus:** Formative and summative assessment systems, standard-based grading, performance assessments, item analysis, and using school-wide assessment data to guide multi-tiered interventions.

### 4. TCHL 560 / EDU 595: Action Research Capstone for Teacher Leaders (3 Hours)
*   **Focus:** Conducting an applied, empirical action research study directly within the candidate's own P-12 classroom or school setting.
*   **Methodology:** Identifying an instructional problem of practice, implementing an evidence-based intervention, collecting quantitative/qualitative student learning data, analyzing outcome metrics, and publishing a formal action research capstone paper.

---

## Career Value & Endorsement
Graduates completing the Teacher Leader core satisfy state competencies for the **Kentucky Teacher Leader Endorsement (KTLE)**, qualifying them for elevated roles as department heads, instructional coaches, curriculum specialists, and district mentor teachers.

---

## Backlinks / Related Documents
*   [[programs/graduate/advanced-teacher-education-mae-0500]]: Flagship 30-Hour Stackable MAE
*   [[courses-and-curriculum/course-prefixes-and-descriptions]]: Master Prefix Table
*   [[pathways-and-certification/rank-change-system]]: Kentucky Rank Change System
""")

    # 3. courses-and-curriculum/INDEX.md
    with open("courses-and-curriculum/INDEX.md", "w") as f:
        f.write("""---
title: "Courses and Curriculum Map of Content"
type: "index"
tags: [curriculum, courses, prefixes, index, teacher-leader]
source_url: "https://catalog.wku.edu/undergraduate/education-behavioral-sciences/teacher-education/"
last_updated: "2026-09-02"
summary: "Map of Content (MOC) for School of Teacher Education course prefixes, catalog descriptions, and the Teacher Leader curriculum framework."
---

# Courses and Curriculum Map of Content

This hub indexes academic course structures, departmental prefixes, and core curricular frameworks in the School of Teacher Education.

---

## Curriculum Documents

*   [[courses-and-curriculum/course-prefixes-and-descriptions|STE Course Prefixes & Catalog Curriculum Guide]]
    *   Comprehensive breakdown of all 13 departmental prefixes (EDU, ELED, IECE, LITE, LTCY, MGE, SEC, SMED, SPED, TCHL, ID, GTE, ABA) and undergraduate pedagogical cores.
*   [[courses-and-curriculum/teacher-leader-core-curriculum|Teacher Leader Framework & Core Graduate Curriculum]]
    *   In-depth analysis of the graduate Teacher Leader core sequence (TCHL 500, 530, 555, 560), action research capstones, and school improvement models.

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Master Index
*   [[programs/INDEX]]: Academic Programs Directory
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Clinical Placement Guidelines
""")

    print("Curriculum files generated successfully.")

if __name__ == "__main__":
    generate_curriculum()
