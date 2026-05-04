"""Milestone 4.36: Standardizing Column Names and Data Formats.

Project: At-Risk Student Detection System
Focus: take a messy dataset (mixed-case headers, whitespace, % symbols)
       and produce a clean, predictable, project-ready DataFrame.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
import re
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students_messy.csv"
PROCESSED_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "students_standardized.csv"

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75


# ---------------------------------------------------------------------------
# Section 3: Loader
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Column-Name Standardization
# ---------------------------------------------------------------------------
def to_snake_case(column_name: str) -> str:
    """Convert a single column name into a clean snake_case identifier."""
    cleaned = column_name.strip().lower()
    cleaned = re.sub(r"%", "_percent", cleaned)
    cleaned = re.sub(r"[^a-z0-9]+", "_", cleaned)
    cleaned = re.sub(r"_+", "_", cleaned).strip("_")
    return cleaned


def standardize_column_names(df: pd.DataFrame) -> pd.DataFrame:
    standardized = df.copy()
    standardized.columns = [to_snake_case(name) for name in standardized.columns]
    return standardized


COLUMN_RENAME_MAP = {
    "student_name": "name",
    "attendance_percent": "attendance",
}


def apply_project_column_names(df: pd.DataFrame) -> pd.DataFrame:
    """Map standardized columns to the project's canonical names."""
    return df.rename(columns=COLUMN_RENAME_MAP)


# ---------------------------------------------------------------------------
# Section 5: Text Standardization
# ---------------------------------------------------------------------------
def standardize_text_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()
    if "name" in cleaned.columns:
        cleaned["name"] = (
            cleaned["name"].astype(str).str.strip().str.title()
        )
    return cleaned


# ---------------------------------------------------------------------------
# Section 6: Numeric Standardization
# ---------------------------------------------------------------------------
def standardize_numeric_columns(df: pd.DataFrame) -> pd.DataFrame:
    cleaned = df.copy()

    if "marks" in cleaned.columns:
        cleaned["marks"] = pd.to_numeric(
            cleaned["marks"].astype(str).str.strip(),
            errors="coerce",
        )

    if "attendance" in cleaned.columns:
        attendance_text = (
            cleaned["attendance"].astype(str).str.strip().str.replace("%", "", regex=False)
        )
        cleaned["attendance"] = pd.to_numeric(attendance_text, errors="coerce")

    return cleaned


# ---------------------------------------------------------------------------
# Section 7: Project Risk Logic
# ---------------------------------------------------------------------------
def add_risk_status(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


# ---------------------------------------------------------------------------
# Section 8: Reporting
# ---------------------------------------------------------------------------
def show_columns_before_after(before: list[str], after: list[str]) -> None:
    print("\n--- Column Names: Before vs After ---")
    width = max(len(name) for name in before)
    print(f"{'before':<{width + 2}}  after")
    for original, cleaned in zip(before, after):
        print(f"{original:<{width + 2}}  {cleaned}")


def show_dtypes_and_head(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- {label} ---")
    print("Dtypes:")
    print(df.dtypes)
    print("Head:")
    print(df.head())


def print_clean_report(df: pd.DataFrame) -> None:
    print("\n--- Risk Report on Standardized Data ---")
    print(df.to_string(index=False))
    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print(f"\nTotal students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 9: Save Cleaned Output
# ---------------------------------------------------------------------------
def save_cleaned_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nSaved standardized dataset -> {output_path}")


# ---------------------------------------------------------------------------
# Section 10: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Raw input file: {RAW_CSV_PATH}")

    raw_df = load_dataframe(RAW_CSV_PATH)
    show_dtypes_and_head(raw_df, "Raw DataFrame")
    original_columns = list(raw_df.columns)

    # Step 2-4: column name standardization
    snake_df = standardize_column_names(raw_df)
    project_df = apply_project_column_names(snake_df)

    show_columns_before_after(original_columns, list(project_df.columns))

    # Step 5: text columns
    text_clean_df = standardize_text_columns(project_df)

    # Step 6-7: numeric columns
    fully_clean_df = standardize_numeric_columns(text_clean_df)

    show_dtypes_and_head(fully_clean_df, "Standardized DataFrame")

    # Step 9: project logic + save
    enriched = add_risk_status(fully_clean_df)
    print_clean_report(enriched)
    save_cleaned_dataframe(enriched, PROCESSED_CSV_PATH)

    print("\nData Scientist Note:")
    print("- Standardized columns: snake_case, no spaces, predictable access.")
    print("- Standardized text: stripped + title-cased to avoid identity drift.")
    print("- Standardized numerics: '%' removed and dtype coerced to numeric.")
    print("- Always standardize before any analysis or merging across sources.")


if __name__ == "__main__":
    main()
