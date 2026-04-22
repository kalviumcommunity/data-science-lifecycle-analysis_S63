"""Milestone 4.19: Passing data into functions and returning results.

Project: At-Risk Student Detection System
Focus: clean input-output function pipeline
"""


def evaluate_risk(marks: float, attendance: float) -> str:
    """Decision engine: accept inputs, return classification."""
    if marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
        return "Invalid Data"
    if marks < 50 or attendance < 75:
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
    valid = 0
    at_risk = 0
    safe = 0
    invalid = 0

    for result in results:
        status = str(result["status"])
        if status == "Invalid Data":
            invalid += 1
            continue
        valid += 1
        if status == "At Risk":
            at_risk += 1
        elif status == "Safe":
            safe += 1

    return {"valid": valid, "at_risk": at_risk, "safe": safe, "invalid": invalid}


def main() -> None:
    students = [
        {"name": "Aisha", "marks": 88, "attendance": 91},
        {"name": "Rohit", "marks": 49, "attendance": 79},
        {"name": "Neha", "marks": 72, "attendance": 70},
        {"name": "Karan", "marks": 83, "attendance": 86},
        {"name": "Isha", "marks": 95, "attendance": 98},
        {"name": "BadRow", "marks": 130, "attendance": 55},
    ]

    # Pipeline: evaluate -> build result -> format/aggregate in main flow
    results: list[dict[str, float | str]] = []
    for student in students:
        marks = float(student["marks"])
        attendance = float(student["attendance"])

        # Step 3/4: pass parameters, capture returned value.
        status = evaluate_risk(marks, attendance)
        result = build_result_record(student, status)
        results.append(result)

    print("=== At-Risk Student Detection (Return Pipeline) ===")
    for result in results:
        # Step 8: chain output of one function into another.
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
