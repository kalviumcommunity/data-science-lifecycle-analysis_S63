"""Milestone 4.18: Defining and calling functions in project context.

Project: At-Risk Student Detection System
Focus: replace repetitive code with reusable functions
"""


def check_risk(marks: float, attendance: float) -> str:
    """Core decision engine: classify student as At Risk or Safe."""
    if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
        return "Invalid Data"
    if marks < 50 or attendance < 75:
        return "At Risk"
    return "Safe"


def build_student_output(name: str, marks: float, attendance: float, status: str) -> str:
    """Generate educator-friendly output line for one student."""
    return (
        f"Student: {name:<10} | Marks: {marks:>5.1f} | "
        f"Attendance: {attendance:>5.1f}% | Status: {status}"
    )


def process_students(students: list[dict[str, float | str]]) -> dict[str, int]:
    """Loop through students, call functions, and print structured report."""
    total_valid = 0
    at_risk_count = 0

    print("=== At-Risk Student Detection (Function Engine) ===")
    for student in students:
        name = str(student["name"])
        marks = float(student["marks"])
        attendance = float(student["attendance"])

        # Function call reused for each student record.
        status = check_risk(marks, attendance)

        if status == "Invalid Data":
            print(build_student_output(name, marks, attendance, status))
            continue

        total_valid += 1
        if status == "At Risk":
            at_risk_count += 1

        # Separate output function keeps display logic clean.
        print(build_student_output(name, marks, attendance, status))

    print("-" * 84)
    print(f"Total valid students: {total_valid}")
    print(f"At-risk students   : {at_risk_count}")
    return {"total_valid": total_valid, "at_risk": at_risk_count}


def scope_demo() -> None:
    """Show function scope: local variables stay inside functions."""
    internal_note = "This variable is local to scope_demo()"
    print("\nScope Demo:", internal_note)
    print("Local variables do not leak into global project state.")


def main() -> None:
    students = [
        {"name": "Aisha", "marks": 88, "attendance": 92},
        {"name": "Rohit", "marks": 44, "attendance": 81},
        {"name": "Neha", "marks": 63, "attendance": 69},
        {"name": "Karan", "marks": 77, "attendance": 84},
        {"name": "Isha", "marks": 95, "attendance": 98},
        {"name": "BadRow", "marks": 120, "attendance": 55},
    ]

    summary = process_students(students)
    scope_demo()

    print("\nEngineering Reflection:")
    print("- check_risk() isolates decision logic")
    print("- build_student_output() isolates presentation")
    print("- process_students() orchestrates flow")
    print(f"- Current at-risk ratio: {summary['at_risk']}/{summary['total_valid']}")


if __name__ == "__main__":
    main()
