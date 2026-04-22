"""Milestone 4.16: Conditional statements mini project.

Student Performance Decision System
- demonstrates if / elif / else
- demonstrates and / or / not
- demonstrates validation and debugging mindset
"""


def classify_student(marks: float, attendance: float) -> str:
    """Return performance category based on marks and attendance."""
    # Edge case validation for real-world messy inputs.
    if marks < 0 or marks > 100:
        return "Invalid marks input"
    if attendance < 0 or attendance > 100:
        return "Invalid attendance input"

    # Separate fail condition requested in milestone.
    if marks < 35:
        return "Fail"

    # if-elif-else grading logic (order matters).
    if marks >= 90:
        return "Excellent"
    elif marks >= 75:
        # Logical operator demo: both conditions must be true.
        if marks >= 75 and attendance > 80:
            return "Good (High attendance bonus)"
        return "Good"
    elif marks >= 50:
        # Logical operator demo: one of the conditions can be true.
        if attendance < 60 or marks < 55:
            return "Average (Needs consistency)"
        return "Average"
    else:
        # This else captures 35 to 49 after fail check.
        return "Needs Improvement"


def attendance_flag(attendance: float) -> str:
    """Show use of `not` for condition inversion."""
    is_regular = attendance >= 75
    if not is_regular:
        return "Attendance Alert"
    return "Attendance OK"


def print_result(student_name: str, marks: float, attendance: float) -> None:
    """Print a clean, structured output line for one student."""
    category = classify_student(marks, attendance)
    attendance_status = attendance_flag(attendance) if "Invalid" not in category else "-"

    print(f"Student    : {student_name}")
    print(f"Marks      : {marks}")
    print(f"Attendance : {attendance}")
    print(f"Category   : {category}")
    print(f"Flag       : {attendance_status}")
    print("-" * 36)


def main() -> None:
    # Includes normal and edge-case records for complete flow testing.
    student_records = [
        {"name": "Aisha", "marks": 93, "attendance": 88},
        {"name": "Rohit", "marks": 79, "attendance": 84},
        {"name": "Neha", "marks": 52, "attendance": 58},
        {"name": "Karan", "marks": 42, "attendance": 77},
        {"name": "Isha", "marks": 31, "attendance": 82},
        {"name": "TestInvalid", "marks": 108, "attendance": 70},
    ]

    print("=== Student Performance Decision System ===")
    print("Conditional logic demo: if / elif / else / and / or / not")
    print("-" * 36)
    for record in student_records:
        print_result(record["name"], record["marks"], record["attendance"])

    print("Debug Tip: If result looks wrong, print values and check condition order.")


if __name__ == "__main__":
    main()
