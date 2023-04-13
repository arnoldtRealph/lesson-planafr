import streamlit as st
import os
import io
import docx

# Set page title and icon
st.set_page_config(page_title="Lesson Plan Creator", page_icon=":books:")

# Create input fields
st.write("HOЁRSKOOL SAUL DAMON")
st.write("LESBEPLANNER")
st.write("Please fill out the following fields to create a new lesson plan:")
st.write("")
subject = st.text_input("Subject")
lesson_title = st.text_input("Lesson Title")
grade = st.selectbox("Grade", ["Grade 9", "Grade 10", "Grade 11", "Grade 12"])
lesson_date = st.date_input("Lesson Date")
lesson_objective = st.text_area("Lesson Objective")
lesson_activities = st.text_area("Lesson Activities")
materials_needed = st.text_area("Materials Needed")
homework = st.text_area("Homework")
notes = st.text_area("Notes")
teacher_name = st.text_input("Teacher Name")
teacher_surname = st.text_input("Teacher Surname")
st.write("")

# Create save button
if st.button("Create Lesson Plan"):
    # Create a new Word document
    document = docx.Document()
    # Add input values to the document
    document.add_heading(subject.upper(), level=0)
    document.add_paragraph("")
    document.add_paragraph("Lesson Title: " + lesson_title)
    document.add_paragraph("Grade: " + grade)
    document.add_paragraph("Lesson Date: " + str(lesson_date))
    document.add_paragraph("")
    document.add_heading("Lesson Objective", level=1)
    document.add_paragraph(lesson_objective)
    document.add_heading("Lesson Activities", level=1)
    document.add_paragraph(lesson_activities)
    document.add_heading("Materials Needed", level=1)
    document.add_paragraph(materials_needed)
    document.add_heading("Homework", level=1)
    document.add_paragraph(homework)
    document.add_heading("Notes", level=1)
    document.add_paragraph(notes)
    document.add_paragraph("")
    document.add_paragraph("Teacher Name: " + teacher_name)
    document.add_paragraph("Teacher Surname: " + teacher_surname)
    document.add_paragraph("Teacher Signature: ")

    # Save document to BytesIO object
    with io.BytesIO() as output:
        document.save(output)
        output.seek(0)
        # Create download button
        st.download_button(
            label="Download Lesson Plan",
            data=output,
            file_name="lesson_plan.docx",
            mime="application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        )
        st.success("Your lesson plan has been created. Click the download button to save the file.")
