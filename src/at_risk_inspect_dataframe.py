"""Milestone 4.30: Inspecting DataFrames using head(), info(), and describe().

Project: At-Risk Student Detection System
Focus: build a strong inspection habit BEFORE any cleaning or analysis.

Note: this milestone is read-only. We do NOT modify or clean the data here.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
CLEAN_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students.csv"
UNCLEAN_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students_unclean.csv"


# ---------------------------------------------------------------------------
# Section 3: Loader (read-only)
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    """Read a CSV with no modifications applied to the underlying values."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: head() - First Visual Look
# ---------------------------------------------------------------------------
def show_head(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- head() :: {label} ---")
    print(df.head())


# ---------------------------------------------------------------------------
# Section 5: info() - Structural Health Check
# ---------------------------------------------------------------------------
def show_info(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- info() :: {label} ---")
    df.info()
    print("\nNull counts per column:")
    print(df.isnull().sum())


# ---------------------------------------------------------------------------
# Section 6: describe() - Statistical Summary
# ---------------------------------------------------------------------------
def show_describe(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- describe() :: {label} ---")
    print(df.describe(include="all"))


# ---------------------------------------------------------------------------
# Section 7: Findings Interpreter
# ---------------------------------------------------------------------------
def interpret_findings(df: pd.DataFrame, label: str) -> list[str]:
    """Return human-readable observations from the three inspection views."""
    findings: list[str] = []

    findings.append(f"Total rows: {len(df)}")
    findings.append(f"Total columns: {df.shape[1]} -> {list(df.columns)}")

    null_counts = df.isnull().sum()
    columns_with_nulls = null_counts[null_counts > 0]
    if not columns_with_nulls.empty:
        for column_name, null_count in columns_with_nulls.items():
            findings.append(f"Missing values in '{column_name}': {null_count}")
    else:
        findings.append("No missing values detected.")

    if "marks" in df.columns:
        marks = df["marks"].dropna()
        if not marks.empty:
            findings.append(
                f"Marks range: min={marks.min()}, max={marks.max()}, mean={marks.mean():.2f}"
            )
            low_count = int((marks < 50).sum())
            findings.append(f"Students with marks < 50: {low_count}")

    if "attendance" in df.columns:
        attendance = df["attendance"].dropna()
        if not attendance.empty:
            findings.append(
                f"Attendance range: min={attendance.min()}, "
                f"max={attendance.max()}, mean={attendance.mean():.2f}"
            )
            low_attendance = int((attendance < 75).sum())
            findings.append(f"Students with attendance < 75%: {low_attendance}")

    print(f"\n--- Findings :: {label} ---")
    for finding in findings:
        print(f"- {finding}")

    return findings


# ---------------------------------------------------------------------------
# Section 8: Inspection Routine
# ---------------------------------------------------------------------------
def run_inspection(df: pd.DataFrame, label: str) -> None:
    show_head(df, label)
    show_info(df, label)
    show_describe(df, label)
    interpret_findings(df, label)


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print("Read-only inspection of student datasets.\n")

    clean_df = load_dataframe(CLEAN_CSV_PATH)
    run_inspection(clean_df, "students.csv (clean version)")

    unclean_df = load_dataframe(UNCLEAN_CSV_PATH)
    run_inspection(unclean_df, "students_unclean.csv (with missing values)")

    print("\nData Scientist Note:")
    print("- head() confirmed columns and basic alignment.")
    print("- info() exposed dtypes and missing values per column.")
    print("- describe() summarized distribution to spot suspicious values.")
    print("- These three views together drive every cleaning decision in the next milestone.")


if __name__ == "__main__":
    main()
