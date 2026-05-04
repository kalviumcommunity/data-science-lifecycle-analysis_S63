"""Milestone 4.32: Selecting Rows and Columns Using Indexing and Slicing.

Project: At-Risk Student Detection System
Focus: extract specific subsets of the dataset cleanly using positional
       and label-based selection. Read-only milestone (no analysis yet).
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
CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students.csv"


# ---------------------------------------------------------------------------
# Section 3: Loader (read-only)
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Column Selection
# ---------------------------------------------------------------------------
def show_column_selection(df: pd.DataFrame) -> None:
    print("\n--- Column Selection ---")

    print("Single column (df['marks']) - returns a Series:")
    print(df["marks"].head())

    print("\nMultiple columns (df[['marks', 'attendance']]) - returns a DataFrame:")
    print(df[["marks", "attendance"]].head())


# ---------------------------------------------------------------------------
# Section 5: Row Selection by Position (iloc)
# ---------------------------------------------------------------------------
def show_row_selection_by_position(df: pd.DataFrame) -> None:
    print("\n--- Row Selection by Position (iloc) ---")

    print("First student (df.iloc[0]):")
    print(df.iloc[0])

    print("\nFirst 3 students (df.iloc[:3]):")
    print(df.iloc[:3])

    print("\nMiddle slice (df.iloc[2:6]):")
    print(df.iloc[2:6])


# ---------------------------------------------------------------------------
# Section 6: Row Selection by Label (loc)
# ---------------------------------------------------------------------------
def show_row_selection_by_label(df: pd.DataFrame) -> None:
    print("\n--- Row Selection by Label (loc) ---")

    df_by_name = df.set_index("name")

    print("Single student by name (df_by_name.loc['Aisha']):")
    print(df_by_name.loc["Aisha"])

    print("\nMultiple students by name (df_by_name.loc[['Rohit', 'Neha', 'Karan']]):")
    print(df_by_name.loc[["Rohit", "Neha", "Karan"]])


# ---------------------------------------------------------------------------
# Section 7: Combined Row + Column Selection
# ---------------------------------------------------------------------------
def show_combined_selection(df: pd.DataFrame) -> None:
    print("\n--- Combined Row + Column Selection ---")

    print("First 5 students, only marks and attendance (iloc-style):")
    print(df.iloc[:5][["marks", "attendance"]])

    df_by_name = df.set_index("name")
    print(
        "\nSpecific students, only marks "
        "(df_by_name.loc[['Vikram', 'Sara'], 'marks']):"
    )
    print(df_by_name.loc[["Vikram", "Sara"], "marks"])

    print(
        "\nSlice of students with both numeric features "
        "(df.loc[2:5, ['marks', 'attendance']]):"
    )
    print(df.loc[2:5, ["marks", "attendance"]])


# ---------------------------------------------------------------------------
# Section 8: Verification of Selections
# ---------------------------------------------------------------------------
def verify_selections(df: pd.DataFrame) -> None:
    print("\n--- Verification ---")

    selected = df.iloc[:5][["marks", "attendance"]]
    print(f"Shape of first-5 selection : {selected.shape}  (expected (5, 2))")

    df_by_name = df.set_index("name")
    pair = df_by_name.loc[["Vikram", "Sara"], "marks"]
    print(f"Type of pair selection     : {type(pair).__name__}")
    print(f"Index of pair selection    : {list(pair.index)}")


# ---------------------------------------------------------------------------
# Section 9: Common Mistakes Demo
# ---------------------------------------------------------------------------
def common_mistakes_demo(df: pd.DataFrame) -> None:
    print("\n--- Common Mistakes ---")

    try:
        _ = df["Marks"]  # case-sensitive mistake
    except KeyError as error:
        print(f"Wrong column name (case-sensitive) -> KeyError: {error}")

    try:
        _ = df.iloc[999]
    except IndexError as error:
        print(f"Out-of-range positional index    -> IndexError: {error}")


# ---------------------------------------------------------------------------
# Section 10: Project-Ready Selection
# ---------------------------------------------------------------------------
def select_features_for_risk_input(df: pd.DataFrame) -> pd.DataFrame:
    """Return only the columns required by risk detection logic."""
    feature_columns = ["name", "marks", "attendance"]
    return df.loc[:, feature_columns]


def show_project_ready_selection(df: pd.DataFrame) -> None:
    print("\n--- Project-Ready Selection (input to risk detection) ---")
    risk_input_df = select_features_for_risk_input(df)
    print(risk_input_df.head())
    print(f"Shape: {risk_input_df.shape}")


# ---------------------------------------------------------------------------
# Section 11: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print("Read-only indexing and slicing on the loaded student dataset.")
    print(f"Source file: {CSV_PATH}")

    df = load_dataframe(CSV_PATH)
    print(f"Initial shape: {df.shape}")

    show_column_selection(df)
    show_row_selection_by_position(df)
    show_row_selection_by_label(df)
    show_combined_selection(df)
    verify_selections(df)
    common_mistakes_demo(df)
    show_project_ready_selection(df)

    print("\nData Scientist Note:")
    print("- iloc selects by integer position; loc selects by label.")
    print("- Always verify the shape of any selection before using it.")
    print("- Project risk logic only needs name, marks, and attendance.")


if __name__ == "__main__":
    main()
