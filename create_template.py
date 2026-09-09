import sys
import subprocess

try:
    from docx import Document
except ImportError:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'python-docx'])
    from docx import Document

doc = Document()

# 1. Title
doc.add_heading('1. Title', level=1)
doc.add_paragraph('Clinic Queue and Token Management System')

# 2. Abstract
doc.add_heading('2. Abstract', level=1)
doc.add_paragraph("Managing patient flow in outpatient clinics has always been difficult, and long wait times often lead to frustrated patients and a less efficient clinic. To help solve this problem, many healthcare facilities are switching to digital Clinic Queue and Token Management Systems (CQTMS). In this review, we look at three recent studies to see how these modern queue systems impact both the clinic’s daily operations and the patient’s experience. Specifically, the research covers web-based queue tracking, using AI to predict and cut down wait times, and strategies to improve flow in clinics that don't rely on appointments.")
doc.add_paragraph("The studies clearly show that moving from manual, paper-based lines to automated token systems makes a major difference in how smoothly a clinic runs. When clinics use web-based check-ins and AI to forecast busy periods, they can actually reduce wait times by routing patients more efficiently through registration, doctor visits, and the pharmacy.")
doc.add_paragraph("Additionally, these systems are better at handling high volumes of walk-in patients because they can prioritize urgent cases rather than sticking to a strict first-come, first-served rule. The research also highlights a big improvement for patients: when they can see their place in line in real-time, the wait feels shorter and they are much less anxious. In the end, setting up an integrated Clinic Queue and Token Management System is a smart step forward for healthcare centers. By keeping patient flow moving, using smart scheduling tools, and being transparent about wait times, clinics can operate more effectively and create a better, more patient-focused environment.")

doc.add_heading('Key References Evaluated', level=2)
doc.add_paragraph("1. Design and Evaluation of QKlinik: A Web-Based Queue Management System for Outpatient Clinics.")
doc.add_paragraph("2. Using artificial intelligence to reduce queuing time and improve satisfaction in pediatric outpatient service.")
doc.add_paragraph("3. An optimized queue management system to improve patient flow in the absence of appointment system.")

# 3. Introduction
doc.add_heading('3. Introduction', level=1)
doc.add_paragraph('[Implement your introduction here]')

# 4. Problem Statement
doc.add_heading('4. Problem Statement', level=1)
doc.add_paragraph('[Implement your problem statement here]')

# 5. Objectives
doc.add_heading('5. Objectives', level=1)
doc.add_paragraph('[Implement your objectives here]')

# 6. System Design (Implement it)
doc.add_heading('6. System Design (Implement it)', level=1)
doc.add_paragraph('• ERD (Entity Relationship Diagram)')
doc.add_paragraph('• DFD (Data Flow Diagram)')
doc.add_paragraph('  o Context Diagram / Level 0')
doc.add_paragraph('  o Level 1 DFD')

doc.save('Clinic_Queue_Project_Report_Template.docx')
print("Successfully created Clinic_Queue_Project_Report_Template.docx")
