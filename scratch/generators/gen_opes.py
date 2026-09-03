import os

def generate_opes():
    print("Generating OPES module and staff files...")
    os.makedirs("opes", exist_ok=True)

    # 1. opes/overview-and-staff.md
    with open("opes/overview-and-staff.md", "w") as f:
        f.write("""---
title: "Office of Professional Educator Services (OPES) Overview & Staff Directory"
type: "overview"
tags: [opes, professional-educator-services, support-unit, staff, ransdell-hall, admissions, certification]
source_url: "https://www.wku.edu/educatorservices/index.php"
last_updated: "2026-09-02"
summary: "Authoritative profile of OPES as the central operational supporting unit for the School of Teacher Education and CEBS, housing admissions, clinical placements, and certification."
---

# Office of Professional Educator Services (OPES) Overview & Staff Directory

*College of Education and Behavioral Sciences*  
*Western Kentucky University*  
*Physical Location: Gary A. Ransdell Hall (GRH), Suite 1092*

The **Office of Professional Educator Services (OPES)** serves as the central administrative and operational supporting unit for the **School of Teacher Education (STE)** and all initial and advanced Educator Preparation Programs (EPP) across Western Kentucky University. 

Operating under the College of Education and Behavioral Sciences (CEBS), OPES manages candidate progression through the entire educator pipeline: formal admission to teacher education, pre-service clinical field experiences, student teaching placements, Kentucky state certification recommendations, and alternative certification pathways.

---

## Core Administrative Responsibilities

```text
┌────────────────────────────────────────────────────────────────────────┐
│               Office of Professional Educator Services (OPES)          │
│                      Gary A. Ransdell Hall, Suite 1092                 │
├───────────────────┬───────────────────┬────────────────────────────────┤
│ 1. Admissions     │ 2. Clinicals      │ 3. Certification & Alternatives│
│ • Unit Orientations│ • 200 Field Hours │ • EPSB CA-1 Application Recs   │
│ • Praxis CASE / ACT│ • KEC/KFETS Logs  │ • Statement of Eligibility     │
│ • Clearances & CAN│ • Student Teaching│ • Rank Change Processing       │
│ • GPA 2.75 Audit  │ • Co-Teaching PD  │ • 16 KAR 5:030 Proficiency Eval│
└───────────────────┴───────────────────┴────────────────────────────────┘
```

1.  **Teacher Education Admissions:** Processing admissions applications for undergraduate and graduate candidates, monitoring GPA/testing thresholds, conducting mandatory orientation sessions, and verifying criminal background/CAN clearances.
2.  **Field Experiences:** Facilitating and monitoring the **200 clock hours** of pre-service clinical fieldwork required by the Kentucky Education Professional Standards Board (EPSB) under 16 KAR 5:040.
3.  **Student Teaching Operations:** Administering the capstone 70-day student teaching semester via Watermark Student Learning & Licensure (SL&L), coordinating placements across partner school districts, and training mentor cooperating teachers.
4.  **State Teacher Certification:** Recommending graduates to the Kentucky EPSB / Office of Educator Licensure and Effectiveness (OELE) for the Statement of Eligibility (SOE), processing Rank II/I salary changes, and completing out-of-state verification audits.
5.  **Alternative Certification & Proficiency Evaluations:** Administering the Kentucky Proficiency Evaluation pathway under **16 KAR 5:030**, providing portfolio-based evaluations for initial, additional, and administrative certification.

---

## Staff Directory & Contact Directory

| Staff Member | Title & Primary Role | Office Location | Telephone | Email |
| :--- | :--- | :--- | :--- | :--- |
| **[[people/mrs-sarah-fischer\|Mrs. Sarah Fischer]]** | **Assistant Director, OPES**<br>Oversees admissions, state certification reporting, and cooperating teacher training. | Gary A. Ransdell Hall 1097 | [(270) 745-3293](tel:12707453293) | [sarah.fischer@wku.edu](mailto:sarah.fischer@wku.edu) |
| **[[people/shannon-evans\|Shannon Evans]]** | **Program Manager, Clinical Experiences**<br>Manages student teaching applications, placement preferences, district coordination. | Gary A. Ransdell Hall 1096 | [(270) 745-3293](tel:12707453293) | [shannon.evans@wku.edu](mailto:shannon.evans@wku.edu) |
| **Lucas Green** | **Watermark SL&L System Administrator**<br>Technical assistance and user account support for Student Learning & Licensure. | Gary A. Ransdell Hall 1092 | [(270) 745-4897](tel:12707454897) | [lucas.green@wku.edu](mailto:lucas.green@wku.edu) |

---

## Suite Contact Card
*   **Physical Office:** Gary A. Ransdell Hall, Suite 1092
*   **Mailing Address:** 1906 College Heights Blvd. #11030, Bowling Green, KY 42101-1030
*   **Main Telephone:** [(270) 745-4897](tel:12707454897) | Admissions & Certification Line: [(270) 745-3293](tel:12707453293)
*   **Admissions Inquiries:** [teacher.services@wku.edu](mailto:teacher.services@wku.edu)
*   **Official Website:** [https://www.wku.edu/educatorservices/](https://www.wku.edu/educatorservices/)

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Index & Map of Content
*   [[opes/INDEX]]: OPES Map of Content
*   [[overview/contact-and-facilities]]: Ransdell Hall Building Layout
*   [[overview/about-ste]]: STE Institutional Overview
*   [[people/mrs-sarah-fischer]]: Assistant Director Profile
*   [[people/shannon-evans]]: Program Manager Profile
*   [[opes/teacher-admissions]]: Admissions Procedures
*   [[opes/field-experience]]: 200-Hour Fieldwork Protocol
*   [[opes/student-teaching-procedures]]: Capstone Student Teaching
*   [[opes/teacher-certification-services]]: EPSB Recommendation Services
""")

    # 2. opes/teacher-admissions.md
    with open("opes/teacher-admissions.md", "w") as f:
        f.write("""---
title: "OPES Teacher Education Program Admissions Procedures"
type: "pathway"
tags: [admissions, opes, teacher-education, orientation, praxis-core, can-check, background-check, gpa-2-75]
source_url: "https://www.wku.edu/educatorservices/teacher_admissions/index.php"
last_updated: "2026-09-02"
summary: "Official admission requirements, mandatory orientation protocols, testing thresholds, and background clearance procedures for WKU Educator Preparation Programs."
---

# OPES Teacher Education Program Admissions Procedures

*Office of Professional Educator Services*  
*School of Teacher Education*  
*Western Kentucky University*

Formal admission into the **Professional Education Unit** at Western Kentucky University is a state-regulated prerequisite that candidates must achieve before enrolling in restricted upper-division methods courses or clinical student teaching. The Office of Professional Educator Services (OPES) in **GRH 1092** oversees this process.

---

## The 3-Step Admissions Framework

```text
Step 1: Mandatory Orientation  ──► Step 2: Background & Clearances ──► Step 3: Academic & Testing
(Audit in GRH / Regional Hub)     (Verified Credentials & CAN)         (2.75 GPA & Praxis/ACT)
```

---

### Step 1: Mandatory Professional Education Admissions Orientation
All undergraduate candidates in their first introductory education course (EDU 250, SMED 101/102, or IECE 214) and new transfer students pursuing teacher certification **must attend a mandatory orientation session**.

*   **Attendance Policy:** Attendance is recorded at every session and transmitted directly to course instructors. *There are no make-up orientation sessions during the semester; attendance is strictly required.*
*   **Campus Locations:**
    *   *Bowling Green Campus:* Conducted during the first two weeks of September and January in Gary A. Ransdell Hall (Room 1074 Auditorium or Room 2069).
    *   *Regional Campuses:* Conducted at WKU Elizabethtown (RPC #233), WKU Glasgow (Community Room #131), and WKU Owensboro (Badgett Conference Room #104).

---

### Step 2: Clearance Documentation Prior to Orientation
Candidates must complete and upload all compliance documentation into their digital **Anthology** portfolio account:

1.  **Kentucky Medical Examination & TB Risk Assessment:**
    *   Completed on the official *KY Department of Education Medical Examination of School Employee* form by a licensed healthcare provider.
    *   TB skin test (PPD) is only required if the clinical examination indicates positive risk factors.
2.  **Criminal Background Check:**
    *   Processed through the approved university vendor, **Verified Credentials Agency**. Must be clear of felony offenses.
3.  **Child Abuse & Neglect (CAN) Check:**
    *   Processed through the Kentucky Cabinet for Health and Family Services (CHFS) Central Registry.
4.  **Teacher Education ID Badge:**
    *   Required for entry into P-12 public school buildings during clinical observations.
    *   Candidates submit a professional headshot to [teacher.services@wku.edu](mailto:teacher.services@wku.edu); physical badges are issued by OPES in GRH 1092.

---

### Step 3: Academic Standing & State Testing Thresholds

Candidates must satisfy both minimum GPA standards and state-approved basic skills testing:

#### 1. Grade Point Average (GPA)
*   **Minimum Cumulative GPA:** **2.75 or higher** on all college-level coursework, **OR** a minimum **3.0 GPA on the last 30 credit hours** attempted.

#### 2. Basic Skills Testing (Praxis CORE or ACT)
Candidates may satisfy the testing benchmark through either the **Praxis Core Academic Skills for Educators (CORE)** exam series or ACT/SAT scores:

| Assessment Battery | Component / Subtest | ETS Test Code | Minimum Kentucky Passing Score |
| :--- | :--- | :--- | :--- |
| **Praxis CORE** | Core Academic Skills: **Reading** | **5713** | **150** |
| **Praxis CORE** | Core Academic Skills: **Writing** | **5723** | **158** |
| **Praxis CORE** | Core Academic Skills: **Mathematics** | **5733** | **144** |
| **ACT Alternative** | ACT Composite Score | N/A | **22 or higher** |

> [!IMPORTANT]
> **Score Reporting Codes:** When registering for Praxis exams through ETS, candidates MUST designate both **Western Kentucky University (Code #1901)** and the **Kentucky Education Professional Standards Board (Code #7283)** as free score recipients. Adding recipients after test administration incurs a $50 ETS surcharge.

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/overview-and-staff]]: OPES Suite GRH 1092
*   [[pathways-and-certification/admission-to-teacher-education]]: Academic Requirements Guide
*   [[opes/field-experience]]: Pre-Service Fieldwork Protocols
*   [[opes/praxis-exams-and-support]]: Praxis Testing Support
""")

    # 3. opes/field-experience.md
    with open("opes/field-experience.md", "w") as f:
        f.write("""---
title: "OPES Field Experience Requirements & Clinical Procedures"
type: "pathway"
tags: [field-experience, clinicals, 200-hours, 16-kar-5-040, kfets, kec, observation-protocols, opes]
source_url: "https://www.wku.edu/educatorservices/field_exp/index.php"
last_updated: "2026-09-02"
summary: "Comprehensive guide to Kentucky's 200-hour pre-service clinical field experience requirement under 16 KAR 5:040, KEC/KFETS hour tracking, and school visit protocols."
---

# OPES Field Experience Requirements & Clinical Procedures

*Office of Professional Educator Services*  
*Gary A. Ransdell Hall, Suite 1092*  
*Western Kentucky University*

Per Kentucky Administrative Regulation **16 KAR 5:040**, all teacher candidates enrolled in educator preparation programs leading to initial certification must complete a minimum of **200 verified clock hours of diverse clinical field experiences** prior to the student teaching capstone semester.

The Office of Professional Educator Services (OPES) coordinates, monitors, and verifies all clinical placements across partner school districts.

---

## State Fieldwork Categories under 16 KAR 5:040

The 200 hours cannot simply be completed in a single classroom; candidates must document engagement across state-mandated clinical domains:

```text
┌────────────────────────────────────────────────────────────────────────┐
│               Kentucky 200-Hour Field Experience Categories             │
├────────────────────────────────────────────────────────────────────────┤
│ 1. Engagement with diverse student populations (SES, race, language)   │
│ 2. Observation in elementary, middle, and secondary school environments│
│ 3. Students with disabilities (IEPs, 504 plans, gifted & talented)     │
│ 4. School-based family resource centers (FRYSCs) and community hubs    │
│ 5. School board meetings and Site-Based Decision Making (SBDM) councils│
│ 6. Professional learning communities (PLCs) and faculty meetings       │
│ 7. Direct student tutoring and small group instructional delivery      │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Digital Hour Logging in KEC / KFETS

All field experience hours must be electronically logged and verified through the Kentucky Department of Education's **Kentucky Educator Credentialing (KEC)** system / **Kentucky Field Experience Tracking System (KFETS)**:

1.  **Account Registration:** Candidates establish a user profile on the [Kentucky Educator Credentialing (KEC) portal](https://kecs.education.ky.gov/).
2.  **Daily Activity Entries:** After each school visit, candidates enter the date, school name, district, cooperating teacher name, hours observed, and specific 16 KAR 5:040 category.
3.  **Instructor Verification:** STE course instructors audit and digitally approve candidate KFETS logs at the conclusion of each clinical course.
4.  **Final Clearance:** OPES conducts a cumulative audit of the 200-hour record prior to clearing candidates for student teaching.

---

## Seven Professional Guidelines for Visiting Partner Schools

When placed in a P-12 public school, WKU candidates represent the university and the profession. OPES mandates adherence to seven core standards:

1.  **Initial Contact Within 48 Hours:** Email the assigned cooperating teacher within 48 hours of receiving placement notification to introduce yourself, confirm policies, and establish check-in/check-out procedures.
2.  **One-Week Escalation Protocol:** If the cooperating teacher does not reply within one calendar week, notify the university course instructor and OPES immediately for placement support.
3.  **Establish Mutually Agreed Schedule:** Agree upon exact dates and times for classroom visits during the initial visit, prioritizing the school's instructional routine.
4.  **Flawless Punctuality & Communication:** Keep all appointments and arrive promptly. If an emergency requires rescheduling, notify the teacher via email in advance.
5.  **Express Professional Appreciation:** Send a formal thank-you letter or email to the cooperating teacher at the conclusion of the placement.
6.  **Confidential Problem Resolution:** Address instructional questions with course faculty. If challenges arise, consult the instructor or OPES Director confidentially, maintaining strict student confidentiality under FERPA.
7.  **Professional Appearance & Demeanor:** Adhere strictly to the school district's faculty dress code (business casual) and display the official **WKU Teacher Education ID Badge** at all times.

---

## Clinical Documentation & Forms
*   **Criminal Background Check:** Verified Credentials clearance uploaded to Anthology.
*   **KDE Physical & TB Risk Assessment:** Current medical report on file.
*   **Out-of-Area Placement Requests:** Candidates seeking placements outside WKU's regional service area must submit the electronic *Out of Area Request for Field Placement* form to OPES by specified semester deadlines.

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/student-teaching-procedures]]: 70-Day Capstone Semester
*   [[opes/co-teaching-model]]: Clinical Co-Teaching Philosophy
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Program Clinical Blueprint
*   [[people/shannon-evans]]: Clinical Placement Program Manager
""")

    # 4. opes/student-teaching-procedures.md
    with open("opes/student-teaching-procedures.md", "w") as f:
        f.write("""---
title: "OPES Student Teaching Procedures & Watermark SL&L Guide"
type: "pathway"
tags: [student-teaching, watermark, sll, clinical-semester, deadlines, 70-days, shannon-evans, lucas-green]
source_url: "https://www.wku.edu/educatorservices/student_teaching/index.php"
last_updated: "2026-09-02"
summary: "Official policies, Watermark SL&L application steps, 1-year advance deadlines, and eligibility criteria for the student teaching semester."
---

# OPES Student Teaching Procedures & Watermark SL&L Guide

*Office of Professional Educator Services*  
*Gary A. Ransdell Hall, Suite 1092*  
*Western Kentucky University*

Student teaching is the culminating, intensive 16-week (70 instructional days) clinical capstone experience for all initial teacher certification candidates at Western Kentucky University. Administered by the Office of Professional Educator Services (OPES), candidates transition full-time into public school classrooms under the daily mentorship of an experienced P-12 cooperating teacher and a university supervisor.

---

## 1-Year Advance Application Deadlines

Because arranging placements across dozens of regional school districts requires extensive administrative coordination and formal district vetting, **applications to student teach are due one full year in advance**:

| Student Teaching Term | Application Opens | Final Submission Deadline |
| :--- | :--- | :--- |
| **Fall Semester Student Teaching** | September 1 | **October 15th** (One year prior) |
| **Spring Semester Student Teaching** | February 1 | **April 15th** (One year prior) |

---

## Application Submission via Watermark Student Learning & Licensure (SL&L)

WKU utilizes the **Watermark Student Learning & Licensure (SL&L)** enterprise platform to manage candidate applications and clinical assessment evaluations:

### Step-by-Step Watermark Application Workflow:
1.  **Access Portal:** Navigate to the [WKU Watermark Portal](https://login.watermarkinsights.com/connect/westernkentuckyuniversity) and authenticate using your WKU NetID credentials.
2.  **Open Program Applications:** Select `Program Applications` from the left-hand navigation menu.
3.  **Start Application:** Click the `START AN APPLICATION` button.
4.  **Locate Semester Form:** Search for your target placement term (e.g., *Application to Student Teach Fall 2027* under Educator Preparation Programs).
5.  **Complete Fields:** Input personal details, certification major, district placement preferences, and transportation confirmations.
6.  **Submit for Audit:** Click `SUBMIT` (or `SAVE AS DRAFT` if returning later).
7.  **Confirm Status:** Verify that your application status displays as **`AWAITING REVIEW`** on the dashboard.

### Support Contacts for Student Teaching:
*   **Watermark Technical Support:** Lucas Green ([lucas.green@wku.edu](mailto:lucas.green@wku.edu))
*   **Application & Placement Inquiries:** [[people/shannon-evans|Shannon Evans]], Program Manager ([shannon.evans@wku.edu](mailto:shannon.evans@wku.edu))

---

## Student Teaching Eligibility Audit Checklist

Prior to entering the placement classroom, candidates must clear a rigorous compliance check:
1.  **Full Admission to Teacher Education:** Verified admission to the Professional Education Unit on TopNet.
2.  **Senior Academic Standing:** Conferred senior standing with completion of all general education and major content courses.
3.  **GPA Thresholds:** Minimum cumulative GPA of **2.75** (overall and in professional education coursework).
4.  **Field Experience Hours:** 100% completion of the **200 verified clock hours** logged in KEC/KFETS.
5.  **State Clearances:** Active criminal background check, child abuse & neglect (CAN) check, and medical physical/TB risk assessment.

---

## Key Student Teaching Documents & Resources
*   **Student Teaching Handbook Resource Site:** Google Site containing observation forms, tri-annual evaluation rubrics, and policy guides.
*   **WKU Co-Teaching Model:** Co-teaching training resources under [[opes/co-teaching-model|WKU Co-Teaching Model]].
*   **Tuition Waiver for Supervising Teachers:** Cooperating teachers in Kentucky qualify for tuition waivers administered through CEBS.

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/co-teaching-model]]: WKU Co-Teaching Framework
*   [[opes/field-experience]]: Pre-Service 200 Hours
*   [[people/shannon-evans]]: Placement Program Manager
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Clinical Semester Overview
""")

    # 5. opes/co-teaching-model.md
    with open("opes/co-teaching-model.md", "w") as f:
        f.write("""---
title: "WKU Co-Teaching Model & Cooperating Teacher Training"
type: "pathway"
tags: [co-teaching, cooperating-teachers, 16-kar-5-040, clinical-supervision, tuition-waiver, stobaugh, opes]
source_url: "https://www.wku.edu/educatorservices/co-teaching.php"
last_updated: "2026-09-02"
summary: "Detailed overview of WKU's co-teaching clinical framework, 16 KAR 5:040 cooperating teacher training requirements, and the 7 co-teaching instructional models."
---

# WKU Co-Teaching Model & Cooperating Teacher Training

*Office of Professional Educator Services*  
*School of Teacher Education*  
*Western Kentucky University*

Western Kentucky University employs a research-based **Co-Teaching Model** for all clinical student teaching experiences. Developed in collaboration with P-12 partner districts, co-teaching is defined as *two teachers (a mentor cooperating teacher and a teacher candidate) working together with groups of students, sharing the planning, organization, delivery, and assessment of instruction, as well as the physical space*.

Rather than relegating the student teacher to passive observation for weeks before a sudden solo takeover, co-teaching engages both educators in active instruction from **Day One**.

---

## State-Mandated Cooperating Teacher Training (16 KAR 5:040)

Per Kentucky Administrative Regulation **16 KAR 5:040**, veteran classroom educators who agree to mentor a WKU student teacher must complete a three-part training sequence prior to assuming supervisory duties:

```text
┌────────────────────────────────────────────────────────────────────────┐
│             Cooperating Teacher Training Sequence (16 KAR 5:040)       │
├────────────────────────────────────────────────────────────────────────┤
│ Part A: Basic Responsibilities Training (iDrive Digital Quiz)          │
│   • Administered via KDE Office of Educator Licensure & Effectiveness  │
│   • Covers legal statutes, role expectations, and ethical boundaries   │
├────────────────────────────────────────────────────────────────────────┤
│ Part B: Best Practice in Supporting a Student Teacher (Video Training) │
│   • Video modules detailing coaching conversations, feedback, & pacing │
│   • Confirmation sent to Assistant Director Sarah Fischer (GRH 1097)   │
├────────────────────────────────────────────────────────────────────────┤
│ Part C: Effective Assessment of the Student Teacher                    │
│   • Review of WKU Student Teaching Handbook, rubrics, & KTPS benchmarks│
└────────────────────────────────────────────────────────────────────────┘
```

> [!NOTE]
> **Cooperating Teacher Tuition Waiver:** Kentucky certified teachers who complete the supervision of a WKU student teacher earn a state-authorized **Tuition Waiver** (up to 6 graduate credit hours) usable for graduate coursework at WKU.

---

## The Seven Methods of Co-Teaching

Based on research and training developed by [[people/dr-rebecca-stobaugh|Dr. Rebecca R. Stobaugh]], Professor of Teacher Education at WKU, candidates and cooperating teachers implement seven strategic co-teaching variations:

| Co-Teaching Method | Description & Classroom Application |
| :--- | :--- |
| **1. One Teach, One Observe** | One teacher leads whole-group instruction while the other collects specific observational data on student engagement, understanding, or behavior. |
| **2. One Teach, One Assist** | One teacher delivers core content while the other circulates quietly to provide individual clarification, redirect attention, or assist struggling learners. |
| **3. Station Teaching** | Instructional content is divided into independent stations. Students rotate between teacher-led stations, independent practice, and digital learning pods. |
| **4. Parallel Teaching** | The class is divided in half. Both teachers teach the exact same lesson simultaneously to smaller cohorts, maximizing student response opportunities. |
| **5. Supplemental Teaching** | One teacher delivers grade-level instruction while the second teacher adapts, enriches, or reteaches the concept to a small targeted group. |
| **6. Alternative / Differentiated Teaching** | Teachers provide different learning approaches (e.g., visual/kinesthetic scaffolding or accelerated inquiry) to match diverse readiness tiers. |
| **7. Team Teaching** | Both educators actively share whole-group instruction simultaneously, modeling collaborative dialogue, debate, problem-solving, and role-play. |

---

## Phased Clinical Progression
Over the 16-week semester, leadership gradually shifts:
*   *Weeks 1–4:* Cooperating teacher leads ~70% of instruction; candidate co-plans and executes stations/assists (~30%).
*   *Weeks 5–8:* Shared lead responsibility (~50% / ~50%).
*   *Weeks 9–13:* Candidate assumes lead teacher role (~80%–100%), with cooperating teacher serving as co-teacher and evaluator.
*   *Weeks 14–16:* Candidate leads reflection, transition, and final evaluation debriefs.

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/student-teaching-procedures]]: Student Teaching Guide
*   [[people/dr-rebecca-stobaugh]]: Co-Teaching Curriculum Author
*   [[people/mrs-sarah-fischer]]: Training Verification Lead
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Fieldwork Framework
""")

    # 6. opes/teacher-certification-services.md
    with open("opes/teacher-certification-services.md", "w") as f:
        f.write("""---
title: "OPES Teacher Certification Services & EPSB Recommendations"
type: "pathway"
tags: [teacher-certification, ca-1, epsb, oele, rank-change, statement-of-eligibility, certification-officer, opes]
source_url: "https://www.wku.edu/educatorservices/teacher_cert/index.php"
last_updated: "2026-09-02"
summary: "Official guide to teacher certification recommendation, CA-1 application processing, Kentucky EPSB Statement of Eligibility, and Rank II/I advancement."
---

# OPES Teacher Certification Services & EPSB Recommendations

*Office of Professional Educator Services*  
*Gary A. Ransdell Hall, Suite 1092*  
*Western Kentucky University*

The Certification Personnel within the Office of Professional Educator Services (OPES) serve as Western Kentucky University's official liaison to the **Kentucky Education Professional Standards Board (EPSB)** and the Kentucky Department of Education's **Office of Educator Licensure and Effectiveness (OELE)**.

OPES processes all formal university recommendations for initial teacher certification, endorsements, non-degree planned rank changes (Rank II and Rank I), and out-of-state verification certificates.

---

## Core Certification Services Administered

```text
┌────────────────────────────────────────────────────────────────────────┐
│                  OPES Teacher Certification Services                   │
├────────────────────────────────────────────────────────────────────────┤
│ • Initial Certification Recommendations (Statement of Eligibility)    │
│ • CA-1 State Application Verification & Submission to EPSB/OELE        │
│ • Rank Change Advancement (Rank III ──► Rank II ──► Rank I)            │
│ • Addition of Endorsements (Gifted, ESL, Math Specialist, Literacy)   │
│ • Out-of-State Educator Verification (Verification of Program Forms)   │
│ • Temporary Provisional Licensure Processing (Option 6 & Proficiency)  │
└────────────────────────────────────────────────────────────────────────┘
```

---

## Kentucky Initial Certification: The CA-1 Application Process

Upon successful completion of an approved educator preparation program (undergraduate degree, MAT, or post-baccalaureate route) and student teaching, candidates apply for their Kentucky teaching license:

1.  **Kentucky Educator Credentialing System (KECS):**
    *   The candidate initiates their electronic **CA-1 Application** via the state [KECS Portal](https://kecs.education.ky.gov/).
2.  **University Audit & Recommendation:**
    *   OPES Certification Officers in GRH 1092 review the candidate's complete record: conferred degree transcript, completion of 200 field hours, successful student teaching evaluation, and passing scores on all required **Praxis Subject Assessments (Praxis II)** and the **Principles of Learning and Teaching (PLT)** exam.
3.  **Electronic Dean/Certification Officer Sign-Off:**
    *   OPES submits the official institutional recommendation directly to the EPSB Division of Certification.
4.  **Issuance of the Statement of Eligibility (SOE):**
    *   EPSB issues a **Statement of Eligibility (SOE)** valid for five years. When hired by a public school district, the SOE converts to a **Provisional Teaching Certificate** during the candidate's Kentucky Teacher Internship Program (KTIP) or mentoring induction year.

---

## Rank Change Certification Processing (Rank II & Rank I)

Practicing educators completing graduate programs at WKU submit applications to upgrade their state salary ranking:

*   **Rank II Advancement:** Conferred upon completion of the 30-hour [[programs/graduate/advanced-teacher-education-mae-0500|MAE in Advanced Teacher Education (0500)]], specialized MAE programs, or the planned 5th-year non-degree program.
*   **Rank I Advancement:** Conferred upon completion of 30 additional approved graduate hours beyond Rank II (e.g., [[programs/graduate/gifted-education-eds-0503|Ed.S. in Gifted Education 0503]] or planned 6th-year Rank I programs 084, 158, 124, 156, 113).
*   **Application Protocol:** Candidates initiate a Rank Change application in KECS; OPES audits transcripts and certifies that all approved curriculum contract hours have been satisfied.

---

## Out-of-State License Verification Audits

Graduates relocating outside Kentucky require formal institutional verification of program completion for out-of-state departments of education:
*   Email the out-of-state verification form with section 1 completed to [teacher.services@wku.edu](mailto:teacher.services@wku.edu).
*   OPES confirms CAEP accreditation, clinical clock hours, and degree conferral, returning the stamped document directly to the candidate or state licensing agency.

---

## Certification Personnel Contact
*   **Lead Certification Officer:** [[people/mrs-sarah-fischer|Mrs. Sarah Fischer]], Assistant Director
*   **Certification Office:** Gary A. Ransdell Hall 1097 / 1092
*   **Phone:** [(270) 745-3293](tel:12707453293)
*   **Email:** [teacher.services@wku.edu](mailto:teacher.services@wku.edu)

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[pathways-and-certification/rank-change-system]]: Kentucky Rank Change Framework
*   [[programs/certificates-and-endorsements/kentucky-teaching-endorsements-guide]]: EPSB Endorsement Guide
*   [[people/mrs-sarah-fischer]]: Assistant Director Profile
*   [[programs/graduate/advanced-teacher-education-mae-0500]]: Flagship Rank Master's Degree
""")

    # 7. opes/proficiency-evaluations-alternative-route.md
    with open("opes/proficiency-evaluations-alternative-route.md", "w") as f:
        f.write("""---
title: "Kentucky Alternative Certification: Proficiency Evaluation Route (16 KAR 5:030)"
type: "pathway"
tags: [alternative-certification, proficiency-evaluation, 16-kar-5-030, portfolio-review, temporary-provisional, elp, opes]
source_url: "https://www.wku.edu/alternative-teacher-certification/"
last_updated: "2026-09-02"
summary: "Comprehensive guide to WKU's Proficiency Evaluation Route under 16 KAR 5:030, enabling career changers and educators to earn certification via portfolio review and an Educator Learning Plan."
---

# Kentucky Alternative Certification: Proficiency Evaluation Route (16 KAR 5:030)

*Office of Professional Educator Services*  
*School of Teacher Education*  
*Western Kentucky University*

Western Kentucky University provides an innovative alternative certification pathway through the **Proficiency Evaluation Route**, governed by Kentucky Administrative Regulation **16 KAR 5:030**. 

Unlike conventional degree-bound programs that require 30–36 credit hours of formal coursework, the Proficiency Evaluation pathway recognizes prior competence, relevant school-based employment experience, and academic content mastery. Candidates demonstrate pedagogical readiness through a **rigorous digital portfolio of evidence**, enabling them to earn a teaching certificate faster while completing a tailored **Educator Learning Plan (ELP)**.

---

## Core Eligibility Criteria

To be eligible for the Proficiency Evaluation route, candidates must meet three foundational criteria:
1.  **Conferred Bachelor's Degree:** From a regionally accredited institution.
2.  **Academic GPA Threshold:** Minimum cumulative GPA of **2.75 or higher**, **OR** a minimum **3.0 GPA on the last 30 credit hours** attempted.
3.  **Relevant School-Based Experience:** Substantial, documented employment experience in a school setting related to the desired certification area (e.g., instructional aide, emergency certified substitute, private school teacher, paraprofessional).

---

## 7-Step Initial Teacher Certification Workflow

```text
Step 1: Inquiry Form ──────────► Step 2: App & $500 Fee ──────────► Step 3: Praxis II Content
      ↓                                                                   ↓
Step 4: Digital Portfolio ────► Step 5: Committee & ELP ────────► Step 6: 3-Hr Practicum
                                                                          ↓
                                                                Step 7: CA-1 Recommendation
```

### Step 1: Candidate Inquiry
Submit the electronic *Proficiency Evaluation Inquiry Form* via the WKU Alternative Certification portal. An advisor conducts an initial review of transcripts and school-based work history.

### Step 2: Formal Admission Application & $500 Assessment Fee
*   Submit a formal application to the WKU Graduate School.
*   Remit the **non-refundable $500 assessment fee** (cashier's check or money order payable to WKU Office of Professional Educator Services, 1906 College Heights Blvd. #61031, Bowling Green, KY 42104).
*   Submit clear background checks: Verified Credentials report, Child Abuse & Neglect (CAN) clearance, Medical Physical/TB screening, signed Kentucky Code of Ethics, and letters of recommendation.

### Step 3: Praxis II Content Exams
Candidates must register for and pass the required state **Praxis Subject Assessment (Praxis II)** and Principles of Learning and Teaching (PLT) exam for their certification discipline.

### Step 4: Digital Portfolio of Evidence
Candidates compile a comprehensive digital portfolio in Anthology demonstrating mastery across the **Kentucky Teacher Performance Standards (KTPS)**:
*   *Domain I: Planning & Preparation:* Lesson plans, curriculum maps, assessment rubrics.
*   *Domain II: Classroom Environment:* Behavior management frameworks, PBIS models.
*   *Domain III: Instruction:* Video recorded teaching samples, questioning strategies, student engagement artifacts.
*   *Domain IV: Professional Responsibilities:* Parent communication logs, PLC meeting notes, professional development records.

### Step 5: Faculty Committee Review & Educator Learning Plan (ELP)
*   A committee of STE content-area faculty evaluates the portfolio evidence.
*   If accepted, the committee constructs an individualized **Educator Learning Plan (ELP)** outlining any specific curricular or pedagogical competencies that must be satisfied.
*   **Temporary Provisional Certificate:** Once the candidate signs the ELP and secures employment in a Kentucky public school district, EPSB issues a **one-year Temporary Provisional Certificate** (renewable for one additional year). The candidate is hired and paid as a full-time teacher of record!
*   **Completion Timeline:** Candidates have a maximum of **two years** from the ELP approval date to complete all requirements.

### Step 6: Clinical Practicum Coursework
All initial certification proficiency candidates must complete at least **one 3-hour clinical practicum course** (e.g., EDU 590 or SPED 590) supervised by a WKU faculty mentor.

### Step 7: Program Exit & CA-1 Certification Recommendation
Upon satisfying all ELP requirements, the committee chair files the *Proficiency Evaluation Exit Form* with OPES. OPES then submits the electronic **CA-1 Recommendation** to EPSB/OELE, issuing the permanent Kentucky teaching certificate.

---

## Application Deadlines & Decision Cycles

| Application Cycle | Final Portfolio Submission Deadline | Faculty Committee Decision Date |
| :--- | :--- | :--- |
| **Fall Review Cycle** | **October 1st** | December 15th |
| **Spring Review Cycle** | **March 1st** | May 15th |
| **Summer Review Cycle** | **June 1st** | August 1st |

---

## Available Certification Disciplines under Proficiency Evaluation

### 1. Initial Certification Areas
*   **Elementary & Early Childhood:** Elementary Education (P–5), Interdisciplinary Early Childhood Education (Birth–Primary).
*   **Middle Grades (5–9):** Middle School English, Middle School Social Studies, Middle School Mathematics, Middle School Science.
*   **Secondary Education (8–12):** Biological Science, Chemistry, Mathematics, Physics, English, Social Studies.
*   **Specialized Areas:** Learning & Behavior Disorders (LBD, P–12), Business & Marketing Education, Family & Consumer Sciences, Physical Education, Chinese, Spanish.
*   **Administration:** School Principal (P–12).

### 2. Additional Certification Areas (For Currently Certified Teachers)
Practicing educators can add secondary biology, chemistry, math, ESL (P–12), Gifted Education (P–12), LBD, Moderate/Severe Disabilities (MSD), Reading Specialist, or School Media Librarian through portfolio review without taking unnecessary courses!

### 3. School Administrator Certifications
Supervisor of Instruction, Director of Special Education (DOSE), Director of Pupil Personnel (DPP), and Career & Technical Education (CTE) Principal.

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[pathways-and-certification/alternative-certification-option-6]]: Option 6 MAT Alternative Route
*   [[opes/teacher-certification-services]]: Certification Application Process
*   [[overview/accreditation-and-standards]]: KTPS Performance Standards
*   [[people/mrs-sarah-fischer]]: Assistant Director, OPES
""")

    # 8. opes/praxis-exams-and-support.md
    with open("opes/praxis-exams-and-support.md", "w") as f:
        f.write("""---
title: "Praxis Test Requirements, State Codes, & Preparation Support"
type: "pathway"
tags: [praxis, ets, praxis-core, praxis-ii, plt, test-codes, certification-exams, opes]
source_url: "https://www.wku.edu/educatorservices/praxis/index.php"
last_updated: "2026-09-02"
summary: "Authoritative reference for Kentucky Praxis testing requirements, ETS registration codes (WKU 1901, EPSB 7283), passing cut scores, and preparation resources."
---

# Praxis Test Requirements, State Codes, & Preparation Support

*Office of Professional Educator Services*  
*Gary A. Ransdell Hall, Suite 1092*  
*Western Kentucky University*

The **Praxis® tests**, administered by Educational Testing Service (ETS), are state-mandated examinations required by the Kentucky Education Professional Standards Board (EPSB) for admission into educator preparation programs and recommendation for initial Kentucky teacher certification.

The Office of Professional Educator Services (OPES) assists candidates with test alignment, passing score requirements, and test preparation resources.

---

## Institutional Registration Codes (Mandatory)

When registering for any Praxis examination at [ets.org/praxis](https://www.ets.org/praxis):
*   **Western Kentucky University Code:** **`1901`** (Must designate as a score recipient).
*   **Kentucky EPSB State Agency Code:** **`7283`** (Must designate as a score recipient).

> [!WARNING]
> **At-Home Testing Policy:** Praxis tests completed using the ETS "At Home" remote proctoring option **do NOT automatically report scores** to institutions. Candidates MUST explicitly select WKU (1901) and KY EPSB (7283) during test registration to avoid a $50 per-recipient retroactive reporting fee.

---

## The Two Testing Tiers in Educator Preparation

### Tier 1: Teacher Admissions Testing (Praxis CORE)
Required for undergraduate admission to the Professional Education Unit (unless waived via an ACT Composite score of 22+):

| Subtest Name | ETS Test Code | Kentucky Minimum Passing Score |
| :--- | :--- | :--- |
| **Core Academic Skills: Reading** | **5713** | **150** |
| **Core Academic Skills: Writing** | **5723** | **158** |
| **Core Academic Skills: Mathematics** | **5733** | **144** |

---

### Tier 2: Certification Testing (Praxis II & PLT)
Required prior to recommendation for initial Kentucky certification and Statement of Eligibility:

#### 1. Principles of Learning and Teaching (PLT) Exams:
*   **PLT: Early Childhood:** Test Code **5621** (Passing Score: **157**)
*   **PLT: Grades K–6:** Test Code **5622** (Passing Score: **160**)
*   **PLT: Grades 5–9:** Test Code **5623** (Passing Score: **160**)
*   **PLT: Grades 7–12:** Test Code **5624** (Passing Score: **157**)

#### 2. Selected Praxis II Subject Assessments:
*   **Elementary Education (P–5):** Elementary Education Multiple Subjects (5001: Reading 5002, Math 5003, Social Studies 5004, Science 5005) + Teaching Reading: Elementary (5205, Score: 159).
*   **Special Education (LBD):** Special Education: Core Knowledge and Mild to Moderate Applications (5543, Score: 158).
*   **Middle Grades English:** Middle School English Language Arts (5047, Score: 164).
*   **Middle Grades Mathematics:** Middle School Mathematics (5164, Score: 157).
*   **Middle Grades Science:** Middle School Science (5442, Score: 152).
*   **Middle Grades Social Studies:** Middle School Social Studies (5089, Score: 149).
*   **Secondary Mathematics (8–12):** Mathematics (5165, Score: 159).
*   **Secondary Biology (8–12):** Biology (5236, Score: 154).
*   **Secondary Chemistry (8–12):** Chemistry (5246, Score: 146).
*   **Secondary English (8–12):** English Language Arts: Content Knowledge (5038, Score: 167).
*   **Secondary Social Studies (8–12):** Social Studies: Content Knowledge (5081, Score: 156).

---

## Test Preparation Support & Fee Assistance
*   **ETS Interactive Practice Tests:** Full-length computer-delivered simulated tests available via ETS.
*   **WKU Praxis Tutoring & Study Guides:** Available through the CEBS Student Success Center in GRH and the WKU Learning Center.
*   **ETS Fee Waivers:** Candidates receiving federal financial aid (Pell Grant) may apply for an ETS Praxis Fee Waiver covering test registration fees.

---

## Backlinks / Related Documents
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/teacher-admissions]]: Admissions Requirements
*   [[opes/teacher-certification-services]]: Certification Application
*   [[pathways-and-certification/admission-to-teacher-education]]: Admission Testing
""")

    # 9. opes/INDEX.md
    with open("opes/INDEX.md", "w") as f:
        f.write("""---
title: "Office of Professional Educator Services (OPES) Map of Content"
type: "index"
tags: [opes, professional-educator-services, map-of-content, index, admissions, clinicals, certification, proficiency]
source_url: "https://www.wku.edu/educatorservices/index.php"
last_updated: "2026-09-02"
summary: "Central Map of Content (MOC) for the Office of Professional Educator Services (OPES), coordinating admissions, clinical field hours, student teaching, certification, and proficiency evaluations."
---

# Office of Professional Educator Services (OPES) Map of Content

*Gary A. Ransdell Hall (GRH), Suite 1092*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

The **Office of Professional Educator Services (OPES)** serves as the administrative operations center and primary supporting unit for the **School of Teacher Education (STE)**. OPES coordinates the end-to-end operational pipeline for all teacher candidates across admissions, clinical field placements, capstone student teaching, state licensure recommendations, and alternative certification routes.

---

## Quick Reference Contact Card

| Service Area | Primary Contact | Office Room | Phone / Contact |
| :--- | :--- | :--- | :--- |
| **OPES Suite Front Desk** | General Inquiries | Gary A. Ransdell Hall 1092 | [(270) 745-4897](tel:12707454897) |
| **Assistant Director** | [[people/mrs-sarah-fischer\|Mrs. Sarah Fischer]] | Gary A. Ransdell Hall 1097 | [(270) 745-3293](tel:12707453293) \| [sarah.fischer@wku.edu](mailto:sarah.fischer@wku.edu) |
| **Clinical Experiences / Student Teaching** | [[people/shannon-evans\|Shannon Evans]] | Gary A. Ransdell Hall 1096 | [(270) 745-3293](tel:12707453293) \| [shannon.evans@wku.edu](mailto:shannon.evans@wku.edu) |
| **Watermark SL&L System Support** | Lucas Green | Gary A. Ransdell Hall 1092 | [lucas.green@wku.edu](mailto:lucas.green@wku.edu) |
| **Admissions & Badge Email** | OPES Admissions Team | Gary A. Ransdell Hall 1092 | [teacher.services@wku.edu](mailto:teacher.services@wku.edu) |

---

## Master OPES Document Index

```text
                               ┌─────────────────────────┐
                               │        OPES HUB         │
                               │      (opes/INDEX)       │
                               └────────────┬────────────┘
        ┌──────────────┬──────────────┬─────┴──────┬──────────────┬──────────────┐
        ▼              ▼              ▼            ▼              ▼              ▼
   1. Overview    2. Admissions  3. Field Exp 4. Student Teach 5. Co-Teaching 6. Cert & Alt
```

### 1. Operations, Governance, & Staffing
*   [[opes/overview-and-staff|OPES Overview & Staff Directory]]: Operational mission as STE's supporting unit, physical suite details, administrative roles, and staff contacts.

### 2. Candidate Admissions to Educator Preparation
*   [[opes/teacher-admissions|Teacher Education Program Admissions]]: 3-step admissions framework, mandatory orientation sessions in GRH, 2.75 GPA requirement, background/CAN clearances, KDE physical form, and Praxis CORE passing thresholds.

### 3. Clinical Experiences & Pre-Service Fieldwork
*   [[opes/field-experience|Field Experience Requirements & Clinical Procedures]]: 200 clock hours pre-service observation under 16 KAR 5:040, digital tracking via KEC/KFETS, seven professional guidelines for visiting partner schools, and out-of-area requests.

### 4. Capstone Student Teaching Operations
*   [[opes/student-teaching-procedures|Student Teaching Procedures & Watermark SL&L Guide]]: Intensive 70-day clinical semester, application submission via Watermark Student Learning & Licensure (SL&L), 1-year advance deadlines (Oct 15 / Apr 15), and eligibility checklist.

### 5. Co-Teaching Framework & Cooperating Teachers
*   [[opes/co-teaching-model|WKU Co-Teaching Model & Cooperating Teacher Training]]: Research-based co-teaching philosophy, 16 KAR 5:040 cooperating teacher training sequence (Parts A, B, C), Dr. Rebecca Stobaugh's 7 methods of co-teaching, and supervising teacher tuition waivers.

### 6. Licensure & State Credentialing Recommendations
*   [[opes/teacher-certification-services|Teacher Certification Services & EPSB Recommendations]]: Official liaison to Kentucky EPSB / OELE, CA-1 application processing, Statement of Eligibility (SOE), Rank II/I salary change certification, and out-of-state verification.

### 7. Alternative Certification & Proficiency Evaluations
*   [[opes/proficiency-evaluations-alternative-route|Alternative Certification: Proficiency Evaluation Route (16 KAR 5:030)]]: Detailed 7-step process for initial certification, $500 fee, digital portfolio standards (KTPS), Educator Learning Plan (ELP), 1-year renewable Temporary Provisional Certificate, additional certification areas, and administrator pathways.

### 8. Testing Standards & Praxis Resources
*   [[opes/praxis-exams-and-support|Praxis Test Requirements, State Codes, & Preparation Support]]: Institutional codes (WKU: 1901, EPSB: 7283), Praxis Core and Subject Assessment passing scores, at-home testing policies, and fee waiver support.

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Index & Map of Content
*   [[overview/contact-and-facilities]]: Gary A. Ransdell Hall Map
*   [[overview/about-ste]]: STE Institutional Overview
*   [[pathways-and-certification/admission-to-teacher-education]]: Academic Admission Guide
*   [[pathways-and-certification/clinical-experiences-and-student-teaching]]: Program Clinical Blueprint
*   [[pathways-and-certification/rank-change-system]]: Kentucky Rank Change System
""")

    # 10. Atomic People Files for OPES Staff
    # people/mrs-sarah-fischer.md
    with open("people/mrs-sarah-fischer.md", "w") as f:
        f.write("""---
title: "Mrs. Sarah Fischer, Assistant Director, OPES"
type: "person"
tags: [faculty, staff, opes, assistant-director, teacher-admissions, teacher-certification, ransdell-hall]
source_url: "https://www.wku.edu/educatorservices/staff/index.php"
last_updated: "2026-09-02"
summary: "Assistant Director of the Office of Professional Educator Services (OPES), overseeing teacher admissions, state certification recommendations, and cooperating teacher training."
---

# Mrs. Sarah Fischer

*Assistant Director, Office of Professional Educator Services (OPES)*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

---

## Contact Information
*   **Office Location:** Gary A. Ransdell Hall (GRH), Room 1097
*   **Telephone:** [(270) 745-3293](tel:12707453293)
*   **Email:** [sarah.fischer@wku.edu](mailto:sarah.fischer@wku.edu)
*   **Departmental Unit:** [[opes/overview-and-staff|Office of Professional Educator Services (OPES)]]

---

## Professional Role & Institutional Responsibilities
As Assistant Director of OPES, Mrs. Sarah Fischer oversees the daily administration of educator preparation compliance across the School of Teacher Education and CEBS:
*   **Teacher Education Admissions:** Manages candidate admission to the Professional Education Unit, verification of GPA (2.75 minimum) and Praxis CORE scores, and leads Teacher Admissions Orientation sessions in GRH.
*   **Teacher Certification Officer:** Serves as WKU's official university certification officer recommending graduates to the Kentucky Education Professional Standards Board (EPSB) / Office of Educator Licensure and Effectiveness (OELE) for initial Statements of Eligibility, rank changes (Rank II/I), and endorsements.
*   **Cooperating Teacher Training:** Audits compliance with Kentucky regulation **16 KAR 5:040**, verifying that regional cooperating teachers complete Parts A, B, and C of the supervisory training curriculum.
*   **Proficiency Evaluation Oversight:** Coordinates administrative review for the [[opes/proficiency-evaluations-alternative-route|16 KAR 5:030 Proficiency Evaluation]] alternative certification route.

---

## Backlinks / Related Documents
*   [[people/INDEX]]: Master Faculty & Staff Directory
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/overview-and-staff]]: OPES Overview & Staff
*   [[opes/teacher-certification-services]]: Teacher Certification Services
*   [[opes/co-teaching-model]]: Cooperating Teacher Training
""")

    # people/shannon-evans.md
    with open("people/shannon-evans.md", "w") as f:
        f.write("""---
title: "Shannon Evans, Program Manager, OPES"
type: "person"
tags: [faculty, staff, opes, program-manager, student-teaching, clinical-placements, field-experience, ransdell-hall]
source_url: "https://www.wku.edu/educatorservices/staff/index.php"
last_updated: "2026-09-02"
summary: "Program Manager in the Office of Professional Educator Services (OPES), managing student teaching applications, placement preferences, and school district coordination."
---

# Shannon Evans

*Program Manager, Clinical Experiences & Student Teaching*  
*Office of Professional Educator Services (OPES)*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

---

## Contact Information
*   **Office Location:** Gary A. Ransdell Hall (GRH), Room 1096
*   **Telephone:** [(270) 745-3293](tel:12707453293)
*   **Email:** [shannon.evans@wku.edu](mailto:shannon.evans@wku.edu)
*   **Departmental Unit:** [[opes/overview-and-staff|Office of Professional Educator Services (OPES)]]

---

## Professional Role & Institutional Responsibilities
Shannon Evans leads the operational coordination of clinical placements and student teaching for the School of Teacher Education:
*   **Student Teaching Applications:** Manages candidate application workflows in **Watermark Student Learning & Licensure (SL&L)** for Fall and Spring placements, enforcing the 1-year advance deadlines (October 15 and April 15).
*   **District Placement Coordination:** Liaises with district human resources directors, building principals, and curriculum coordinators across Warren County, Bowling Green Independent, Daviess County, and regional public school systems to secure high-quality clinical placements.
*   **Field Placement Inquiries:** Assists teacher candidates with placement preferences, out-of-area requests, and eligibility audits.
*   **Handbook & Evaluation Support:** Coordinates distribution of the WKU Student Teaching Handbook, cooperating teacher evaluation materials, and clinical triad communication.

---

## Backlinks / Related Documents
*   [[people/INDEX]]: Master Faculty & Staff Directory
*   [[opes/INDEX]]: OPES Master Hub
*   [[opes/student-teaching-procedures]]: Student Teaching Guide
*   [[opes/field-experience]]: Field Experience Procedures
*   [[opes/overview-and-staff]]: OPES Overview & Staff
""")

    print("OPES module and staff files generated successfully.")

if __name__ == "__main__":
    generate_opes()
