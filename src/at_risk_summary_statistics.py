"""Milestone 4.37: Computing Basic Summary Statistics for Individual Columns.

Project: At-Risk Student Detection System
Focus: turn the standardized dataset into per-column insights that guide
       risk detection decisions.

Note: this milestone reports statistics only. Risk classification still
runs at the end so we can connect insights to actions.
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


# ---------------------------------------------------------------------------
# Section 3: Loader
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Per-Column Statistics
# ---------------------------------------------------------------------------
def compute_column_statistics(series: pd.Series) -> dict[str, float]:
    """Return a small dictionary of basic statistics for one numeric column."""
    return {
        "count": int(series.count()),
        "mean": float(series.mean()),
        "median": float(series.median()),
        "min": float(series.min()),
        "max": float(series.max()),
        "range": float(series.max() - series.min()),
        "std": float(series.std()),
        "q25": float(series.quantile(0.25)),
        "q75": float(series.quantile(0.75)),
    }


def print_column_statistics(label: str, stats: dict[str, float]) -> None:
    print(f"\n--- Statistics :: {label} ---")
    print(f"count : {stats['count']}")
    print(f"mean  : {stats['mean']:.2f}")
    print(f"median: {stats['median']:.2f}")
    print(f"min   : {stats['min']:.2f}")
    print(f"max   : {stats['max']:.2f}")
    print(f"range : {stats['range']:.2f}")
    print(f"std   : {stats['std']:.2f}")
    print(f"q25   : {stats['q25']:.2f}")
    print(f"q75   : {stats['q75']:.2f}")


def mean_vs_median_signal(stats: dict[str, float], label: str) -> None:
    diff = stats["mean"] - stats["median"]
    if abs(diff) < 1.0:
        verdict = "balanced (mean ~ median)"
    elif diff > 0:
        verdict = "right-skewed: mean > median (high outliers possible)"
    else:
        verdict = "left-skewed: mean < median (low outliers possible)"
    print(f"Mean vs Median ({label}): {verdict}")


# ---------------------------------------------------------------------------
# Section 5: Column-vs-Column Comparison
# ---------------------------------------------------------------------------
def compare_columns(stats_a: dict[str, float], label_a: str,
                    stats_b: dict[str, float], label_b: str) -> None:
    print(f"\n--- Comparison :: {label_a} vs {label_b} ---")
    print(f"{'metric':<8} {label_a:>10} {label_b:>10}")
    for metric in ("mean", "median", "min", "max", "range", "std"):
        print(f"{metric:<8} {stats_a[metric]:>10.2f} {stats_b[metric]:>10.2f}")


# ---------------------------------------------------------------------------
# Section 6: Risk Pattern Insight
# ---------------------------------------------------------------------------
def report_risk_patterns(df: pd.DataFrame) -> None:
    print("\n--- Risk Pattern Insight ---")

    low_marks_count = int((df["marks"] < PASSING_MARKS_THRESHOLD).sum())
    low_attendance_count = int((df["attendance"] < MIN_ATTENDANCE_PERCENTAGE).sum())
    both_low_count = int(
        ((df["marks"] < PASSING_MARKS_THRESHOLD) &
         (df["attendance"] < MIN_ATTENDANCE_PERCENTAGE)).sum()
    )

    print(f"Students with marks < {PASSING_MARKS_THRESHOLD}      : {low_marks_count}")
    print(f"Students with attendance < {MIN_ATTENDANCE_PERCENTAGE}% : {low_attendance_count}")
    print(f"Students failing on BOTH conditions : {both_low_count}")

    # Identify lowest performers based on the stats lens
    bottom_marks = df.nsmallest(3, "marks")[["name", "marks", "attendance"]]
    bottom_attendance = df.nsmallest(3, "attendance")[["name", "marks", "attendance"]]

    print("\nBottom 3 by marks:")
    print(bottom_marks.to_string(index=False))

    print("\nBottom 3 by attendance:")
    print(bottom_attendance.to_string(index=False))


# ---------------------------------------------------------------------------
# Section 7: Risk Classification (kept consistent with project rule)
# ---------------------------------------------------------------------------
def add_risk_status(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_clean_report(df: pd.DataFrame) -> None:
    print("\n--- Risk Report Linked to Statistics ---")
    print(df.to_string(index=False))
    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print(f"\nTotal students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 8: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Input file: {INPUT_CSV_PATH}")

    df = load_dataframe(INPUT_CSV_PATH)
    print(f"\nShape: {df.shape}")
    print(df.head())

    # Drop the previously added at_risk column for a clean stats view
    if "at_risk" in df.columns:
        df_for_stats = df.drop(columns=["at_risk"])
    else:
        df_for_stats = df

    # Per-column statistics
    marks_stats = compute_column_statistics(df_for_stats["marks"])
    attendance_stats = compute_column_statistics(df_for_stats["attendance"])

    print_column_statistics("marks", marks_stats)
    mean_vs_median_signal(marks_stats, "marks")

    print_column_statistics("attendance", attendance_stats)
    mean_vs_median_signal(attendance_stats, "attendance")

    # Compare both numeric columns
    compare_columns(marks_stats, "marks", attendance_stats, "attendance")

    # Risk pattern insight
    report_risk_patterns(df_for_stats)

    # Connect insights to project decision
    enriched = add_risk_status(df_for_stats)
    print_clean_report(enriched)

    print("\nData Scientist Note:")
    print("- mean and median together expose skew that a single metric hides.")
    print("- range and std reveal how spread out marks/attendance are.")
    print("- 'bottom-N' lists are the fastest entry point for intervention talks.")


if __name__ == "__main__":
    main()
