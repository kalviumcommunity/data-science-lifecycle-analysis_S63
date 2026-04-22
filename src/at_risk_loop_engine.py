"""Milestone 4.17: for loops and while loops in project context.

Project: At-Risk Student Detection System
- for loop: process all student records
- while loop: controlled repeated monitoring cycles
- break/continue: robust control flow
"""


def risk_status(marks: float, attendance: float) -> str:
    """Classify student as at-risk or safe using project thresholds."""
    marks_threshold = 50
    attendance_threshold = 75
    if marks < marks_threshold or attendance < attendance_threshold:
        return "At Risk"
    return "Safe"


def run_detection_cycle(students: list[dict[str, float | str]]) -> dict[str, int]:
    """Process all students once and return aggregate counts."""
    total_students = 0
    at_risk_count = 0

    print("\n=== Detection Cycle Report ===")
    print(f"{'Name':<12} {'Marks':>6} {'Attend%':>8} {'Status':>12}")
    print("-" * 44)

    # for loop: automatically process all student records.
    for student in students:
        name = str(student["name"])
        marks = float(student["marks"])
        attendance = float(student["attendance"])

        # continue: skip invalid rows safely.
        if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
            print(f"{name:<12} {'-':>6} {'-':>8} {'Skipped':>12}")
            continue

        status = risk_status(marks, attendance)
        total_students += 1
        if status == "At Risk":
            at_risk_count += 1

        print(f"{name:<12} {marks:>6.1f} {attendance:>8.1f} {status:>12}")

    print("-" * 44)
    print(f"Total valid students : {total_students}")
    print(f"At-risk students     : {at_risk_count}")
    return {"total": total_students, "at_risk": at_risk_count}


def monitoring_loop(students: list[dict[str, float | str]]) -> None:
    """while loop for repeated execution with explicit exit control."""
    cycle = 1
    max_cycles = 2

    # while loop: repeat while condition remains true.
    while True:
        print(f"\n[Monitoring Cycle {cycle}]")
        summary = run_detection_cycle(students)

        if summary["total"] == 0:
            print("No valid data to evaluate. Exiting early.")
            break

        if cycle >= max_cycles:
            print("Reached planned monitoring cycles. Exiting loop.")
            break

        cycle += 1


def main() -> None:
    students = [
        {"name": "Aisha", "marks": 88, "attendance": 92},
        {"name": "Rohit", "marks": 47, "attendance": 81},
        {"name": "Neha", "marks": 62, "attendance": 68},
        {"name": "Karan", "marks": 35, "attendance": 55},
        {"name": "Isha", "marks": 93, "attendance": 97},
        {"name": "BadRow", "marks": 140, "attendance": 60},  # invalid -> continue
    ]

    print("=== At-Risk Student Detection System ===")
    print("Loop engine demo: for + while + break + continue")
    monitoring_loop(students)

    print("\nEngineering Reflection:")
    print("- for loop scales naturally from 5 to 1000+ records")
    print("- while loop handles repeated monitoring cycles")
    print("- break prevents infinite loops")
    print("- continue skips bad rows without stopping pipeline")


if __name__ == "__main__":
    main()
