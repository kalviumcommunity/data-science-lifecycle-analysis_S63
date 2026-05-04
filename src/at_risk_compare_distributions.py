"""Milestone 4.38: Comparing Distributions Across Multiple Columns.

Project: At-Risk Student Detection System
Focus: contrast the distributions of `marks` and `attendance` to surface
       cross-column patterns that drive at-risk decisions.

Note: no graphs in this milestone. Comparison is purely statistical.
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
INPUT_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "students_standardized.csv"

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75
NUMERIC_COLUMNS = ("marks", "attendance")
LOW_QUARTILE = 0.25


# ---------------------------------------------------------------------------
# Section 3: Loader
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Side-by-Side Distribution Summary
# ---------------------------------------------------------------------------
def build_distribution_summary(df: pd.DataFrame) -> pd.DataFrame:
    """Return a compact comparison table for numeric columns."""
    summary_rows = {}
    for column in NUMERIC_COLUMNS:
        series = df[column]
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        summary_rows[column] = {
            "count": int(series.count()),
            "mean": round(float(series.mean()), 2),
            "median": round(float(series.median()), 2),
            "min": float(series.min()),
            "max": float(series.max()),
            "range": float(series.max() - series.min()),
            "std": round(float(series.std()), 2),
            "q25": float(q1),
            "q75": float(q3),
            "iqr": float(q3 - q1),
        }
    return pd.DataFrame(summary_rows).T


# ---------------------------------------------------------------------------
# Section 5: Cross-Column Differences
# ---------------------------------------------------------------------------
def report_mean_difference(df: pd.DataFrame) -> None:
    marks_mean = df["marks"].mean()
    attendance_mean = df["attendance"].mean()
    delta = attendance_mean - marks_mean
    print("\n--- Mean Comparison ---")
    print(f"marks mean      : {marks_mean:.2f}")
    print(f"attendance mean : {attendance_mean:.2f}")
    print(f"attendance - marks : {delta:+.2f}")
    if delta > 5:
        print("Reading: attendance is higher than marks on average.")
    elif delta < -5:
        print("Reading: marks are higher than attendance on average.")
    else:
        print("Reading: averages are close to each other.")


def report_spread_comparison(df: pd.DataFrame) -> None:
    print("\n--- Spread Comparison (range and std) ---")
    for column in NUMERIC_COLUMNS:
        series = df[column]
        print(
            f"{column:<11} -> range={float(series.max() - series.min()):.2f}, "
            f"std={series.std():.2f}"
        )
    if (df["marks"].std() > df["attendance"].std()):
        print("Reading: marks vary more than attendance across the class.")
    else:
        print("Reading: attendance varies more than marks across the class.")


# ---------------------------------------------------------------------------
# Section 6: Cross-Column Relationship
# ---------------------------------------------------------------------------
def report_correlation(df: pd.DataFrame) -> None:
    correlation = df["marks"].corr(df["attendance"])
    print("\n--- Relationship Between Marks and Attendance ---")
    print(f"Pearson correlation (marks vs attendance): {correlation:.3f}")
    if correlation > 0.5:
        verdict = "Strong positive: low marks tend to coincide with low attendance."
    elif correlation > 0.2:
        verdict = "Moderate positive: some link between low marks and low attendance."
    elif correlation > -0.2:
        verdict = "Weak link: marks and attendance move mostly independently."
    elif correlation > -0.5:
        verdict = "Moderate negative: unusual pattern, worth deeper review."
    else:
        verdict = "Strong negative: high marks correlate with low attendance (rare)."
    print(f"Reading: {verdict}")


def show_low_low_overlap(df: pd.DataFrame) -> None:
    print("\n--- Low-Low Overlap ---")
    low_marks = df["marks"] < df["marks"].quantile(LOW_QUARTILE)
    low_attendance = df["attendance"] < df["attendance"].quantile(LOW_QUARTILE)
    overlap = df[low_marks & low_attendance]
    print(
        f"Students in BOTTOM 25% of marks AND attendance: {len(overlap)}"
    )
    if not overlap.empty:
        print(overlap[["name", "marks", "attendance"]].to_string(index=False))


# ---------------------------------------------------------------------------
# Section 7: Outlier Detection (IQR Rule)
# ---------------------------------------------------------------------------
def detect_iqr_outliers(df: pd.DataFrame) -> None:
    print("\n--- Outlier Detection (IQR rule, k=1.5) ---")
    for column in NUMERIC_COLUMNS:
        series = df[column]
        q1 = series.quantile(0.25)
        q3 = series.quantile(0.75)
        iqr = q3 - q1
        low_bound = q1 - 1.5 * iqr
        high_bound = q3 + 1.5 * iqr
        outliers = df.loc[(series < low_bound) | (series > high_bound),
                          ["name", column]]
        print(
            f"{column:<11} -> low<{low_bound:.2f}, high>{high_bound:.2f}, "
            f"outliers={len(outliers)}"
        )
        if not outliers.empty:
            print(outliers.to_string(index=False))


# ---------------------------------------------------------------------------
# Section 8: Project Risk Application
# ---------------------------------------------------------------------------
def add_risk_status(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_risk_summary(df: pd.DataFrame) -> None:
    print("\n--- Risk Summary Linked to Distributions ---")
    print(df.to_string(index=False))
    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print(f"\nTotal students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Input file: {INPUT_CSV_PATH}")

    df = load_dataframe(INPUT_CSV_PATH)
    if "at_risk" in df.columns:
        df = df.drop(columns=["at_risk"])

    print(f"\nShape: {df.shape}")
    print(df.head())

    summary = build_distribution_summary(df)
    print("\n--- Side-by-Side Distribution Summary ---")
    print(summary)

    report_mean_difference(df)
    report_spread_comparison(df)
    report_correlation(df)
    show_low_low_overlap(df)
    detect_iqr_outliers(df)

    enriched = add_risk_status(df)
    print_risk_summary(enriched)

    print("\nData Scientist Note:")
    print("- Distribution comparison goes beyond single numbers.")
    print("- Correlation flags whether marks and attendance move together.")
    print("- IQR-based outliers identify candidates for individual review.")


if __name__ == "__main__":
    main()
