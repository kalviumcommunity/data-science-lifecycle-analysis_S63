"""Milestone 4.33: Detecting Missing Values in DataFrames.

Project: At-Risk Student Detection System
Focus: locate, count, and inspect missing values BEFORE cleaning.

Note: this milestone is read-only. We do NOT clean or fill the data here.
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
DATA_DIR = PROJECT_ROOT / "data" / "raw"

DATASETS_TO_INSPECT = {
    "students.csv (clean)": DATA_DIR / "students.csv",
    "students_unclean.csv (with missing values)": DATA_DIR / "students_unclean.csv",
}

PROJECT_NUMERIC_COLUMNS = ("marks", "attendance")


# ---------------------------------------------------------------------------
# Section 3: Loader (read-only)
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Missing-Value Mask
# ---------------------------------------------------------------------------
def show_missing_value_mask(df: pd.DataFrame) -> None:
    print("\n--- Missing Value Mask (df.isna()) ---")
    print(df.isna())


# ---------------------------------------------------------------------------
# Section 5: Per-Column Missing Counts
# ---------------------------------------------------------------------------
def report_missing_per_column(df: pd.DataFrame) -> pd.DataFrame:
    null_counts = df.isna().sum()
    null_percent = (null_counts / len(df) * 100).round(2)

    summary = pd.DataFrame({
        "missing_count": null_counts,
        "missing_percent": null_percent,
    })

    print("\n--- Missing Values per Column ---")
    print(summary)
    return summary


# ---------------------------------------------------------------------------
# Section 6: Rows with Any Missing Values
# ---------------------------------------------------------------------------
def show_problematic_rows(df: pd.DataFrame) -> pd.DataFrame:
    rows_with_missing = df[df.isna().any(axis=1)]
    print("\n--- Rows With at Least One Missing Value ---")
    if rows_with_missing.empty:
        print("None. The dataset has no missing values in any row.")
    else:
        print(rows_with_missing)
        print(f"Rows affected: {len(rows_with_missing)} / {len(df)}")
    return rows_with_missing


# ---------------------------------------------------------------------------
# Section 7: Pattern Insight
# ---------------------------------------------------------------------------
def describe_pattern(rows_with_missing: pd.DataFrame) -> None:
    print("\n--- Missing Value Pattern Insight ---")
    if rows_with_missing.empty:
        print("No missing values, so no pattern to investigate.")
        return

    print("Affected student names:")
    print(list(rows_with_missing["name"]))

    affected_columns = rows_with_missing.columns[
        rows_with_missing.isna().any(axis=0)
    ].tolist()
    print(f"Affected columns: {affected_columns}")

    if len(rows_with_missing) > 1:
        print("Pattern looks scattered across multiple students.")
    else:
        print("Pattern is isolated to a single student record.")


# ---------------------------------------------------------------------------
# Section 8: Project Impact Statement
# ---------------------------------------------------------------------------
def report_project_impact(df: pd.DataFrame) -> None:
    print("\n--- Project Impact ---")
    risk_relevant_missing = df[list(PROJECT_NUMERIC_COLUMNS)].isna().any(axis=1)
    impacted_rows = int(risk_relevant_missing.sum())

    if impacted_rows == 0:
        print("All risk-relevant features are present. Risk detection can run safely.")
    else:
        print(
            f"{impacted_rows} student(s) have missing values in "
            f"{list(PROJECT_NUMERIC_COLUMNS)}."
        )
        print("Impact:")
        print("  - Risk thresholds (marks < 50 or attendance < 75) cannot be evaluated.")
        print("  - These rows would produce unreliable or NaN-based decisions.")
        print("  - Cleaning is required before classification.")


# ---------------------------------------------------------------------------
# Section 9: Inspection Routine per Dataset
# ---------------------------------------------------------------------------
def run_missing_value_inspection(label: str, csv_path: Path) -> None:
    print("\n" + "=" * 72)
    print(f"Dataset: {label}")
    print(f"Path   : {csv_path}")
    print("=" * 72)

    df = load_dataframe(csv_path)
    print(f"Shape: {df.shape}")
    print(f"Total cells: {df.size}")
    print(f"Total missing cells: {int(df.isna().sum().sum())}")

    show_missing_value_mask(df)
    report_missing_per_column(df)
    rows_with_missing = show_problematic_rows(df)
    describe_pattern(rows_with_missing)
    report_project_impact(df)


# ---------------------------------------------------------------------------
# Section 10: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print("Read-only detection of missing values in student datasets.")

    for label, csv_path in DATASETS_TO_INSPECT.items():
        run_missing_value_inspection(label, csv_path)

    print("\nData Scientist Note:")
    print("- isna() is the canonical missing-value check in pandas.")
    print("- Always count missing values per column before cleaning.")
    print("- Inspect problematic rows to understand the missing-value pattern.")
    print("- The next milestone will define and apply a cleaning strategy.")


if __name__ == "__main__":
    main()
