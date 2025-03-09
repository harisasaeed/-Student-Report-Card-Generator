
import streamlit as st
import pandas as pd

# Function to calculate grade and add emoji
def calculate_grade(percentage):
    if percentage < 40:
        return "F ❌"
    elif percentage < 50:
        return "C 🟠"
    elif percentage < 60:
        return "B 🟡"
    elif percentage < 70:
        return "A 🟢"
    else:
        return "A+ ⭐"

# Initialize session state for student data if not already present
if "student_data" not in st.session_state:
    st.session_state.student_data = []

# Main Streamlit application
def main():
    st.title("📘 Student Report Card Generator")

    # Input student details
    student_name = st.text_input("Enter Student Name:")
    roll_number = st.text_input("Enter Roll Number:")

    math_marks = st.number_input("Math Marks:", min_value=0, max_value=100)
    physics_marks = st.number_input("Physics Marks:", min_value=0, max_value=100)
    urdu_marks = st.number_input("Urdu Marks:", min_value=0, max_value=100)
    english_marks = st.number_input("English Marks:", min_value=0, max_value=100)
    computer_marks = st.number_input("Computer Marks:", min_value=0, max_value=100)

    if st.button("📩 Submit Student Info"):
        if not student_name or not roll_number:
            st.error("⚠️ Please enter both student name and roll number.")
        else:
            total_marks = math_marks + physics_marks + urdu_marks + english_marks + computer_marks
            percentage = (total_marks / 500) * 100
            grade = calculate_grade(percentage)

            # Store student information in session state
            st.session_state.student_data.append({
                "name": student_name,
                "roll_number": roll_number,
                "marks": {
                    "Math": math_marks,
                    "Physics": physics_marks,
                    "Urdu": urdu_marks,
                    "English": english_marks,
                    "Computer": computer_marks
                },
                "total": total_marks,
                "percentage": percentage,
                "grade": grade,
            })

            st.success(f"✅ Record of {student_name} inserted successfully!")

    # Display report cards if data exists
    if st.session_state.student_data:
        st.markdown("## 🏆 Generated Report Cards")
        for student in st.session_state.student_data:
            st.markdown(f"### 📜 Report Card for **{student['name']}** (Roll No: **{student['roll_number']}**)")

            # Create DataFrame for table-like display
            marks_df = pd.DataFrame(student["marks"].items(), columns=["Subject", "Marks"])
            st.table(marks_df)

            st.markdown(f"""
            **🎯 Total Marks:** `{student['total']}/500`  
            **📊 Percentage:** `{student['percentage']:.2f}%`  
            **🏅 Final Grade:** `{student['grade']}`
            """)
            st.divider()

    # Reset data
    if st.button("🔄 Reset Data"):
        st.session_state.student_data = []
        st.success("♻️ Data has been reset successfully!")

if __name__ == "__main__":
    main()
