"""Milestone 4.28: Creating Pandas DataFrames from Dictionaries and Files.

Project: At-Risk Student Detection System
Focus: convert the project into a real data-driven workflow by representing
       students as a DataFrame and loading the dataset from a CSV file.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
from pathlib import Path

import pandas as pd


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75

PROJECT_ROOT = Path(__file__).resolve().parents[1]
RAW_DATA_PATH = PROJECT_ROOT / "data" / "raw" / "students.csv"


# ---------------------------------------------------------------------------
# Section 3: Build DataFrame from Dictionary
# ---------------------------------------------------------------------------
def build_students_dataframe_from_dict() -> pd.DataFrame:
    """Construct a DataFrame from an in-memory dictionary."""
    student_data = {
        "name": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        "marks": [88, 49, 72, 83, 95],
        "attendance": [91, 79, 70, 86, 98],
    }
    return pd.DataFrame(student_data)


# ---------------------------------------------------------------------------
# Section 4: Load DataFrame from CSV File
# ---------------------------------------------------------------------------
def load_students_dataframe_from_csv(csv_path: Path) -> pd.DataFrame:
    """Load student records from a CSV file using pandas."""
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 5: Inspection Helpers
# ---------------------------------------------------------------------------
def inspect_dataframe(label: str, df: pd.DataFrame) -> None:
    print(f"\n--- {label} ---")
    print("First rows (head):")
    print(df.head())
    print(f"\nShape   : {df.shape}  (rows, columns)")
    print(f"Columns : {list(df.columns)}")
    print("Dtypes  :")
    print(df.dtypes)


# ---------------------------------------------------------------------------
# Section 6: Project Integration (Data-Driven Risk Detection)
# ---------------------------------------------------------------------------
def add_risk_status_column(df: pd.DataFrame) -> pd.DataFrame:
    """Return a copy of the DataFrame with an `at_risk` boolean column."""
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_clean_report(df: pd.DataFrame) -> None:
    print("\n--- Student Report (DataFrame) ---")
    print(df.to_string(index=False))

    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print("\n--- Summary ---")
    print(f"Total students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 7: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    # Step 2: from dictionary
    df_from_dict = build_students_dataframe_from_dict()
    inspect_dataframe("DataFrame built from dictionary", df_from_dict)

    # Step 5: from CSV file
    df_from_csv = load_students_dataframe_from_csv(RAW_DATA_PATH)
    inspect_dataframe("DataFrame loaded from CSV", df_from_csv)

    # Step 8: integrate the file-based dataset into project logic
    enriched_df = add_risk_status_column(df_from_csv)
    print_clean_report(enriched_df)

    print("\nData Scientist Note:")
    print("- DataFrames replaced ad-hoc lists/arrays with a tabular dataset.")
    print("- File-based loading mirrors how real systems consume data.")
    print("- The project is now data-driven and ready for analysis steps.")


if __name__ == "__main__":
    main()
