"""Milestone 4.34: Handling Missing Values Using Drop and Fill Strategies.

Project: At-Risk Student Detection System
Focus: take the previously detected missing values and apply a deliberate
       cleaning strategy before risk classification.
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
RAW_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students_unclean.csv"
PROCESSED_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "students_cleaned.csv"

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75
NUMERIC_FEATURE_COLUMNS = ("marks", "attendance")


# ---------------------------------------------------------------------------
# Section 3: Loader
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Inspection Before Cleaning
# ---------------------------------------------------------------------------
def report_missing_status(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- Missing Status :: {label} ---")
    print(f"Shape         : {df.shape}")
    print(f"Total NaN     : {int(df.isna().sum().sum())}")
    print("Per-column NaN:")
    print(df.isna().sum())


# ---------------------------------------------------------------------------
# Section 5: Drop Strategy
# ---------------------------------------------------------------------------
def drop_rows_with_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Drop any row that contains a NaN in numeric feature columns."""
    return df.dropna(subset=list(NUMERIC_FEATURE_COLUMNS)).reset_index(drop=True)


# ---------------------------------------------------------------------------
# Section 6: Fill Strategy
# ---------------------------------------------------------------------------
def fill_with_column_mean(df: pd.DataFrame) -> pd.DataFrame:
    """Fill missing values in numeric features using the column mean."""
    cleaned = df.copy()
    for column in NUMERIC_FEATURE_COLUMNS:
        column_mean = cleaned[column].mean(skipna=True)
        cleaned[column] = cleaned[column].fillna(round(column_mean, 2))
    return cleaned


# ---------------------------------------------------------------------------
# Section 7: Strategy Decision
# ---------------------------------------------------------------------------
def choose_strategy(df: pd.DataFrame) -> str:
    """Pick drop or fill based on how much data would be lost."""
    rows_total = len(df)
    rows_with_missing = int(df[list(NUMERIC_FEATURE_COLUMNS)].isna().any(axis=1).sum())
    drop_loss_percent = (rows_with_missing / rows_total) * 100

    print("\n--- Strategy Decision ---")
    print(f"Rows total            : {rows_total}")
    print(f"Rows with NaN features: {rows_with_missing}")
    print(f"Drop strategy loss    : {drop_loss_percent:.2f}%")

    if drop_loss_percent <= 5:
        chosen = "drop"
        reason = "Loss is small; dropping is the simplest and safest choice."
    else:
        chosen = "fill"
        reason = (
            "Loss is meaningful; filling preserves dataset size while keeping "
            "averages close to original."
        )

    print(f"Chosen strategy       : {chosen}")
    print(f"Reason                : {reason}")
    return chosen


# ---------------------------------------------------------------------------
# Section 8: Risk Detection on Cleaned Data
# ---------------------------------------------------------------------------
def add_risk_status(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_clean_report(df: pd.DataFrame, strategy_label: str) -> None:
    print(f"\n--- Risk Report on {strategy_label}-cleaned Data ---")
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
    print(f"\nSaved cleaned dataset -> {output_path}")


# ---------------------------------------------------------------------------
# Section 10: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Raw input file: {RAW_CSV_PATH}")

    raw_df = load_dataframe(RAW_CSV_PATH)
    report_missing_status(raw_df, "raw_df (before cleaning)")

    # Apply both strategies for comparison
    dropped_df = drop_rows_with_missing(raw_df)
    filled_df = fill_with_column_mean(raw_df)

    print("\n--- Drop Strategy Result ---")
    report_missing_status(dropped_df, "dropped_df")
    print(f"Rows lost: {len(raw_df) - len(dropped_df)}")
    print(dropped_df.head())

    print("\n--- Fill Strategy Result ---")
    report_missing_status(filled_df, "filled_df")
    print("Filled values (rows previously containing NaN):")
    affected_index = raw_df.index[
        raw_df[list(NUMERIC_FEATURE_COLUMNS)].isna().any(axis=1)
    ]
    print(filled_df.loc[affected_index])

    # Decide
    chosen = choose_strategy(raw_df)
    cleaned_df = filled_df if chosen == "fill" else dropped_df

    enriched = add_risk_status(cleaned_df)
    print_clean_report(enriched, strategy_label=chosen)

    save_cleaned_dataframe(enriched, PROCESSED_CSV_PATH)

    print("\nData Scientist Note:")
    print("- Drop is fastest but reduces dataset size.")
    print("- Fill (mean) preserves dataset size but slightly biases statistics.")
    print("- Always state your strategy and why - decisions must be defensible.")


if __name__ == "__main__":
    main()
