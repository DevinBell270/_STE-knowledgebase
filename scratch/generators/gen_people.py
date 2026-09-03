import os

staff_data = [
    {
        "slug": "dr-susan-keesey",
        "name": "Dr. Susan Keesey",
        "degrees_str": "Ph.D., The Ohio State University (2012)",
        "full_degrees": "Ph.D. in Physical Activity and Education Services (Special Education), The Ohio State University Main Campus (2012); M.A. in Special Education; B.S. in Elementary Education.",
        "title": "Director, School of Teacher Education; Professor",
        "email": "susan.keesey@wku.edu",
        "office": "Gary A. Ransdell Hall 1105 / 1005",
        "phone": "(270) 745-5414",
        "role_category": "Executive Leadership & Administration",
        "tags": ["director", "administration", "special-education", "faculty", "professor"],
        "bio": "Dr. Susan Keesey serves as the Director of the School of Teacher Education at Western Kentucky University. In this capacity, she provides executive, academic, and operational leadership for all undergraduate and graduate teacher preparation programs, clinical partnerships, accreditation reviews, and faculty development within the School.",
        "expertise": "Special education administration, multi-tiered systems of support (MTSS), early literacy interventions for students with disabilities, candidate performance assessment, and teacher educator clinical preparation.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/graduate/advanced-teacher-education-mae-0500", "programs/graduate/special-education-lbd-mae-0457"]
    },
    {
        "slug": "dr-corinne-murphy",
        "name": "Dr. Corinne M. Murphy",
        "degrees_str": "Ph.D., BCBA-D, The Ohio State University (2006)",
        "full_degrees": "Ph.D. in Physical Activity and Education Services (Special Education & Applied Behavior Analysis), The Ohio State University Main Campus (2006); Board Certified Behavior Analyst - Doctoral (BCBA-D).",
        "title": "Dean, College of Education and Behavioral Sciences; Professor",
        "email": "corinne.murphy@wku.edu",
        "office": "Gary A. Ransdell Hall 2038",
        "phone": "(270) 745-4664",
        "role_category": "Executive Leadership & Administration",
        "tags": ["dean", "cebs", "administration", "aba", "special-education", "bcba"],
        "bio": "Dr. Corinne M. Murphy is the Dean of the College of Education and Behavioral Sciences (CEBS) at Western Kentucky University and Professor of Special Education and Applied Behavior Analysis. As Dean, she oversees the School of Teacher Education, the School of Leadership and Professional Studies, Psychology, Counseling and Student Affairs, the Suzanne Vitale CEC, and military science programs. She championed the landmark $350/credit hour Graduate Educator Tuition Discount.",
        "expertise": "Applied Behavior Analysis (ABA), autism spectrum disorders, clinical personnel preparation, behavioral interventions, and higher education academic leadership.",
        "programs_linked": ["overview/about-ste", "funding-and-aid/educator-tuition-discount", "programs/graduate/applied-behavior-analysis-ms-0508", "centers-and-partnerships/suzanne-vitale-clinical-education-complex"]
    },
    {
        "slug": "dr-jennifer-klemm",
        "name": "Dr. Jennifer P. Klemm",
        "degrees_str": "Ph.D., Southern Illinois University Carbondale (2010)",
        "full_degrees": "Ph.D. in Education, Southern Illinois University Carbondale (2010).",
        "title": "Associate Dean, College of Education and Behavioral Sciences; Professor",
        "email": "jennifer.klemm@wku.edu",
        "office": "Gary A. Ransdell Hall 2038",
        "phone": "(270) 745-4664",
        "role_category": "Executive Leadership & Administration",
        "tags": ["associate-dean", "cebs", "administration", "special-education", "faculty"],
        "bio": "Dr. Jennifer P. Klemm serves as Associate Dean in the College of Education and Behavioral Sciences. She coordinates college-level academic operations, curricular proposals through the Professional Education Council (PEC), student academic complaints, and accreditation compliance.",
        "expertise": "Teacher preparation policy, educator assessment, special education curriculum design, and university-school district clinical memoranda of understanding.",
        "programs_linked": ["overview/leadership-and-governance", "overview/accreditation-and-standards"]
    },
    {
        "slug": "dr-janet-tassell",
        "name": "Dr. Janet L. Tassell",
        "degrees_str": "Ph.D., Indiana University-Bloomington (2002)",
        "full_degrees": "Ph.D. in Curriculum & Instruction (Mathematics Education & Gifted Education), Indiana University-Bloomington (2002).",
        "title": "Assistant Director, School of Teacher Education; Program Coordinator; Professor",
        "email": "janet.tassell@wku.edu",
        "office": "Gary A. Ransdell Hall 1105 / 1005",
        "phone": "(270) 745-5306",
        "role_category": "Executive Leadership & Elementary / Math",
        "tags": ["assistant-director", "coordinator", "elementary-math", "stem", "professor"],
        "bio": "Dr. Janet L. Tassell is Assistant Director of the School of Teacher Education and Program Coordinator for Elementary Education and Mathematics Education. She spearheaded the design of the Elementary Mathematics Specialist (EMS) endorsement and certificate program and has directed major state and federal grants in teacher numeracy leadership.",
        "expertise": "Elementary mathematics pedagogy, math coaching, gifted mathematics education, numeracy intervention, and clinical educator preparation.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/certificates-and-endorsements/elementary-math-specialist-certificate-0485", "programs/graduate/advanced-teacher-education-mae-0500"]
    },
    {
        "slug": "dr-julia-link-roberts",
        "name": "Dr. Julia Link Roberts",
        "degrees_str": "Ed.D., Oklahoma State University (1970)",
        "full_degrees": "Ed.D. in Curriculum and Instruction, Oklahoma State University Main Campus (1970).",
        "title": "Mahurin Professor of Gifted Studies; Executive Director, The Center for Gifted Studies",
        "email": "julia.roberts@wku.edu",
        "office": "Gary A. Ransdell Hall 1019",
        "phone": "(270) 745-6323",
        "role_category": "Gifted Education Leadership",
        "tags": ["gifted-education", "mahurin-professor", "gatton-academy", "center-for-gifted-studies", "distinguished-faculty"],
        "bio": "Dr. Julia Link Roberts is the Mahurin Professor of Gifted Studies at WKU, Executive Director of The Center for Gifted Studies, and Executive Director of the Carol Martin Gatton Academy of Mathematics and Science. An internationally acclaimed scholar in gifted education, she has authored numerous seminal books on talent development, differentiation, and advocacy, and served on the Executive Committee of the World Council for Gifted and Talented Children.",
        "expertise": "Gifted child education, talent development, curriculum differentiation, advocacy, state policy for advanced learners, and educational leadership.",
        "programs_linked": ["programs/graduate/gifted-education-mae-0482", "programs/graduate/gifted-education-eds-0503", "programs/certificates-and-endorsements/gifted-education-certificate-1764"]
    },
    {
        "slug": "dr-christina-noel",
        "name": "Dr. Christina R. Noel",
        "degrees_str": "Ph.D., BCBA, Vanderbilt University (2013)",
        "full_degrees": "Ph.D. in Special Education, Vanderbilt University (2013); Board Certified Behavior Analyst (BCBA).",
        "title": "Director, Suzanne Vitale Clinical Education Complex; Professor of Special Education",
        "email": "christina.noel@wku.edu",
        "office": "Suzanne Vitale CEC / GRH 1082",
        "phone": "(270) 745-8989",
        "role_category": "Special Education & Clinical Leadership",
        "tags": ["special-education", "cec", "autism", "bcba", "kelly-autism-program"],
        "bio": "Dr. Christina R. Noel is Director of the Suzanne Vitale Clinical Education Complex (CEC) and Professor of Special Education in STE. She conducts extensive research on evidence-based behavioral and academic practices for students on the autism spectrum and individuals with severe emotional and behavioral disorders.",
        "expertise": "Autism spectrum disorders, applied behavior analysis, severe behavioral interventions, inclusive education, and clinical education management.",
        "programs_linked": ["centers-and-partnerships/suzanne-vitale-clinical-education-complex", "programs/graduate/special-education-lbd-mae-0457", "programs/graduate/special-education-msd-mae-0438", "programs/undergraduate/special-education-and-elementary-education-bs-5003"]
    },
    {
        "slug": "dr-jeremy-logsdon",
        "name": "Dr. Jeremy R. Logsdon",
        "degrees_str": "Ed.D. / Ph.D., Western Kentucky University",
        "full_degrees": "Doctoral studies in Educational Leadership and Literacy, Western Kentucky University.",
        "title": "Director, Center for Literacy; Assistant Professor of Literacy",
        "email": "jeremy.logsdon@wku.edu",
        "office": "Gary A. Ransdell Hall 1083B / Center for Literacy",
        "phone": "(270) 745-4309",
        "role_category": "Literacy & Reading Leadership",
        "tags": ["literacy", "reading-clinic", "center-for-literacy", "reading-specialist", "assistant-professor"],
        "bio": "Dr. Jeremy R. Logsdon serves as Director of the Center for Literacy and Assistant Professor of Literacy in STE. He directs the on-campus reading clinic, supervising graduate candidates in diagnostic reading assessments and clinical remediation practicums.",
        "expertise": "Diagnostic reading assessment, clinical reading practicums, structured literacy instruction, adolescent literacy, and community literacy partnerships.",
        "programs_linked": ["centers-and-partnerships/center-for-literacy", "programs/graduate/literacy-education-mae-044", "programs/certificates-and-endorsements/literacy-p12-certificate-1750"]
    },
    {
        "slug": "dr-martha-day",
        "name": "Dr. Martha M. Day",
        "degrees_str": "Ed.D., Tennessee State University (1998)",
        "full_degrees": "Ed.D. in Administration and Supervision, Tennessee State University (1998); M.S. in Chemistry.",
        "title": "SKyTeach Education Co-Director; Professor of Science Education",
        "email": "martha.day@wku.edu",
        "office": "Kelly Thompson Hall (KTH) 1011C",
        "phone": "(270) 745-3900",
        "role_category": "STEM & Secondary Education Leadership",
        "tags": ["skyteach", "stem", "science-education", "secondary-education", "uteach"],
        "bio": "Dr. Martha M. Day is Professor of Science Education and the Education Co-Director of SKyTeach, WKU's nationally acclaimed STEM teacher preparation model replicated from the UTeach initiative. She has authored multiple national science education curricula and led NSF-funded projects in inquiry-based science teaching.",
        "expertise": "Inquiry-based science instruction, chemistry education, STEM candidate recruitment, project-based learning (PBL), and secondary educator induction.",
        "programs_linked": ["centers-and-partnerships/skyteach-stem-program", "programs/undergraduate/science-and-mathematics-education-bs-774", "programs/undergraduate/secondary-education-certification"]
    },
    {
        "slug": "dr-ellen-casale",
        "name": "Dr. Ellen G. Casale",
        "degrees_str": "Ph.D., BCBA, LBA, Vanderbilt University (2021)",
        "full_degrees": "Ph.D. in Special Education, Vanderbilt University (2021); Board Certified Behavior Analyst (BCBA); Licensed Behavior Analyst (LBA).",
        "title": "Assistant Professor, Schools of Teacher Education and Leadership and Professional Studies",
        "email": "ellen.casale@wku.edu",
        "office": "Gary A. Ransdell Hall 1087",
        "phone": "(270) 745-4118",
        "role_category": "Special Education & Applied Behavior Analysis",
        "tags": ["special-education", "aba", "bcba", "behavior-management", "assistant-professor"],
        "bio": "Dr. Ellen G. Casale is an Assistant Professor with a joint appointment across the School of Teacher Education and SLPS. She is a BCBA and specializes in applied behavior analysis and classroom behavior management strategies for high-incidence and low-incidence disabilities.",
        "expertise": "Applied behavior analysis, single-case research design, functional behavior assessments (FBA), behavior intervention plans (BIP), and special education teacher mentoring.",
        "programs_linked": ["programs/graduate/applied-behavior-analysis-ms-0508", "programs/certificates-and-endorsements/advanced-behavior-management-certificate-1736", "programs/graduate/special-education-lbd-mae-0457"]
    },
    {
        "slug": "dr-nancy-hulan",
        "name": "Dr. Nancy F. Hulan",
        "degrees_str": "Ph.D., University of Louisville (2010)",
        "full_degrees": "Ph.D. in Curriculum and Instruction (Literacy), University of Louisville (2010).",
        "title": "Professor / Associate Professor of Literacy Education",
        "email": "nancy.hulan@wku.edu",
        "office": "Gary A. Ransdell Hall 1083A",
        "phone": "(270) 745-4324",
        "role_category": "Literacy & Elementary Education",
        "tags": ["literacy", "reading", "elementary-education", "curriculum", "faculty"],
        "bio": "Dr. Nancy F. Hulan is a senior scholar in literacy education in STE. Her research focuses on early reading acquisition, children's literature, reading comprehension strategy instruction, and professional development for classroom reading teachers.",
        "expertise": "Early literacy development, reading comprehension, children's literature, teacher preparation in phonics and phonemic awareness, and reading clinic practicum.",
        "programs_linked": ["programs/graduate/literacy-education-mae-044", "programs/undergraduate/elementary-education-bs-527", "centers-and-partnerships/center-for-literacy"]
    },
    {
        "slug": "dr-jeanine-huss",
        "name": "Dr. Jeanine M. Huss",
        "degrees_str": "Ph.D., Oklahoma State University (2007)",
        "full_degrees": "Ph.D. in Environmental Science, Oklahoma State University Main Campus (2007).",
        "title": "Professor of Elementary Education & Environmental Education",
        "email": "jeanine.huss@wku.edu",
        "office": "Gary A. Ransdell Hall 1010",
        "phone": "(270) 745-2293",
        "role_category": "Elementary & Environmental Education",
        "tags": ["elementary-education", "environmental-education", "sustainability", "professor", "faculty"],
        "bio": "Dr. Jeanine M. Huss is a Professor of Elementary Education in the School of Teacher Education. She coordinates the Environmental Education P-12 endorsement and certificate programs, integrating environmental literacy, outdoor learning, and sustainability science into elementary teacher education.",
        "expertise": "Environmental education, elementary science methods, place-based education, sustainability education, and qualitative educational inquiry.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/certificates-and-endorsements/kentucky-teaching-endorsements-guide", "programs/graduate/advanced-teacher-education-mae-0500"]
    },
    {
        "slug": "dr-pamela-jukes",
        "name": "Dr. Pamela M. Jukes",
        "degrees_str": "Ed.D., University of Kentucky (1997)",
        "full_degrees": "Ed.D. in Instruction and Administration, University of Kentucky (1997).",
        "title": "Professor of Elementary Education",
        "email": "pam.jukes@wku.edu",
        "office": "Gary A. Ransdell Hall 1012",
        "phone": "(270) 745-4485",
        "role_category": "Elementary Education Leadership",
        "tags": ["elementary-education", "curriculum", "clinical-preparation", "professor", "faculty"],
        "bio": "Dr. Pamela M. Jukes is a Professor of Elementary Education. She has served in multiple leadership roles in CEBS and STE, specializing in social studies pedagogical methods, elementary curriculum alignment, and clinical field mentoring.",
        "expertise": "Elementary social studies curriculum, teacher candidate evaluation, clinical mentoring models, and instructional design.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/graduate/advanced-teacher-education-mae-0500"]
    },
    {
        "slug": "dr-erin-margarella",
        "name": "Dr. Erin E. Margarella",
        "degrees_str": "Ph.D., University of South Florida (2016)",
        "full_degrees": "Ph.D. in Curriculum and Instruction (Secondary English Education), University of South Florida (2016).",
        "title": "Associate Professor, Middle and Secondary Education",
        "email": "erin.margarella@wku.edu",
        "office": "Gary A. Ransdell Hall 1080",
        "phone": "(270) 745-4417",
        "role_category": "Middle & Secondary Education",
        "tags": ["secondary-education", "middle-grades", "english-education", "associate-professor", "faculty"],
        "bio": "Dr. Erin E. Margarella is an Associate Professor of Middle and Secondary Education in STE. She teaches secondary English education methods, young adult literature, and instructional strategies for diverse secondary classrooms.",
        "expertise": "Secondary English language arts methods, writing pedagogy, young adult literature, and clinical supervision of secondary teacher candidates.",
        "programs_linked": ["programs/undergraduate/middle-level-education-bs-5001", "programs/undergraduate/secondary-education-certification", "programs/graduate/advanced-teacher-education-mae-0500"]
    },
    {
        "slug": "dr-julia-mittelberg",
        "name": "Dr. Julia A. Mittelberg",
        "degrees_str": "Ph.D., Kansas State University (2014)",
        "full_degrees": "Ph.D. in Curriculum and Instruction (Social Studies Education), Kansas State University (2014).",
        "title": "Associate Professor of Middle and Secondary Education",
        "email": "julia.mittelberg@wku.edu",
        "office": "Gary A. Ransdell Hall 1081",
        "phone": "(270) 745-4416",
        "role_category": "Middle & Secondary Education",
        "tags": ["social-studies", "middle-grades", "secondary-education", "associate-professor", "faculty"],
        "bio": "Dr. Julia A. Mittelberg is an Associate Professor of Middle and Secondary Education. Her research and teaching center on inquiry-based social studies pedagogy, democratic citizenship education, and secondary teacher candidate development.",
        "expertise": "Secondary social studies education, historical thinking skills, civic engagement pedagogy, and middle grades curriculum.",
        "programs_linked": ["programs/undergraduate/middle-level-education-bs-5001", "programs/undergraduate/secondary-education-certification"]
    },
    {
        "slug": "dr-andrea-paganelli",
        "name": "Dr. Andrea Paganelli",
        "degrees_str": "Ph.D., The University of Alabama (2010)",
        "full_degrees": "Ph.D. in Instructional Leadership (Library Media & Educational Technology), The University of Alabama (2010).",
        "title": "Associate Professor, Libraries, Informatics, and Technology in Education (LITE)",
        "email": "andrea.paganelli@wku.edu",
        "office": "Gary A. Ransdell Hall 1089",
        "phone": "(270) 745-4420",
        "role_category": "LITE & Instructional Technology",
        "tags": ["lite", "library-media", "educational-technology", "informatics", "associate-professor"],
        "bio": "Dr. Andrea Paganelli is an Associate Professor and lead faculty member for the Libraries, Informatics, and Technology in Education (LITE) program. She prepares school librarians, media specialists, and digital coaches in digital information management, curation, and educational technology integration.",
        "expertise": "School library media administration, educational technology integration, information literacy, digital curation, and emerging instructional tools.",
        "programs_linked": ["programs/graduate/libraries-informatics-technology-ms-0497", "programs/certificates-and-endorsements/ai-and-educational-technology-certificate-1796"]
    },
    {
        "slug": "dr-kandy-smith",
        "name": "Dr. Kandy C. Smith",
        "degrees_str": "Ph.D., University of Tennessee, Knoxville (2014)",
        "full_degrees": "Ph.D. in Education (Teacher Education & Literacy), University of Tennessee, Knoxville (2014).",
        "title": "Associate Professor of Literacy",
        "email": "kandy.smith@wku.edu",
        "office": "Gary A. Ransdell Hall 1083",
        "phone": "(270) 745-4433",
        "role_category": "Literacy & Reading",
        "tags": ["literacy", "reading-specialist", "elementary-education", "associate-professor", "faculty"],
        "bio": "Dr. Kandy C. Smith is an Associate Professor of Literacy in STE. She teaches graduate and undergraduate courses in reading diagnosis, content-area literacy strategies, and children's/adolescent literature.",
        "expertise": "Reading assessment, structured literacy interventions, writing instruction, and clinical teacher preparation.",
        "programs_linked": ["programs/graduate/literacy-education-mae-044", "centers-and-partnerships/center-for-literacy", "programs/undergraduate/elementary-education-bs-527"]
    },
    {
        "slug": "mr-josiah-super",
        "name": "Dr. Daniel Josiah Super",
        "degrees_str": "Ed.D., Western Kentucky University (2016)",
        "full_degrees": "Ed.D. in Educational Leadership, Western Kentucky University (2016); M.A. in Education.",
        "title": "Educational Specialist / Associate Professor",
        "email": "josiah.super@wku.edu",
        "office": "Gary A. Ransdell Hall 1033",
        "phone": "(270) 745-2819",
        "role_category": "Instructional Technology & Specialist Support",
        "tags": ["specialist", "instructional-technology", "leadership", "faculty", "ransdell-hall"],
        "bio": "Dr. Daniel Josiah Super serves as an Educational Specialist and faculty member in STE. He oversees technology-enhanced learning resources in Gary A. Ransdell Hall and supports faculty and candidates in digital tool implementation.",
        "expertise": "Educational leadership, educational technology integration, distance education instructional systems, and assessment technology.",
        "programs_linked": ["overview/contact-and-facilities", "programs/certificates-and-endorsements/ai-and-educational-technology-certificate-1796"]
    },
    {
        "slug": "dr-trudy-little",
        "name": "Dr. Trudy M. Little",
        "degrees_str": "Ph.D., BCBA, Vanderbilt University (2023)",
        "full_degrees": "Ph.D. in Special Education & Early Intervention, Vanderbilt University (2023); Board Certified Behavior Analyst (BCBA).",
        "title": "Assistant Professor, Interdisciplinary Early Childhood Education & Special Education",
        "email": "trudy.little@wku.edu",
        "office": "Gary A. Ransdell Hall 1084",
        "phone": "(270) 745-4444",
        "role_category": "Early Childhood & Special Education",
        "tags": ["iece", "early-childhood", "special-education", "bcba", "assistant-professor"],
        "bio": "Dr. Trudy M. Little is an Assistant Professor specializing in Interdisciplinary Early Childhood Education (IECE) and Special Education. Her scholarship focuses on early intervention for infants, toddlers, and preschoolers with developmental delays and behavioral challenges.",
        "expertise": "Interdisciplinary early childhood education (Birth to Primary), early intervention (IFSP/IEP), family-centered practice, and positive behavioral support.",
        "programs_linked": ["programs/undergraduate/interdisciplinary-early-childhood-education-bs-526", "programs/graduate/interdisciplinary-early-childhood-mat-0460", "programs/graduate/interdisciplinary-early-childhood-mae-0461"]
    },
    {
        "slug": "dr-erin-coffield-feeney",
        "name": "Dr. Erin M. Coffield-Feeney",
        "degrees_str": "Ph.D., West Virginia University (2022)",
        "full_degrees": "Ph.D. in Education (Curriculum & Instruction), West Virginia University (2022).",
        "title": "Assistant Professor, Elementary Education",
        "email": "erin.coffield@wku.edu",
        "office": "Gary A. Ransdell Hall 1086",
        "phone": "(270) 745-8752",
        "role_category": "Elementary Education",
        "tags": ["elementary-education", "curriculum", "instruction", "assistant-professor", "faculty"],
        "bio": "Dr. Erin M. Coffield-Feeney is an Assistant Professor of Elementary Education in STE. She teaches undergraduate methods courses in elementary curriculum, assessment, and instructional design.",
        "expertise": "Elementary curriculum design, clinical teacher preparation, formative classroom assessment, and student engagement strategies.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/graduate/advanced-teacher-education-mae-0500"]
    },
    {
        "slug": "dr-shannon-pardue",
        "name": "Dr. Shannon D. Pardue",
        "degrees_str": "Ph.D., University of North Carolina at Charlotte (2026)",
        "full_degrees": "Ph.D. in Special Education, University of North Carolina at Charlotte (2026).",
        "title": "Assistant Professor, Special Education",
        "email": "shannon.pardue@wku.edu",
        "office": "Gary A. Ransdell Hall 1088",
        "phone": "(270) 745-5414",
        "role_category": "Special Education",
        "tags": ["special-education", "lbd", "inclusion", "assistant-professor", "faculty"],
        "bio": "Dr. Shannon D. Pardue is an Assistant Professor of Special Education in STE. She specializes in Learning and Behavior Disorders (LBD), multi-tiered systems of support, and inclusive classroom instructional adaptations.",
        "expertise": "Learning and Behavior Disorders (LBD), high-incidence disabilities, evidence-based academic interventions, and special education legal mandates.",
        "programs_linked": ["programs/undergraduate/special-education-and-elementary-education-bs-5003", "programs/graduate/special-education-lbd-mae-0457"]
    },
    {
        "slug": "dr-brooke-royalty",
        "name": "Dr. Jordan Brooke Royalty",
        "degrees_str": "Ph.D., Liberty University (2026)",
        "full_degrees": "Ph.D. in Special Education, Liberty University (2026); M.Ed. in Special Education.",
        "title": "Assistant Professor, Special Education",
        "email": "brooke.royalty@wku.edu",
        "office": "Gary A. Ransdell Hall 1084",
        "phone": "(270) 745-5414",
        "role_category": "Special Education",
        "tags": ["special-education", "lbd", "msd", "assistant-professor", "faculty"],
        "bio": "Dr. Jordan Brooke Royalty is an Assistant Professor of Special Education in STE. She teaches coursework across initial certification and advanced graduate special education sequences, focusing on differentiated instructional strategies.",
        "expertise": "Special education teacher preparation, co-teaching models, IEP development, and individualized instructional adaptations for exceptional learners.",
        "programs_linked": ["programs/undergraduate/special-education-and-elementary-education-bs-5003", "programs/graduate/special-education-initial-certification-mat-0456"]
    },
    {
        "slug": "dr-leslee-bailey-tarbett",
        "name": "Dr. Leslee Bailey Tarbett",
        "degrees_str": "Ed.D., University of Memphis (2020)",
        "full_degrees": "Ed.D. in Instruction and Curriculum Leadership (Special Education), University of Memphis (2020).",
        "title": "Assistant Professor of Special Education",
        "email": "leslee.tarbett@wku.edu",
        "office": "Gary A. Ransdell Hall 1084",
        "phone": "(270) 745-4444",
        "role_category": "Special Education",
        "tags": ["special-education", "lbd", "inclusion", "assistant-professor", "faculty"],
        "bio": "Dr. Leslee Bailey Tarbett is an Assistant Professor of Special Education. Her scholarly focus includes transition planning for youth with disabilities, universal design for learning (UDL), and collaborative school models.",
        "expertise": "Secondary transition for youth with disabilities, UDL implementation, behavior intervention, and special education field supervision.",
        "programs_linked": ["programs/graduate/special-education-lbd-mae-0457", "programs/graduate/special-education-msd-mae-0438"]
    },
    {
        "slug": "dr-renming-liu",
        "name": "Dr. Renming Liu",
        "degrees_str": "Ph.D., Baylor University (2026)",
        "full_degrees": "Ph.D. in Educational Psychology (Quantitative Research Methods & Measurement), Baylor University (2026).",
        "title": "Assistant Professor of Educational Psychology / Research",
        "email": "renming.liu@wku.edu",
        "office": "Gary A. Ransdell Hall 1088",
        "phone": "(270) 745-5414",
        "role_category": "Research & Educational Foundations",
        "tags": ["educational-psychology", "research-methods", "quantitative-analysis", "assistant-professor", "faculty"],
        "bio": "Dr. Renming Liu is an Assistant Professor in STE teaching graduate research methods, statistics, and educational psychology courses for teacher leaders and specialist candidates.",
        "expertise": "Educational measurement, psychometrics, quantitative inquiry, student motivation, and classroom assessment systems.",
        "programs_linked": ["programs/graduate/advanced-teacher-education-mae-0500", "programs/graduate/gifted-education-eds-0503"]
    },
    {
        "slug": "dr-mindy-waldrop",
        "name": "Dr. Mindy C. Waldrop",
        "degrees_str": "Ph.D., University of Mississippi (2024)",
        "full_degrees": "Ph.D. in Education (Curriculum & Instruction), University of Mississippi (2024).",
        "title": "Assistant Professor, School of Teacher Education",
        "email": "mindy.waldrop@wku.edu",
        "office": "Gary A. Ransdell Hall 1088",
        "phone": "(270) 745-5414",
        "role_category": "Elementary & Teacher Education",
        "tags": ["teacher-education", "curriculum", "assistant-professor", "faculty"],
        "bio": "Dr. Mindy C. Waldrop is an Assistant Professor in STE. Her research focuses on teacher candidate efficacy, pedagogical coaching in clinical settings, and early elementary literacy integration.",
        "expertise": "Curriculum theory, elementary literacy coaching, teacher candidate reflection, and pedagogical innovation.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527"]
    },
    {
        "slug": "dr-kierra-chandler",
        "name": "Dr. Kierra A. Chandler",
        "degrees_str": "Ed.D., Carson-Newman University (2025)",
        "full_degrees": "Ed.D. in Educational Leadership, Carson-Newman University (2025); M.Ed.",
        "title": "Visiting Assistant Professor",
        "email": "kierra.chandler@wku.edu",
        "office": "Gary A. Ransdell Hall 1105",
        "phone": "(270) 745-2345",
        "role_category": "Teacher Education Instruction",
        "tags": ["visiting-professor", "leadership", "teacher-education", "faculty"],
        "bio": "Dr. Kierra A. Chandler is a Visiting Assistant Professor in STE, contributing to undergraduate professional education core courses and clinical mentoring.",
        "expertise": "Educational leadership, culturally responsive teaching, teacher candidate development, and classroom management.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/undergraduate/middle-level-education-bs-5001"]
    },
    {
        "slug": "katie-decker",
        "name": "Kathryn (Katie) L. Decker",
        "degrees_str": "MAE, Western Kentucky University (2007)",
        "full_degrees": "MAE in Elementary Education, Western Kentucky University (2007); B.S. in Elementary Education.",
        "title": "Clinical Assistant Professor, Elementary Education",
        "email": "katie.decker@wku.edu",
        "office": "Gary A. Ransdell Hall 2014",
        "phone": "(270) 745-4202",
        "role_category": "Clinical Faculty & Field Mentoring",
        "tags": ["clinical-faculty", "elementary-education", "field-supervision", "student-teaching"],
        "bio": "Kathryn (Katie) Decker is a Clinical Assistant Professor in Elementary Education. She coordinates clinical field placements and mentors undergraduate teacher candidates during clinical field courses and student teaching semesters.",
        "expertise": "Clinical practice mentoring, co-teaching models, elementary classroom management, and lesson planning design.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "pathways-and-certification/clinical-experiences-and-student-teaching"]
    },
    {
        "slug": "dr-angela-dyer-nagel",
        "name": "Dr. Angela D. Dyer-Nagel",
        "degrees_str": "Ed.D., Union University (2019)",
        "full_degrees": "Ed.D. in P-12 Educational Leadership, Union University (2019).",
        "title": "Research Assistant Professor",
        "email": "angela.nagel@wku.edu",
        "office": "Gary A. Ransdell Hall 1013",
        "phone": "(270) 745-4054",
        "role_category": "Research & Grant Administration",
        "tags": ["research-professor", "educational-leadership", "grant-administration", "faculty"],
        "bio": "Dr. Angela Dyer-Nagel serves as a Research Assistant Professor in STE, supporting externally funded grant initiatives, programmatic assessment research, and P-12 leadership partnerships.",
        "expertise": "P-12 educational leadership, program evaluation, educational data analysis, and grant writing.",
        "programs_linked": ["overview/accreditation-and-standards", "programs/graduate/advanced-teacher-education-mae-0500"]
    },
    {
        "slug": "melanie-owens",
        "name": "Ms. Melanie D. Owens",
        "degrees_str": "MAE, Western Kentucky University (1992)",
        "full_degrees": "MAE in Secondary Education, Western Kentucky University (1992); B.S. in Mathematics.",
        "title": "SKyTeach Master Teacher / Instructor I",
        "email": "melanie.owens@wku.edu",
        "office": "Kelly Thompson Hall (KTH) 1011",
        "phone": "(270) 745-3900",
        "role_category": "SKyTeach Master Teachers",
        "tags": ["skyteach", "master-teacher", "stem", "mathematics-education", "instructor"],
        "bio": "Ms. Melanie D. Owens is a Master Teacher in the SKyTeach program. A veteran high school mathematics educator, she mentors STEM majors through their introductory and advanced field teaching experiences in regional schools.",
        "expertise": "Secondary mathematics instruction, STEM inquiry lessons, 5E learning cycle, and clinical coaching of future math teachers.",
        "programs_linked": ["centers-and-partnerships/skyteach-stem-program", "programs/undergraduate/science-and-mathematics-education-bs-774"]
    },
    {
        "slug": "emily-perkins",
        "name": "Mrs. Emily S. Perkins",
        "degrees_str": "B.S., Western Kentucky University (1994)",
        "full_degrees": "B.S. in Middle Grades Education (Science & Math), Western Kentucky University (1994).",
        "title": "SKyTeach Master Teacher / Instructor I",
        "email": "emily.perkins@wku.edu",
        "office": "Kelly Thompson Hall (KTH) 1011",
        "phone": "(270) 745-3900",
        "role_category": "SKyTeach Master Teachers",
        "tags": ["skyteach", "master-teacher", "stem", "middle-grades-science", "instructor"],
        "bio": "Mrs. Emily S. Perkins is a Master Teacher in SKyTeach. She brings extensive public school classroom experience to guide STEM majors in developing hands-on, inquiry-driven science lessons for middle and high school students.",
        "expertise": "Middle grades science pedagogy, inquiry lesson design, classroom management in laboratory settings, and candidate mentoring.",
        "programs_linked": ["centers-and-partnerships/skyteach-stem-program", "programs/undergraduate/science-and-mathematics-education-bs-774"]
    },
    {
        "slug": "mr-rico-tyler",
        "name": "Mr. Rico Tyler",
        "degrees_str": "M.S., Western Kentucky University",
        "full_degrees": "M.S. in Physics / Science Education, Western Kentucky University; B.S. in Physics.",
        "title": "Master Teacher / Transitional Retiree, SKyTeach",
        "email": "rico.tyler@wku.edu",
        "office": "Kelly Thompson Hall (KTH) 1011",
        "phone": "(270) 745-3900",
        "role_category": "SKyTeach Master Teachers",
        "tags": ["skyteach", "physics-education", "stem", "master-teacher"],
        "bio": "Mr. Rico Tyler is a founding Master Teacher in SKyTeach. Recognized across Kentucky for physics and astronomy education, he mentors secondary physics, chemistry, and earth science teacher candidates.",
        "expertise": "Physics education, astronomy outreach, hands-on STEM laboratory demonstrations, and secondary science teacher mentoring.",
        "programs_linked": ["centers-and-partnerships/skyteach-stem-program", "programs/undergraduate/science-and-mathematics-education-bs-774"]
    },
    {
        "slug": "jessica-hussung",
        "name": "Jessica M. Hussung",
        "degrees_str": "M.S., Western Kentucky University (2022)",
        "full_degrees": "M.S., Western Kentucky University (2022); B.S. in Education.",
        "title": "Instructor II",
        "email": "jessica.hussung@wku.edu",
        "office": "Gary A. Ransdell Hall 1085",
        "phone": "(270) 745-5414",
        "role_category": "Instructors & Specialized Teaching Faculty",
        "tags": ["instructor", "teacher-education", "clinical-preparation", "faculty"],
        "bio": "Jessica M. Hussung serves as Instructor II in the School of Teacher Education, teaching core foundational and pedagogical courses in teacher preparation.",
        "expertise": "Teacher candidate preparation, classroom management, foundations of education, and clinical practice supervision.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527"]
    },
    {
        "slug": "dr-stephanie-jernigan",
        "name": "Dr. Stephanie S. Jernigan",
        "degrees_str": "Ed.D., Lipscomb University (2022)",
        "full_degrees": "Ed.D. in Education Leadership, Lipscomb University (2022); M.Ed.",
        "title": "Instructor II",
        "email": "stephanie.jernigan@wku.edu",
        "office": "Gary A. Ransdell Hall 1085",
        "phone": "(270) 745-5414",
        "role_category": "Instructors & Specialized Teaching Faculty",
        "tags": ["instructor", "leadership", "teacher-education", "faculty"],
        "bio": "Dr. Stephanie S. Jernigan is an Instructor II in STE, delivering instructional coursework in teacher education foundations, classroom leadership, and instructional design.",
        "expertise": "Educational leadership, curriculum implementation, teacher mentoring, and professional education seminar facilitation.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527"]
    },
    {
        "slug": "charley-jo-vaughn",
        "name": "Charley Jo Vaughn",
        "degrees_str": "MAE, Western Kentucky University (2022)",
        "full_degrees": "MAE in Special Education, Western Kentucky University (2022); B.S. in Special Education.",
        "title": "Visiting Assistant Professor / Instructor",
        "email": "charley.vaughn@wku.edu",
        "office": "Gary A. Ransdell Hall 1085",
        "phone": "(270) 745-5414",
        "role_category": "Instructors & Specialized Teaching Faculty",
        "tags": ["special-education", "lbd", "instructor", "faculty"],
        "bio": "Charley Jo Vaughn serves as an instructor in Special Education, teaching undergraduate and graduate introductory courses in exceptionalities and behavior management.",
        "expertise": "Special education foundations, inclusive classroom practices, IEP development, and field experience coaching.",
        "programs_linked": ["programs/undergraduate/special-education-and-elementary-education-bs-5003"]
    },
    {
        "slug": "bailey-payne",
        "name": "Bailey A. Payne",
        "degrees_str": "M.S., Pittsburg State University (2012)",
        "full_degrees": "M.S. in Psychology (Behavior Analysis), Pittsburg State University (2012); B.S. in Psychology.",
        "title": "Instructor II, Psychology / Behavior Analysis",
        "email": "bailey.payne@wku.edu",
        "office": "Gary A. Ransdell Hall 1085",
        "phone": "(270) 745-5414",
        "role_category": "Instructors & Specialized Teaching Faculty",
        "tags": ["aba", "psychology", "behavior-analysis", "instructor"],
        "bio": "Bailey A. Payne is an Instructor II in STE and the Applied Behavior Analysis program, teaching coursework in behavioral assessment, principles of behavior, and classroom ethics.",
        "expertise": "Applied behavior analysis, principles of learning, behavioral assessment, and single-subject data evaluation.",
        "programs_linked": ["programs/graduate/applied-behavior-analysis-ms-0508", "programs/certificates-and-endorsements/advanced-behavior-management-certificate-1736"]
    },
    {
        "slug": "kim-taylor",
        "name": "Kimberly A. Taylor",
        "degrees_str": "MAE, Western Kentucky University (1997)",
        "full_degrees": "MAE in Education, Western Kentucky University (1997); B.S. in Elementary Education.",
        "title": "Instructor II",
        "email": "kimberly.taylor@wku.edu",
        "office": "Gary A. Ransdell Hall 1085",
        "phone": "(270) 745-5414",
        "role_category": "Instructors & Specialized Teaching Faculty",
        "tags": ["instructor", "elementary-education", "clinical-supervision"],
        "bio": "Kimberly A. Taylor is an Instructor II in STE, specializing in elementary education methods and clinical field supervision of student teachers across regional districts.",
        "expertise": "Elementary education methods, student teaching clinical observation, teacher candidate portfolio mentoring, and school district liaison work.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "pathways-and-certification/clinical-experiences-and-student-teaching"]
    },
    {
        "slug": "sally-tooley",
        "name": "Sally H. Tooley",
        "degrees_str": "MAE, Western Kentucky University (2009)",
        "full_degrees": "MAE in Elementary Education (Literacy), Western Kentucky University (2009); B.S. in Elementary Education.",
        "title": "Instructor of Literacy and Elementary Education",
        "email": "sally.tooley@wku.edu",
        "office": "Gary A. Ransdell Hall 1085",
        "phone": "(270) 745-5414",
        "role_category": "Instructors & Specialized Teaching Faculty",
        "tags": ["literacy", "elementary-education", "reading", "instructor"],
        "bio": "Sally H. Tooley is an Instructor in STE teaching undergraduate literacy courses (LTCY 320, LTCY 421) and elementary instructional methods.",
        "expertise": "Foundational reading instruction, phonemic awareness, elementary writing workshops, and clinical field mentoring.",
        "programs_linked": ["programs/undergraduate/elementary-education-bs-527", "programs/graduate/literacy-education-mae-044"]
    },
    {
        "slug": "christina-heady",
        "name": "Christina Heady",
        "degrees_str": "M.S. in Library & Information Science / Technology",
        "full_degrees": "Master's degree in Information Science and Educational Technology.",
        "title": "Specialist, School of Teacher Education",
        "email": "christina.heady@wku.edu",
        "office": "Gary A. Ransdell Hall 1033",
        "phone": "(270) 745-2819",
        "role_category": "Professional Staff & Specialists",
        "tags": ["specialist", "technology", "support-staff", "curriculum-resources"],
        "bio": "Christina Heady serves as a Specialist in STE, managing curriculum resource collections, digital instructional databases, and technological equipment for teacher candidates and faculty in Gary A. Ransdell Hall.",
        "expertise": "Educational resource curation, educational technology maintenance, candidate testing resources, and instructional lab support.",
        "programs_linked": ["overview/contact-and-facilities"]
    },
    {
        "slug": "meredith-stewart",
        "name": "Meredith Stewart",
        "degrees_str": "B.S. / M.A., Western Kentucky University",
        "full_degrees": "Academic advising credentials and master's coursework at Western Kentucky University.",
        "title": "Academic Advisor, School of Teacher Education",
        "email": "meredith.stewart@wku.edu",
        "office": "Gary A. Ransdell Hall 1005",
        "phone": "(270) 745-5414",
        "role_category": "Professional Staff & Specialists",
        "tags": ["advising", "undergraduate-advisor", "recruitment", "student-success"],
        "bio": "Meredith Stewart is the primary Academic Advisor for undergraduate students in the School of Teacher Education. She advises students on degree tracks, prerequisite course sequences, admission to teacher education requirements, and graduation checks.",
        "expertise": "Undergraduate degree audits, teacher admissions counseling, Colonnade transfer evaluations, and student success interventions.",
        "programs_linked": ["pathways-and-certification/become-a-teacher", "pathways-and-certification/admission-to-teacher-education", "programs/undergraduate/elementary-education-bs-527"]
    },
    {
        "slug": "mandy-zeh",
        "name": "Mandy Zeh",
        "degrees_str": "B.A. / B.S., Western Kentucky University",
        "full_degrees": "Higher education administrative and office management credentials.",
        "title": "Office Coordinator, School of Teacher Education",
        "email": "mandy.zeh@wku.edu",
        "office": "Gary A. Ransdell Hall 1005",
        "phone": "(270) 745-5414",
        "role_category": "Professional Staff & Specialists",
        "tags": ["office-coordinator", "administration", "budget", "operations", "support-staff"],
        "bio": "Mandy Zeh serves as the Office Coordinator for the School of Teacher Education. She manages front-office operations, department budgets, scheduling, course scheduling, payroll coordination, and general administrative inquiries in GRH 1005.",
        "expertise": "University financial systems, course scheduling, departmental event management, faculty travel coordination, and visitor reception.",
        "programs_linked": ["overview/contact-and-facilities", "overview/leadership-and-governance"]
    }
]

def generate_people():
    print(f"Generating {len(staff_data)} individual faculty and staff profiles...")
    
    for s in staff_data:
        filename = f"people/{s['slug']}.md"
        with open(filename, "w") as f:
            f.write(f"""---
title: "{s['name']}"
type: "person"
tags: {s['tags']}
source_url: "https://www.wku.edu/ste/staff/{s['slug'].replace('dr-', '').replace('mr-', '').replace('-', '_')}"
last_updated: "2026-09-02"
summary: "{s['title']} in the WKU School of Teacher Education. Specialization: {s['expertise']}."
---

# {s['name']}

**{s['title']}**  
*School of Teacher Education*  
*College of Education and Behavioral Sciences*  
*Western Kentucky University*

---

## Contact Information

*   **Office Location:** {s['office']}
*   **Email:** [{s['email']}](mailto:{s['email']})
*   **Phone:** [{s['phone']}](tel:{s['phone'].replace('(', '').replace(')', '').replace(' ', '').replace('-', '')})
*   **Department Address:** 1906 College Heights Blvd. #11030, Bowling Green, KY 42101-1030
*   **Official Directory Listing:** [WKU Staff Listing](https://www.wku.edu/ste/staff/{s['slug'].replace('dr-', '').replace('mr-', '').replace('-', '_')})

---

## Academic Credentials

*   **Highest Degree:** {s['degrees_str']}
*   **Educational Background:** {s['full_degrees']}

---

## Professional Role & Biography

{s['bio']}

---

## Areas of Expertise & Research Interests

*   {s['expertise']}

---

## Associated Programs & Centers

""")
            for p in s['programs_linked']:
                p_name = p.split('/')[-1].replace('-', ' ').title()
                f.write(f"*   [[{p}|{p_name}]]\n")

            f.write(f"""
---

## Backlinks / Related Documents
*   [[people/INDEX]]: School of Teacher Education Faculty & Staff Directory
*   [[overview/leadership-and-governance]]: STE Leadership and Organizational Governance
*   [[overview/contact-and-facilities]]: Gary A. Ransdell Hall Facilities and Directory
""")
    
    # Generate people/INDEX.md
    print("Generating people/INDEX.md...")
    with open("people/INDEX.md", "w") as f:
        f.write("""---
title: "School of Teacher Education Faculty & Staff Directory"
type: "index"
tags: [wku, ste, faculty, staff, directory, people, contact]
source_url: "https://www.wku.edu/ste/staff/"
last_updated: "2026-09-02"
summary: "Master directory of all 39 faculty members, administrators, master teachers, specialists, and staff in the WKU School of Teacher Education."
---

# School of Teacher Education Faculty & Staff Directory

This directory provides comprehensive profiles for all 39 faculty, administrators, master teachers, specialists, and academic advisors within the School of Teacher Education at Western Kentucky University.

---

## Executive Leadership & Administration

| Name | Role / Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-corinne-murphy|Dr. Corinne M. Murphy]] | Dean, CEBS; Professor | GRH 2038 | corinne.murphy@wku.edu | (270) 745-4664 |
| [[people/dr-jennifer-klemm|Dr. Jennifer P. Klemm]] | Associate Dean, CEBS; Professor | GRH 2038 | jennifer.klemm@wku.edu | (270) 745-4664 |
| [[people/dr-susan-keesey|Dr. Susan Keesey]] | Director, STE; Professor | GRH 1105 / 1005 | susan.keesey@wku.edu | (270) 745-5414 |
| [[people/dr-janet-tassell|Dr. Janet L. Tassell]] | Assistant Director, STE; Coordinator; Professor | GRH 1105 / 1005 | janet.tassell@wku.edu | (270) 745-5306 |
| [[people/mandy-zeh|Mandy Zeh]] | Office Coordinator | GRH 1005 | mandy.zeh@wku.edu | (270) 745-5414 |
| [[people/meredith-stewart|Meredith Stewart]] | Academic Advisor | GRH 1005 | meredith.stewart@wku.edu | (270) 745-5414 |

---

## Elementary Education Faculty

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-janet-tassell|Dr. Janet L. Tassell]] | Professor & Elementary Math Lead | GRH 1105 | janet.tassell@wku.edu | (270) 745-5306 |
| [[people/dr-pamela-jukes|Dr. Pamela M. Jukes]] | Professor | GRH 1012 | pam.jukes@wku.edu | (270) 745-4485 |
| [[people/dr-jeanine-huss|Dr. Jeanine M. Huss]] | Professor | GRH 1010 | jeanine.huss@wku.edu | (270) 745-2293 |
| [[people/dr-erin-coffield-feeney|Dr. Erin M. Coffield-Feeney]] | Assistant Professor | GRH 1086 | erin.coffield@wku.edu | (270) 745-8752 |
| [[people/katie-decker|Kathryn (Katie) Decker]] | Clinical Assistant Professor | GRH 2014 | katie.decker@wku.edu | (270) 745-4202 |
| [[people/dr-mindy-waldrop|Dr. Mindy C. Waldrop]] | Assistant Professor | GRH 1088 | mindy.waldrop@wku.edu | (270) 745-5414 |
| [[people/kim-taylor|Kimberly A. Taylor]] | Instructor II | GRH 1085 | kimberly.taylor@wku.edu | (270) 745-5414 |
| [[people/jessica-hussung|Jessica M. Hussung]] | Instructor II | GRH 1085 | jessica.hussung@wku.edu | (270) 745-5414 |

---

## Middle Grades & Secondary Education Faculty

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-erin-margarella|Dr. Erin E. Margarella]] | Associate Professor (Secondary English) | GRH 1080 | erin.margarella@wku.edu | (270) 745-4417 |
| [[people/dr-julia-mittelberg|Dr. Julia A. Mittelberg]] | Associate Professor (Social Studies) | GRH 1081 | julia.mittelberg@wku.edu | (270) 745-4416 |
| [[people/dr-kierra-chandler|Dr. Kierra A. Chandler]] | Visiting Assistant Professor | GRH 1105 | kierra.chandler@wku.edu | (270) 745-2345 |
| [[people/dr-stephanie-jernigan|Dr. Stephanie S. Jernigan]] | Instructor II | GRH 1085 | stephanie.jernigan@wku.edu | (270) 745-5414 |

---

## Special Education & Behavior Analysis Faculty

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-christina-noel|Dr. Christina R. Noel]] | Professor & Director, CEC | CEC / GRH 1082 | christina.noel@wku.edu | (270) 745-8989 |
| [[people/dr-ellen-casale|Dr. Ellen G. Casale]] | Assistant Professor, BCBA | GRH 1087 | ellen.casale@wku.edu | (270) 745-4118 |
| [[people/dr-shannon-pardue|Dr. Shannon D. Pardue]] | Assistant Professor | GRH 1088 | shannon.pardue@wku.edu | (270) 745-5414 |
| [[people/dr-brooke-royalty|Dr. Jordan Brooke Royalty]] | Assistant Professor | GRH 1084 | brooke.royalty@wku.edu | (270) 745-5414 |
| [[people/dr-leslee-bailey-tarbett|Dr. Leslee Bailey Tarbett]] | Assistant Professor | GRH 1084 | leslee.tarbett@wku.edu | (270) 745-4444 |
| [[people/charley-jo-vaughn|Charley Jo Vaughn]] | Visiting Assistant Professor | GRH 1085 | charley.vaughn@wku.edu | (270) 745-5414 |
| [[people/bailey-payne|Bailey A. Payne]] | Instructor II (Psychology / ABA) | GRH 1085 | bailey.payne@wku.edu | (270) 745-5414 |

---

## Interdisciplinary Early Childhood Education (IECE)

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-trudy-little|Dr. Trudy M. Little]] | Assistant Professor, BCBA | GRH 1084 | trudy.little@wku.edu | (270) 745-4444 |

---

## Literacy & Reading Education Faculty

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-jeremy-logsdon|Dr. Jeremy R. Logsdon]] | Assistant Professor; Director, Center for Literacy | GRH 1083B | jeremy.logsdon@wku.edu | (270) 745-4309 |
| [[people/dr-nancy-hulan|Dr. Nancy F. Hulan]] | Professor | GRH 1083A | nancy.hulan@wku.edu | (270) 745-4324 |
| [[people/dr-kandy-smith|Dr. Kandy C. Smith]] | Associate Professor | GRH 1083 | kandy.smith@wku.edu | (270) 745-4433 |
| [[people/sally-tooley|Sally H. Tooley]] | Instructor | GRH 1085 | sally.tooley@wku.edu | (270) 745-5414 |

---

## Libraries, Informatics, & Technology in Education (LITE)

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-andrea-paganelli|Dr. Andrea Paganelli]] | Associate Professor | GRH 1089 | andrea.paganelli@wku.edu | (270) 745-4420 |
| [[people/mr-josiah-super|Dr. Daniel Josiah Super]] | Specialist / Associate Professor | GRH 1033 | josiah.super@wku.edu | (270) 745-2819 |
| [[people/christina-heady|Christina Heady]] | Specialist | GRH 1033 | christina.heady@wku.edu | (270) 745-2819 |

---

## Gifted Education Leadership

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-julia-link-roberts|Dr. Julia Link Roberts]] | Mahurin Professor & Executive Director | GRH 1019 | julia.roberts@wku.edu | (270) 745-6323 |

---

## SKyTeach STEM Faculty & Master Teachers

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-martha-day|Dr. Martha M. Day]] | Professor & Education Co-Director | KTH 1011C | martha.day@wku.edu | (270) 745-3900 |
| [[people/melanie-owens|Melanie D. Owens]] | SKyTeach Master Teacher / Instructor I | KTH 1011 | melanie.owens@wku.edu | (270) 745-3900 |
| [[people/emily-perkins|Emily S. Perkins]] | SKyTeach Master Teacher / Instructor I | KTH 1011 | emily.perkins@wku.edu | (270) 745-3900 |
| [[people/mr-rico-tyler|Mr. Rico Tyler]] | Master Teacher / Transitional Retiree | KTH 1011 | rico.tyler@wku.edu | (270) 745-3900 |

---

## Educational Research & Grant Leadership

| Name | Title | Office | Email | Phone |
| :--- | :--- | :--- | :--- | :--- |
| [[people/dr-renming-liu|Dr. Renming Liu]] | Assistant Professor (Psychology & Research) | GRH 1088 | renming.liu@wku.edu | (270) 745-5414 |
| [[people/dr-angela-dyer-nagel|Dr. Angela D. Dyer-Nagel]] | Research Assistant Professor | GRH 1013 | angela.nagel@wku.edu | (270) 745-4054 |

---

## Backlinks / Related Documents
*   [[INDEX]]: Central Knowledge Base Index & Map of Content
*   [[overview/leadership-and-governance]]: STE Leadership and Governance Overview
*   [[overview/contact-and-facilities]]: Gary A. Ransdell Hall Building Directory
*   [[programs/INDEX]]: Academic Degrees and Programs Matrix
""")

    print("All faculty and staff files generated successfully.")

if __name__ == "__main__":
    generate_people()
