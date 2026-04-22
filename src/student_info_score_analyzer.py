"""Milestone 4.14: Numeric and string data types mini project.

Student Info & Score Analyzer
- demonstrates integers, floats, strings
- demonstrates type conversion and type checking
"""


def main() -> None:
    # Step 1: Numeric basics (int and float)
    maths_marks = 82  # int
    science_marks = 76  # int
    english_marks = 79.5  # float

    total_marks = maths_marks + science_marks + english_marks
    average_marks = total_marks / 3

    # Step 2: String basics
    student_name = "Rahul"
    course_label = "Class 10"

    # Step 3/4: Safe type conversion for mixed output
    summary_line = (
        "Student "
        + student_name
        + " from "
        + course_label
        + " scored an average of "
        + str(round(average_marks, 2))
    )

    # Step 5: Type checking
    print("=== Type Check ===")
    print("student_name:", type(student_name).__name__)
    print("maths_marks:", type(maths_marks).__name__)
    print("english_marks:", type(english_marks).__name__)
    print("average_marks:", type(average_marks).__name__)

    # Step 6/7: Clean project-style output
    print("\n=== Student Info & Score Analyzer ===")
    print(f"Student Name : {student_name}")
    print(f"Course       : {course_label}")
    print(f"Maths Marks  : {maths_marks}")
    print(f"Science Marks: {science_marks}")
    print(f"English Marks: {english_marks}")
    print(f"Total Marks  : {total_marks}")
    print(f"Average Marks: {average_marks:.2f}")
    print(summary_line)

    # Step 8: Error awareness simulation (text to number conversion)
    marks_from_form = "88.5"  # often arrives as text
    converted_marks = float(marks_from_form)
    print("\nConverted text marks to number:", converted_marks)


if __name__ == "__main__":
    main()
