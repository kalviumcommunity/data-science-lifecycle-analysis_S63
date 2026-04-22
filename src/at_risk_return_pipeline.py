"""Milestone 4.19: Passing data into functions and returning results.

Project: At-Risk Student Detection System
Focus: clean input-output function pipeline
"""


def evaluate_student_risk(marks: float, attendance_percentage: float) -> str:
    """Return risk classification using marks and attendance thresholds."""
    if marks < 0 or marks > 100 or attendance_percentage < 0 or attendance_percentage > 100:
        return "Invalid Data"
    if marks < 50 or attendance_percentage < 75:
        return "At Risk"
    return "Safe"


def build_result_record(student: dict[str, float | str], risk_status: str) -> dict[str, float | str]:
    """Create normalized result record from raw student + risk result."""
    return {
        "name": str(student["name"]),
        "marks": float(student["marks"]),
        "attendance": float(student["attendance"]),
        "status": risk_status,
    }


def format_result_line(result: dict[str, float | str]) -> str:
    """Convert result record into educator-friendly output text."""
    return (
        f"Student: {result['name']:<10} | Marks: {result['marks']:>5.1f} | "
        f"Attendance: {result['attendance']:>5.1f}% | Status: {result['status']}"
    )


def summarize_results(results: list[dict[str, float | str]]) -> dict[str, int]:
    """Return aggregate project metrics from result records."""
    valid_student_count = 0
    at_risk_student_count = 0
    safe_student_count = 0
    invalid_record_count = 0

    for result in results:
        risk_status = str(result["status"])
        if risk_status == "Invalid Data":
            invalid_record_count += 1
            continue
        valid_student_count += 1
        if risk_status == "At Risk":
            at_risk_student_count += 1
        elif risk_status == "Safe":
            safe_student_count += 1

    return {
        "valid": valid_student_count,
        "at_risk": at_risk_student_count,
        "safe": safe_student_count,
        "invalid": invalid_record_count,
    }


def main() -> None:
    student_records = [
        {"name": "Aisha", "marks": 88, "attendance": 91},
        {"name": "Rohit", "marks": 49, "attendance": 79},
        {"name": "Neha", "marks": 72, "attendance": 70},
        {"name": "Karan", "marks": 83, "attendance": 86},
        {"name": "Isha", "marks": 95, "attendance": 98},
        {"name": "InvalidRecordDemo", "marks": 130, "attendance": 55},
    ]

    # Build results first, then format output and aggregate metrics.
    results: list[dict[str, float | str]] = []
    for student in student_records:
        marks = float(student["marks"])
        attendance_percentage = float(student["attendance"])

        risk_status = evaluate_student_risk(marks, attendance_percentage)
        result = build_result_record(student, risk_status)
        results.append(result)

    print("=== At-Risk Student Detection (Return Pipeline) ===")
    for result in results:
        print(format_result_line(result))

    summary = summarize_results(results)
    print("-" * 84)
    print(f"Valid students : {summary['valid']}")
    print(f"At-risk count  : {summary['at_risk']}")
    print(f"Safe count     : {summary['safe']}")
    print(f"Invalid rows   : {summary['invalid']}")

    print("\nDeveloper Note:")
    print("- Functions now return values, so logic is reusable and testable.")
    print("- Main loop composes outputs into a clear project data pipeline.")


if __name__ == "__main__":
    main()
