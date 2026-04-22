"""Milestone 4.13: First Python script for data analysis.

This script analyzes simple student marks data and prints:
- class average
- highest scorer
- lowest scorer
"""

from statistics import mean


def analyze_student_performance(students: list[dict[str, int | str]]) -> dict[str, object]:
    """Compute summary metrics from student marks."""
    scores = [int(student["marks"]) for student in students]

    average_marks = mean(scores)
    highest_scorer = max(students, key=lambda student: int(student["marks"]))
    lowest_scorer = min(students, key=lambda student: int(student["marks"]))

    return {
        "average": average_marks,
        "highest": highest_scorer,
        "lowest": lowest_scorer,
    }


def print_report(summary: dict[str, object]) -> None:
    """Print analysis results in a clean, readable structure."""
    highest = summary["highest"]
    lowest = summary["lowest"]

    print("=== Student Performance Analyzer ===")
    print(f"Average Marks : {summary['average']:.2f}")
    print(f"Highest Scorer: {highest['name']} ({highest['marks']})")
    print(f"Lowest Scorer : {lowest['name']} ({lowest['marks']})")


def main() -> None:
    """Script entrypoint."""
    students = [
        {"name": "Aisha", "marks": 85},
        {"name": "Rohit", "marks": 92},
        {"name": "Neha", "marks": 76},
        {"name": "Karan", "marks": 88},
        {"name": "Isha", "marks": 95},
    ]

    summary = analyze_student_performance(students)
    print_report(summary)


if __name__ == "__main__":
    main()
