"""Milestone 4.21: Structured At-Risk Student Detection pipeline.

Project: At-Risk Student Detection System
Focus: clear sections, grouped functions, clean main execution.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
from typing import TypedDict


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
# Thresholds are centralized so that policy changes need exactly one edit.
PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75
VALID_SCORE_RANGE = (0, 100)

STATUS_AT_RISK = "At Risk"
STATUS_SAFE = "Safe"
STATUS_INVALID = "Invalid Data"

REPORT_DIVIDER_WIDTH = 84
REPORT_TITLE = "=== At-Risk Student Detection (Structured Pipeline) ==="


# ---------------------------------------------------------------------------
# Section 3: Type Definitions
# ---------------------------------------------------------------------------
class StudentRecord(TypedDict):
    name: str
    marks: float
    attendance: float


class ResultRecord(TypedDict):
    name: str
    marks: float
    attendance: float
    status: str


class SummaryMetrics(TypedDict):
    valid: int
    at_risk: int
    safe: int
    invalid: int


# ---------------------------------------------------------------------------
# Section 4: Data Setup
# ---------------------------------------------------------------------------
def load_student_records() -> list[StudentRecord]:
    """Return the sample dataset used by the detection system."""
    return [
        {"name": "Aisha", "marks": 88, "attendance": 91},
        {"name": "Rohit", "marks": 49, "attendance": 79},
        {"name": "Neha", "marks": 72, "attendance": 70},
        {"name": "Karan", "marks": 83, "attendance": 86},
        {"name": "Isha", "marks": 95, "attendance": 98},
        {"name": "InvalidRecordDemo", "marks": 130, "attendance": 55},
    ]


# ---------------------------------------------------------------------------
# Section 5: Risk Evaluation Functions
# ---------------------------------------------------------------------------
def is_score_valid(score: float) -> bool:
    """Return True when score is within the allowed numeric range."""
    minimum, maximum = VALID_SCORE_RANGE
    return minimum <= score <= maximum


def evaluate_student_risk(marks: float, attendance_percentage: float) -> str:
    """Return risk classification using marks and attendance thresholds."""
    if not is_score_valid(marks) or not is_score_valid(attendance_percentage):
        return STATUS_INVALID
    if marks < PASSING_MARKS_THRESHOLD or attendance_percentage < MIN_ATTENDANCE_PERCENTAGE:
        return STATUS_AT_RISK
    return STATUS_SAFE


def build_result_record(student: StudentRecord, risk_status: str) -> ResultRecord:
    """Create a normalized result record from a raw student plus its status."""
    return {
        "name": str(student["name"]),
        "marks": float(student["marks"]),
        "attendance": float(student["attendance"]),
        "status": risk_status,
    }


def evaluate_all_students(student_records: list[StudentRecord]) -> list[ResultRecord]:
    """Run risk evaluation across every student and return result records."""
    results: list[ResultRecord] = []
    for student in student_records:
        marks = float(student["marks"])
        attendance_percentage = float(student["attendance"])
        risk_status = evaluate_student_risk(marks, attendance_percentage)
        results.append(build_result_record(student, risk_status))
    return results


# ---------------------------------------------------------------------------
# Section 6: Reporting Functions
# ---------------------------------------------------------------------------
def format_result_line(result: ResultRecord) -> str:
    """Convert a result record into an educator-friendly output line."""
    return (
        f"Student: {result['name']:<18} | Marks: {result['marks']:>5.1f} | "
        f"Attendance: {result['attendance']:>5.1f}% | Status: {result['status']}"
    )


def summarize_results(results: list[ResultRecord]) -> SummaryMetrics:
    """Return aggregate metrics computed from result records."""
    summary: SummaryMetrics = {"valid": 0, "at_risk": 0, "safe": 0, "invalid": 0}
    for result in results:
        risk_status = result["status"]
        if risk_status == STATUS_INVALID:
            summary["invalid"] += 1
            continue
        summary["valid"] += 1
        if risk_status == STATUS_AT_RISK:
            summary["at_risk"] += 1
        elif risk_status == STATUS_SAFE:
            summary["safe"] += 1
    return summary


def print_report(results: list[ResultRecord], summary: SummaryMetrics) -> None:
    """Print the full detection report using formatted lines and summary."""
    print(REPORT_TITLE)
    for result in results:
        print(format_result_line(result))

    print("-" * REPORT_DIVIDER_WIDTH)
    print(f"Valid students : {summary['valid']}")
    print(f"At-risk count  : {summary['at_risk']}")
    print(f"Safe count     : {summary['safe']}")
    print(f"Invalid rows   : {summary['invalid']}")


# ---------------------------------------------------------------------------
# Section 7: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_records = load_student_records()
    results = evaluate_all_students(student_records)
    summary = summarize_results(results)
    print_report(results, summary)


if __name__ == "__main__":
    main()
