import streamlit as st
import docx
import os
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.shared import Pt
from docx.oxml.ns import qn

# Set up the document style
document = docx.Document()
document.styles['Normal'].font.name = 'Arial'
document.styles['Normal']._element.rPr.rFonts.set(qn('w:eastAsia'), 'Arial')
document.styles['Normal'].font.size = Pt(12)
document.styles['Heading 1'].font.bold = True
document.styles['Heading 1'].font.size = Pt(16)
document.styles['Heading 2'].font.bold = True
document.styles['Heading 2'].font.size = Pt(14)
document.styles['Heading 3'].font.bold = True
document.styles['Heading 3'].font.size = Pt(12)

st.title("HOЁRSKOOL SAUL DAMON")
st.header("LESBEPLANNER")
# Define the grade levels
grade_levels = ['GRAAD 9', 'GRAAD 10', 'GRAAD 11', 'GRAAD 12']

# Set up the sidebar
st.sidebar.title("DAAGLIKE BEPLANNER")
selected_grade = st.sidebar.selectbox("KIES N GRAAD", grade_levels)

# Define the lesson plan inputs
subject_name = st.text_input("VAK")
lesson_title = st.text_input("LES TITEL")
lesson_date = st.date_input("LES DATUM")
lesson_objective = st.text_input("LES DOELWIT")
lesson_activities = st.text_area("LEERDER AKTIWITEITE")
lesson_materials = st.text_area("MATERIAAL BENODIG")
lesson_homework = st.text_area("HUISWERK")
lesson_notes = st.text_area("NOTAS")

st.write("Designed by Mr. A.R Visagie @ Saul Damon High School")
# Set up the save button
if st.button("Save"):
    # Check if the file already exists
    file_path = os.path.expanduser(f"~/Desktop/{lesson_title}.docx")
    while os.path.exists(file_path):
        st.warning(f"A file with the name '{lesson_title}.docx' already exists on your desktop. Please choose a different name.")
        lesson_title = st.text_input("Lesson Title")
        file_path = os.path.expanduser(f"~/Desktop/{lesson_title}.docx")
        
    # Add the lesson plan to the document
    p = document.add_paragraph(selected_grade, style='Heading 1')
    p = document.add_paragraph()
    p.add_run(f"Subject: ").bold = True
    p.add_run(f"{subject_name}").bold = True
    p = document.add_paragraph(lesson_title, style='Heading 1')
    
    # Add the lesson date
    date_str = lesson_date.strftime('%A, %B %d, %Y')
    document.add_paragraph(date_str, style='Heading 2')
    
    # Add the lesson objective, activities, materials, and homework
    document.add_heading("Objective", level=2)
    document.add_paragraph(lesson_objective)
    
    document.add_heading("Activities", level=2)
    document.add_paragraph(lesson_activities)
    
    document.add_heading("Materials", level=2)
    document.add_paragraph(lesson_materials)
    
    document.add_heading("Homework", level=2)
    document.add_paragraph(lesson_homework)
    
    # Add the notes
    document.add_heading("Notes", level=2)
    document.add_paragraph(lesson_notes)
    
    # Add the teacher's signature line
    document.add_paragraph("")
    document.add_paragraph("")
    document.add_paragraph("")
    p = document.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    p.add_run("___________________________").bold = True
    p.add_run("\nTeacher's Signature").bold = True
    
    # Save the document
    document.save(file_path)
    st.success("File saved successfully!")
