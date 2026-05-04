"""Milestone 4.29: Loading CSV Data into Pandas DataFrames.

Project: At-Risk Student Detection System
Focus: replace hardcoded student data with a real CSV input pipeline,
       including path validation, schema checks, and inspection.
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
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "students.csv"

REQUIRED_COLUMNS = ("name", "marks", "attendance")

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75


# ---------------------------------------------------------------------------
# Section 3: CSV Loading Pipeline
# ---------------------------------------------------------------------------
def validate_csv_path(csv_path: Path) -> None:
    """Confirm the CSV file exists and is not empty before reading."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    if csv_path.stat().st_size == 0:
        raise ValueError(f"CSV file is empty: {csv_path}")


def load_csv_to_dataframe(csv_path: Path) -> pd.DataFrame:
    """Load the CSV after validating its path."""
    validate_csv_path(csv_path)
    return pd.read_csv(csv_path)


def validate_schema(df: pd.DataFrame) -> None:
    """Ensure all required columns are present in the loaded DataFrame."""
    missing_columns = [column for column in REQUIRED_COLUMNS if column not in df.columns]
    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}. "
            f"Found columns: {list(df.columns)}"
        )


# ---------------------------------------------------------------------------
# Section 4: Inspection Helpers
# ---------------------------------------------------------------------------
def inspect_loaded_data(df: pd.DataFrame) -> None:
    """Print key inspection views: head, tail, shape, columns, dtypes."""
    print("\n--- Head (first 5 rows) ---")
    print(df.head())

    print("\n--- Tail (last 5 rows) ---")
    print(df.tail())

    print(f"\nShape   : {df.shape}  (rows, columns)")
    print(f"Columns : {list(df.columns)}")
    print("Dtypes  :")
    print(df.dtypes)

    null_counts = df.isnull().sum()
    print("\nNull counts per column:")
    print(null_counts)


def detect_common_issues(df: pd.DataFrame) -> list[str]:
    """Return a list of human-readable issues found in the loaded DataFrame."""
    issues: list[str] = []

    if df.empty:
        issues.append("DataFrame is empty after loading.")

    if df.duplicated(subset=["name"]).any():
        duplicated_names = df.loc[df.duplicated(subset=["name"]), "name"].tolist()
        issues.append(f"Duplicate student names found: {duplicated_names}")

    for numeric_column in ("marks", "attendance"):
        if numeric_column in df.columns and not pd.api.types.is_numeric_dtype(df[numeric_column]):
            issues.append(f"Column '{numeric_column}' is not numeric.")

    if "marks" in df.columns:
        out_of_range_marks = df[(df["marks"] < 0) | (df["marks"] > 100)]
        if not out_of_range_marks.empty:
            issues.append(
                f"{len(out_of_range_marks)} row(s) have 'marks' outside 0..100."
            )

    if "attendance" in df.columns:
        out_of_range_att = df[(df["attendance"] < 0) | (df["attendance"] > 100)]
        if not out_of_range_att.empty:
            issues.append(
                f"{len(out_of_range_att)} row(s) have 'attendance' outside 0..100."
            )

    return issues


# ---------------------------------------------------------------------------
# Section 5: Project Integration on File-Loaded Data
# ---------------------------------------------------------------------------
def add_risk_status_column(df: pd.DataFrame) -> pd.DataFrame:
    """Apply project risk logic to the file-driven DataFrame."""
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_clean_report(df: pd.DataFrame) -> None:
    print("\n--- File-Driven At-Risk Report ---")
    print(df.to_string(index=False))

    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print("\n--- Summary ---")
    print(f"Source file     : {RAW_DATA_PATH}")
    print(f"Total students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 6: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print(f"Loading dataset from: {RAW_DATA_PATH}")
    df = load_csv_to_dataframe(RAW_DATA_PATH)
    validate_schema(df)

    inspect_loaded_data(df)

    issues = detect_common_issues(df)
    print("\n--- Data Quality Check ---")
    if issues:
        print("Issues detected:")
        for issue in issues:
            print(f"- {issue}")
    else:
        print("No issues detected.")

    enriched = add_risk_status_column(df)
    print_clean_report(enriched)

    print("\nData Scientist Note:")
    print("- Hardcoded data has been replaced with a real CSV input.")
    print("- The pipeline validates path, schema, and basic data quality.")
    print("- The same script handles tomorrow's updated CSV with no changes.")


if __name__ == "__main__":
    main()
