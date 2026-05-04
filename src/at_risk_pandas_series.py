"""Milestone 4.27: Creating Pandas Series from Lists and Arrays.

Project: At-Risk Student Detection System
Focus: attach meaningful labels (student names) to numeric data using
       pandas Series, then use Series for clear, named risk reporting.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
import numpy as np
import pandas as pd


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75


# ---------------------------------------------------------------------------
# Section 3: Project Data
# ---------------------------------------------------------------------------
def load_student_data() -> dict[str, list]:
    return {
        "names": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        "marks": [88, 49, 72, 83, 95],
        "attendance": [91, 79, 70, 86, 98],
    }


# ---------------------------------------------------------------------------
# Section 4: Create Series from List and NumPy Array
# ---------------------------------------------------------------------------
def make_marks_series_from_list(student_data: dict[str, list]) -> pd.Series:
    """Series built directly from a Python list with default integer index."""
    return pd.Series(student_data["marks"], name="marks")


def make_marks_series_with_names(student_data: dict[str, list]) -> pd.Series:
    """Series built from a Python list using student names as the index."""
    return pd.Series(
        student_data["marks"],
        index=student_data["names"],
        name="marks",
    )


def make_attendance_series_from_array(student_data: dict[str, list]) -> pd.Series:
    """Series built from a NumPy array with student names as the index."""
    attendance_array = np.array(student_data["attendance"], dtype=float)
    return pd.Series(
        attendance_array,
        index=student_data["names"],
        name="attendance",
    )


# ---------------------------------------------------------------------------
# Section 5: Inspection Helpers
# ---------------------------------------------------------------------------
def inspect_series(label: str, series: pd.Series) -> None:
    print(f"\n--- {label} ---")
    print(series)
    print(f"name   : {series.name}")
    print(f"dtype  : {series.dtype}")
    print(f"index  : {list(series.index)}")
    print(f"values : {series.values}")


# ---------------------------------------------------------------------------
# Section 6: Label-Based Access
# ---------------------------------------------------------------------------
def show_label_access(marks_series: pd.Series) -> None:
    print("\n--- Label-Based Access ---")
    print(f"marks_series['Aisha'] = {marks_series['Aisha']}")
    print(f"marks_series['Rohit'] = {marks_series['Rohit']}")
    print("Selecting multiple students by label:")
    print(marks_series[["Aisha", "Neha", "Isha"]])


# ---------------------------------------------------------------------------
# Section 7: Array vs Series Comparison
# ---------------------------------------------------------------------------
def array_vs_series_demo(student_data: dict[str, list]) -> None:
    print("\n--- Array vs Series ---")
    marks_array = np.array(student_data["marks"], dtype=float)
    print("NumPy array (positional, no labels):")
    print(marks_array)

    marks_series = pd.Series(marks_array, index=student_data["names"], name="marks")
    print("\nPandas Series (labeled):")
    print(marks_series)


# ---------------------------------------------------------------------------
# Section 8: Project Risk Logic Using Series
# ---------------------------------------------------------------------------
def detect_at_risk_with_series(
    marks_series: pd.Series,
    attendance_series: pd.Series,
) -> pd.Series:
    """Vectorized at-risk detection on aligned Series; preserves student names."""
    risk_mask = (marks_series < PASSING_MARKS_THRESHOLD) | (
        attendance_series < MIN_ATTENDANCE_PERCENTAGE
    )
    return risk_mask.rename("at_risk")


def print_named_risk_report(
    marks_series: pd.Series,
    attendance_series: pd.Series,
    risk_series: pd.Series,
) -> None:
    print("\n--- Named At-Risk Report ---")
    print(f"{'Student':<8} {'Marks':>6} {'Attend%':>8} {'Status':>10}")
    print("-" * 38)
    for student_name in marks_series.index:
        status = "At Risk" if bool(risk_series[student_name]) else "Safe"
        print(
            f"{student_name:<8} "
            f"{marks_series[student_name]:>6.1f} "
            f"{attendance_series[student_name]:>8.1f} "
            f"{status:>10}"
        )
    print("-" * 38)
    at_risk_students = risk_series[risk_series].index.tolist()
    print(f"At-risk students: {at_risk_students}")


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_data = load_student_data()

    marks_series_default = make_marks_series_from_list(student_data)
    inspect_series("Marks Series (default integer index)", marks_series_default)

    marks_series = make_marks_series_with_names(student_data)
    inspect_series("Marks Series (named index)", marks_series)

    attendance_series = make_attendance_series_from_array(student_data)
    inspect_series("Attendance Series (from NumPy array)", attendance_series)

    show_label_access(marks_series)

    array_vs_series_demo(student_data)

    risk_series = detect_at_risk_with_series(marks_series, attendance_series)
    print_named_risk_report(marks_series, attendance_series, risk_series)

    print("\nData Scientist Note:")
    print("- Series carries values + labels, so output is self-explaining.")
    print("- Aligned Series make label-based comparisons safe and readable.")
    print("- This is the foundation step before introducing DataFrames.")


if __name__ == "__main__":
    main()
