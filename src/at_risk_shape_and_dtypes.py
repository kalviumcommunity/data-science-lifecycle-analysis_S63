"""Milestone 4.31: Understanding Data Shapes and Column Data Types.

Project: At-Risk Student Detection System
Focus: confirm dataset size and column dtypes BEFORE any cleaning,
       and surface type problems that would break risk calculations.

Note: this milestone is read-only. We do NOT modify the data here.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
from pathlib import Path

import pandas as pd
from pandas.api.types import is_numeric_dtype, is_string_dtype


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data" / "raw"

DATASETS_TO_INSPECT = {
    "students.csv (clean)": DATA_DIR / "students.csv",
    "students_unclean.csv (missing values)": DATA_DIR / "students_unclean.csv",
    "students_typed_issues.csv (text in numeric col)": DATA_DIR / "students_typed_issues.csv",
}

EXPECTED_NUMERIC_COLUMNS = ("marks", "attendance")
EXPECTED_TEXT_COLUMNS = ("name",)


# ---------------------------------------------------------------------------
# Section 3: Loader (read-only)
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Shape Inspection
# ---------------------------------------------------------------------------
def report_shape(df: pd.DataFrame) -> None:
    rows, columns = df.shape
    print(f"Shape           : {df.shape}")
    print(f"  Rows (students): {rows}")
    print(f"  Columns        : {columns}")
    print(f"  len(df)        : {len(df)}")
    print(f"  Column names   : {list(df.columns)}")


# ---------------------------------------------------------------------------
# Section 5: Dtype Inspection
# ---------------------------------------------------------------------------
def report_dtypes(df: pd.DataFrame) -> None:
    print("\nColumn dtypes:")
    print(df.dtypes)

    print("\nPer-column summary:")
    for column_name in df.columns:
        column_dtype = df[column_name].dtype
        is_numeric = is_numeric_dtype(df[column_name])
        is_text = is_string_dtype(df[column_name])
        kind = "numeric" if is_numeric else ("text" if is_text else "other")
        print(f"  {column_name:<11} -> dtype={column_dtype}, kind={kind}")


# ---------------------------------------------------------------------------
# Section 6: Type-Issue Detection
# ---------------------------------------------------------------------------
def detect_type_issues(df: pd.DataFrame) -> list[str]:
    issues: list[str] = []

    for expected_numeric in EXPECTED_NUMERIC_COLUMNS:
        if expected_numeric not in df.columns:
            issues.append(f"Missing expected numeric column: '{expected_numeric}'.")
            continue
        if not is_numeric_dtype(df[expected_numeric]):
            issues.append(
                f"Column '{expected_numeric}' is not numeric "
                f"(dtype={df[expected_numeric].dtype})."
            )

    for expected_text in EXPECTED_TEXT_COLUMNS:
        if expected_text not in df.columns:
            issues.append(f"Missing expected text column: '{expected_text}'.")
            continue
        if not is_string_dtype(df[expected_text]):
            issues.append(
                f"Column '{expected_text}' is not text "
                f"(dtype={df[expected_text].dtype})."
            )

    return issues


def project_impact_note(issues: list[str]) -> None:
    if not issues:
        print("Project impact: types look correct. Risk math will run safely.")
        return
    print("Project impact: type problems detected.")
    print("  - Numeric operations on non-numeric columns will raise errors")
    print("  - Risk thresholds (marks < 50, attendance < 75) require numeric dtypes")
    print("  - Cleaning is required before risk classification can be trusted")


# ---------------------------------------------------------------------------
# Section 7: Cross-Check with info()
# ---------------------------------------------------------------------------
def cross_check_with_info(df: pd.DataFrame) -> None:
    print("\nCross-check via info():")
    df.info()


# ---------------------------------------------------------------------------
# Section 8: Inspection Routine
# ---------------------------------------------------------------------------
def run_inspection(label: str, csv_path: Path) -> None:
    print("\n" + "=" * 72)
    print(f"Dataset: {label}")
    print(f"Path   : {csv_path}")
    print("=" * 72)

    df = load_dataframe(csv_path)

    report_shape(df)
    report_dtypes(df)

    issues = detect_type_issues(df)
    print("\nType-issue findings:")
    if issues:
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("  - No type issues detected.")

    project_impact_note(issues)
    cross_check_with_info(df)


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print("Read-only inspection of dataset shape and column data types.")

    for label, csv_path in DATASETS_TO_INSPECT.items():
        run_inspection(label, csv_path)

    print("\nData Scientist Note:")
    print("- Shape tells you the dataset's size and structure (rows x columns).")
    print("- Dtypes tell you which operations are safe per column.")
    print("- Numeric thresholds in this project ONLY work on numeric dtypes.")
    print("- Cleaning the next milestone will rely on the issues found here.")


if __name__ == "__main__":
    main()
