"""Milestone 4.41: Identifying Trends Over Time Using Line Plots.

Project: At-Risk Student Detection System
Focus: read marks and attendance trends per student across exam_weeks,
       detect sudden drops, and feed those signals into the at-risk rule.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # safe, file-only rendering for any environment

import matplotlib.pyplot as plt  # noqa: E402
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV_PATH = PROJECT_ROOT / "data" / "raw" / "students_timeseries.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75

# Trend rules (kept simple and explainable)
DECLINING_SLOPE_LIMIT = -0.5  # value drop per week to count as "declining"
SUDDEN_DROP_LIMIT_MARKS = -10
SUDDEN_DROP_LIMIT_ATTENDANCE = -5


# ---------------------------------------------------------------------------
# Section 3: Loader and Sorting
# ---------------------------------------------------------------------------
def load_timeseries(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    df = pd.read_csv(csv_path)
    df = df.sort_values(["name", "exam_week"]).reset_index(drop=True)
    return df


# ---------------------------------------------------------------------------
# Section 4: Per-Student Trend Math
# ---------------------------------------------------------------------------
def compute_slope(values: list) -> float:
    weeks = np.arange(len(values))
    if len(values) < 2:
        return 0.0
    slope, _intercept = np.polyfit(weeks, values, 1)
    return float(slope)


def detect_max_drop(values: list) -> float:
    if len(values) < 2:
        return 0.0
    diffs = np.diff(values)
    return float(diffs.min())


def build_trend_summary(df: pd.DataFrame) -> pd.DataFrame:
    rows = []
    for name, group in df.groupby("name"):
        group_sorted = group.sort_values("exam_week")
        marks_values = group_sorted["marks"].tolist()
        attendance_values = group_sorted["attendance"].tolist()

        marks_slope = compute_slope(marks_values)
        attendance_slope = compute_slope(attendance_values)
        marks_max_drop = detect_max_drop(marks_values)
        attendance_max_drop = detect_max_drop(attendance_values)

        rows.append(
            {
                "name": name,
                "first_marks": marks_values[0],
                "last_marks": marks_values[-1],
                "marks_slope_per_week": marks_slope,
                "marks_max_weekly_drop": marks_max_drop,
                "first_attendance": attendance_values[0],
                "last_attendance": attendance_values[-1],
                "attendance_slope_per_week": attendance_slope,
                "attendance_max_weekly_drop": attendance_max_drop,
            }
        )
    return pd.DataFrame(rows)


# ---------------------------------------------------------------------------
# Section 5: Plotting Helpers
# ---------------------------------------------------------------------------
def plot_per_student_lines(
    df: pd.DataFrame,
    value_column: str,
    title: str,
    ylabel: str,
    threshold: float,
    threshold_label: str,
    output_path: Path,
) -> None:
    plt.figure(figsize=(10, 6))
    for name, group in df.groupby("name"):
        group_sorted = group.sort_values("exam_week")
        plt.plot(
            group_sorted["exam_week"],
            group_sorted[value_column],
            marker="o",
            label=name,
        )
    plt.axhline(
        threshold,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=threshold_label,
    )
    plt.title(title)
    plt.xlabel("Exam week")
    plt.ylabel(ylabel)
    plt.xticks(sorted(df["exam_week"].unique()))
    plt.grid(linestyle=":", alpha=0.5)
    plt.legend(loc="center left", bbox_to_anchor=(1.02, 0.5), fontsize=8)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120, bbox_inches="tight")
    plt.close()
    print(f"Saved -> {output_path}")


def plot_class_average_lines(df: pd.DataFrame, output_path: Path) -> None:
    weekly = df.groupby("exam_week")[["marks", "attendance"]].mean().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(
        weekly["exam_week"],
        weekly["marks"],
        marker="o",
        color="#4C72B0",
        label="class avg marks",
    )
    plt.plot(
        weekly["exam_week"],
        weekly["attendance"],
        marker="s",
        color="#55A868",
        label="class avg attendance (%)",
    )
    plt.axhline(
        PASSING_MARKS_THRESHOLD,
        color="red",
        linestyle="dashed",
        linewidth=1.2,
        label=f"passing (<{PASSING_MARKS_THRESHOLD})",
    )
    plt.axhline(
        MIN_ATTENDANCE_PERCENTAGE,
        color="orange",
        linestyle="dashed",
        linewidth=1.2,
        label=f"attendance min (<{MIN_ATTENDANCE_PERCENTAGE}%)",
    )
    plt.title("Class Average Trend: Marks and Attendance")
    plt.xlabel("Exam week")
    plt.ylabel("Value")
    plt.xticks(weekly["exam_week"])
    plt.grid(linestyle=":", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)
    plt.close()
    print(f"Saved -> {output_path}")


# ---------------------------------------------------------------------------
# Section 6: Project Risk Application
# ---------------------------------------------------------------------------
def apply_trend_risk(trend_df: pd.DataFrame) -> pd.DataFrame:
    enriched = trend_df.copy()
    enriched["marks_declining"] = enriched["marks_slope_per_week"] < DECLINING_SLOPE_LIMIT
    enriched["attendance_declining"] = (
        enriched["attendance_slope_per_week"] < DECLINING_SLOPE_LIMIT
    )
    enriched["marks_sudden_drop"] = (
        enriched["marks_max_weekly_drop"] <= SUDDEN_DROP_LIMIT_MARKS
    )
    enriched["attendance_sudden_drop"] = (
        enriched["attendance_max_weekly_drop"] <= SUDDEN_DROP_LIMIT_ATTENDANCE
    )
    enriched["last_below_marks_threshold"] = (
        enriched["last_marks"] < PASSING_MARKS_THRESHOLD
    )
    enriched["last_below_attendance_threshold"] = (
        enriched["last_attendance"] < MIN_ATTENDANCE_PERCENTAGE
    )
    enriched["at_risk"] = (
        enriched["marks_declining"]
        | enriched["attendance_declining"]
        | enriched["marks_sudden_drop"]
        | enriched["attendance_sudden_drop"]
        | enriched["last_below_marks_threshold"]
        | enriched["last_below_attendance_threshold"]
    )
    return enriched


def print_trend_table(trend_df: pd.DataFrame) -> None:
    print("\n--- Per-Student Trend Summary ---")
    cols = [
        "name",
        "first_marks",
        "last_marks",
        "marks_slope_per_week",
        "marks_max_weekly_drop",
        "first_attendance",
        "last_attendance",
        "attendance_slope_per_week",
        "attendance_max_weekly_drop",
    ]
    print(trend_df[cols].round(2).to_string(index=False))


def print_risk_table(trend_df: pd.DataFrame) -> None:
    print("\n--- Trend-Aligned Risk Table ---")
    cols = [
        "name",
        "marks_slope_per_week",
        "attendance_slope_per_week",
        "marks_declining",
        "attendance_declining",
        "marks_sudden_drop",
        "attendance_sudden_drop",
        "last_below_marks_threshold",
        "last_below_attendance_threshold",
        "at_risk",
    ]
    print(trend_df[cols].round(2).to_string(index=False))
    at_risk_names = trend_df.loc[trend_df["at_risk"], "name"].tolist()
    print(f"\nTotal students  : {len(trend_df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 7: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Input file : {INPUT_CSV_PATH}")
    print(f"Output dir : {OUTPUT_DIR}")

    df = load_timeseries(INPUT_CSV_PATH)
    print(f"\nShape: {df.shape}")
    print(df.head(8))
    print("\nUnique students :", df["name"].nunique())
    print("Weeks observed  :", sorted(df["exam_week"].unique()))

    plot_per_student_lines(
        df=df,
        value_column="marks",
        title="Marks Trend per Student (across exam weeks)",
        ylabel="Marks",
        threshold=PASSING_MARKS_THRESHOLD,
        threshold_label=f"passing (<{PASSING_MARKS_THRESHOLD})",
        output_path=OUTPUT_DIR / "trend_marks_per_student.png",
    )
    plot_per_student_lines(
        df=df,
        value_column="attendance",
        title="Attendance Trend per Student (across exam weeks)",
        ylabel="Attendance (%)",
        threshold=MIN_ATTENDANCE_PERCENTAGE,
        threshold_label=f"minimum (<{MIN_ATTENDANCE_PERCENTAGE}%)",
        output_path=OUTPUT_DIR / "trend_attendance_per_student.png",
    )
    plot_class_average_lines(df, OUTPUT_DIR / "trend_class_average.png")

    trend_df = build_trend_summary(df)
    print_trend_table(trend_df)

    enriched = apply_trend_risk(trend_df)
    print_risk_table(enriched)

    output_csv = PROJECT_ROOT / "data" / "processed" / "students_trend_summary.csv"
    output_csv.parent.mkdir(parents=True, exist_ok=True)
    enriched.to_csv(output_csv, index=False)
    print(f"\nSaved trend summary -> {output_csv}")

    print("\nData Scientist Note:")
    print("- Trends require ordered, multi-point time data.")
    print("- A single dip is not a trend; sustained slope is.")
    print("- Saved images live in `outputs/` for reports and review.")


if __name__ == "__main__":
    main()
