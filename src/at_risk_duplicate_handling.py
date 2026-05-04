"""Milestone 4.35: Identifying and Removing Duplicate Records.

Project: At-Risk Student Detection System
Focus: detect exact and partial duplicate student records, remove them
       safely, and persist a deduplicated dataset for risk analysis.
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
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students_with_duplicates.csv"
PROCESSED_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "students_deduplicated.csv"

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75
IDENTITY_COLUMN = "name"


# ---------------------------------------------------------------------------
# Section 3: Loader
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Duplicate Detection
# ---------------------------------------------------------------------------
def report_duplicates(df: pd.DataFrame) -> dict[str, int]:
    """Report counts of exact duplicates and name-based duplicates."""
    exact_count = int(df.duplicated().sum())
    name_count = int(df.duplicated(subset=[IDENTITY_COLUMN]).sum())
    print("\n--- Duplicate Detection ---")
    print(f"Exact duplicate rows         : {exact_count}")
    print(f"Duplicate '{IDENTITY_COLUMN}' rows           : {name_count}")
    return {"exact": exact_count, "by_name": name_count}


def show_duplicate_rows(df: pd.DataFrame) -> None:
    """Print every row that is involved in a duplicate (full and partial)."""
    full_duplicates = df[df.duplicated(keep=False)]
    name_duplicates = df[df.duplicated(subset=[IDENTITY_COLUMN], keep=False)]

    print("\nExact duplicate rows (all occurrences):")
    print(full_duplicates if not full_duplicates.empty else "  None")

    print("\nRows sharing a 'name' (all occurrences):")
    print(name_duplicates if not name_duplicates.empty else "  None")


# ---------------------------------------------------------------------------
# Section 5: Removal Strategies
# ---------------------------------------------------------------------------
def drop_exact_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows that are exact copies of any earlier row."""
    return df.drop_duplicates(keep="first").reset_index(drop=True)


def drop_duplicates_by_name(df: pd.DataFrame) -> pd.DataFrame:
    """Remove rows that repeat the identity column (`name`), keeping the first."""
    return df.drop_duplicates(subset=[IDENTITY_COLUMN], keep="first").reset_index(drop=True)


# ---------------------------------------------------------------------------
# Section 6: Verification
# ---------------------------------------------------------------------------
def verify_no_duplicates(df: pd.DataFrame, label: str) -> None:
    counts = report_duplicates(df)
    if counts["exact"] == 0 and counts["by_name"] == 0:
        print(f"OK :: {label} has no duplicates.")
    else:
        print(f"WARNING :: {label} still contains duplicates.")


# ---------------------------------------------------------------------------
# Section 7: Project Risk Classification
# ---------------------------------------------------------------------------
def add_risk_status(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_clean_report(df: pd.DataFrame) -> None:
    print("\n--- Risk Report on Deduplicated Data ---")
    print(df.to_string(index=False))
    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print(f"\nTotal students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 8: Save Cleaned Output
# ---------------------------------------------------------------------------
def save_cleaned_dataframe(df: pd.DataFrame, output_path: Path) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"\nSaved deduplicated dataset -> {output_path}")


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Raw input file: {RAW_CSV_PATH}")

    raw_df = load_dataframe(RAW_CSV_PATH)
    print(f"\nInitial shape: {raw_df.shape}")
    print(raw_df)

    # Step 2 & 3: detect and inspect
    counts_before = report_duplicates(raw_df)
    show_duplicate_rows(raw_df)

    # Step 5: remove exact duplicates first
    after_exact = drop_exact_duplicates(raw_df)
    print(f"\nShape after dropping EXACT duplicates : {after_exact.shape}")
    print(f"Rows removed (exact strategy)         : {len(raw_df) - len(after_exact)}")

    # Step 6: remove name-based duplicates next
    after_name = drop_duplicates_by_name(after_exact)
    print(f"\nShape after dropping NAME duplicates  : {after_name.shape}")
    print(f"Rows removed (name strategy)          : {len(after_exact) - len(after_name)}")

    # Step 8: verify
    print("\n--- Verification ---")
    verify_no_duplicates(after_name, "after_name")

    # Step 9: apply project logic and save
    enriched = add_risk_status(after_name)
    print_clean_report(enriched)
    save_cleaned_dataframe(enriched, PROCESSED_CSV_PATH)

    # Step 7: before vs after summary
    print("\n--- Before vs After Summary ---")
    print(f"Original rows                 : {len(raw_df)}")
    print(f"After dropping duplicates     : {len(after_name)}")
    print(f"Total duplicates removed      : {len(raw_df) - len(after_name)}")
    print(f"Exact duplicates detected     : {counts_before['exact']}")
    print(f"Duplicate-name rows detected  : {counts_before['by_name']}")

    print("\nData Scientist Note:")
    print("- Duplicates inflate counts and bias every metric.")
    print("- Deduplicate by exact match first, then by identity if needed.")
    print("- Always re-verify after cleaning before running analysis.")


if __name__ == "__main__":
    main()
