"""Milestone 4.40: Visualizing Data Distributions Using Boxplots.

Project: At-Risk Student Detection System
Focus: read median, quartiles, spread, and outliers from boxplots and
       feed those insights into the project's at-risk decisions.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
from pathlib import Path

import matplotlib

matplotlib.use("Agg")  # safe, file-only rendering for any environment

import matplotlib.pyplot as plt  # noqa: E402
import pandas as pd  # noqa: E402


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PROJECT_ROOT = Path(__file__).resolve().parents[1]
INPUT_CSV_PATH = PROJECT_ROOT / "data" / "processed" / "students_standardized.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"

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
# Section 4: Five-Number Summary and IQR Outlier Math
# ---------------------------------------------------------------------------
def compute_box_summary(series: pd.Series, label: str) -> dict:
    q1 = float(series.quantile(0.25))
    q2 = float(series.quantile(0.50))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    lower_whisker = q1 - 1.5 * iqr
    upper_whisker = q3 + 1.5 * iqr
    outliers = series[(series < lower_whisker) | (series > upper_whisker)]
    summary = {
        "label": label,
        "min": float(series.min()),
        "q1": q1,
        "median": q2,
        "q3": q3,
        "max": float(series.max()),
        "iqr": iqr,
        "lower_whisker": lower_whisker,
        "upper_whisker": upper_whisker,
        "outliers": outliers.tolist(),
    }
    return summary


def print_box_summary(summary: dict) -> None:
    print(f"\n--- Box Summary :: {summary['label']} ---")
    print(f"  min            : {summary['min']:.2f}")
    print(f"  Q1 (25%)       : {summary['q1']:.2f}")
    print(f"  median (Q2)    : {summary['median']:.2f}")
    print(f"  Q3 (75%)       : {summary['q3']:.2f}")
    print(f"  max            : {summary['max']:.2f}")
    print(f"  IQR            : {summary['iqr']:.2f}")
    print(f"  lower whisker  : {summary['lower_whisker']:.2f}")
    print(f"  upper whisker  : {summary['upper_whisker']:.2f}")
    print(f"  outliers       : {summary['outliers']}")


# ---------------------------------------------------------------------------
# Section 5: Plotting Helpers
# ---------------------------------------------------------------------------
def plot_single_boxplot(
    series: pd.Series,
    title: str,
    ylabel: str,
    threshold: float,
    threshold_label: str,
    output_path: Path,
) -> None:
    plt.figure(figsize=(6, 6))
    plt.boxplot(
        series,
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="#4C72B0", color="black"),
        medianprops=dict(color="yellow", linewidth=2),
        flierprops=dict(marker="o", markerfacecolor="red", markersize=8),
    )
    plt.axhline(
        threshold,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=threshold_label,
    )
    plt.title(title)
    plt.ylabel(ylabel)
    plt.xticks([1], [series.name or "value"])
    plt.grid(axis="y", linestyle=":", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)
    plt.close()
    print(f"Saved -> {output_path}")


def plot_side_by_side_boxplots(
    marks_series: pd.Series,
    attendance_series: pd.Series,
    output_path: Path,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(12, 6))

    axes[0].boxplot(
        marks_series,
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="#4C72B0", color="black"),
        medianprops=dict(color="yellow", linewidth=2),
        flierprops=dict(marker="o", markerfacecolor="red", markersize=8),
    )
    axes[0].axhline(
        PASSING_MARKS_THRESHOLD,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=f"passing (<{PASSING_MARKS_THRESHOLD})",
    )
    axes[0].set_title("Boxplot of Marks")
    axes[0].set_ylabel("Marks")
    axes[0].set_xticks([1])
    axes[0].set_xticklabels(["marks"])
    axes[0].grid(axis="y", linestyle=":", alpha=0.5)
    axes[0].legend()

    axes[1].boxplot(
        attendance_series,
        vert=True,
        patch_artist=True,
        boxprops=dict(facecolor="#55A868", color="black"),
        medianprops=dict(color="yellow", linewidth=2),
        flierprops=dict(marker="o", markerfacecolor="red", markersize=8),
    )
    axes[1].axhline(
        MIN_ATTENDANCE_PERCENTAGE,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=f"minimum (<{MIN_ATTENDANCE_PERCENTAGE}%)",
    )
    axes[1].set_title("Boxplot of Attendance")
    axes[1].set_ylabel("Attendance (%)")
    axes[1].set_xticks([1])
    axes[1].set_xticklabels(["attendance"])
    axes[1].grid(axis="y", linestyle=":", alpha=0.5)
    axes[1].legend()

    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)
    plt.close()
    print(f"Saved -> {output_path}")


# ---------------------------------------------------------------------------
# Section 6: Pattern Reading
# ---------------------------------------------------------------------------
def report_spread_comparison(marks_summary: dict, attendance_summary: dict) -> None:
    print("\n--- Spread Comparison ---")
    print(
        f"  marks IQR      = {marks_summary['iqr']:.2f}, "
        f"attendance IQR = {attendance_summary['iqr']:.2f}"
    )
    if marks_summary["iqr"] > attendance_summary["iqr"]:
        print("  Marks shows wider middle 50% spread -> less consistent performance.")
    elif marks_summary["iqr"] < attendance_summary["iqr"]:
        print("  Attendance shows wider middle 50% spread -> less consistent attendance.")
    else:
        print("  Both columns share the same middle-50% spread.")


# ---------------------------------------------------------------------------
# Section 7: Project Risk Application
# ---------------------------------------------------------------------------
def add_risk_columns(df: pd.DataFrame, marks_summary: dict, attendance_summary: dict) -> pd.DataFrame:
    enriched = df.copy()
    enriched["below_marks_threshold"] = enriched["marks"] < PASSING_MARKS_THRESHOLD
    enriched["below_attendance_threshold"] = (
        enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE
    )
    enriched["in_lower_quartile_marks"] = enriched["marks"] <= marks_summary["q1"]
    enriched["in_lower_quartile_attendance"] = (
        enriched["attendance"] <= attendance_summary["q1"]
    )
    enriched["marks_outlier"] = (
        (enriched["marks"] < marks_summary["lower_whisker"])
        | (enriched["marks"] > marks_summary["upper_whisker"])
    )
    enriched["attendance_outlier"] = (
        (enriched["attendance"] < attendance_summary["lower_whisker"])
        | (enriched["attendance"] > attendance_summary["upper_whisker"])
    )
    enriched["at_risk"] = (
        enriched["below_marks_threshold"]
        | enriched["below_attendance_threshold"]
        | enriched["in_lower_quartile_marks"]
        | enriched["in_lower_quartile_attendance"]
        | enriched["marks_outlier"]
        | enriched["attendance_outlier"]
    )
    return enriched


def print_risk_table(df: pd.DataFrame) -> None:
    print("\n--- Boxplot-Aligned Risk Table ---")
    cols = [
        "name",
        "marks",
        "attendance",
        "in_lower_quartile_marks",
        "in_lower_quartile_attendance",
        "marks_outlier",
        "attendance_outlier",
        "at_risk",
    ]
    print(df[cols].to_string(index=False))
    at_risk_names = df.loc[df["at_risk"], "name"].tolist()
    print(f"\nTotal students  : {len(df)}")
    print(f"At-risk count   : {len(at_risk_names)}")
    print(f"At-risk students: {at_risk_names}")


# ---------------------------------------------------------------------------
# Section 8: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    print("Project: At-Risk Student Detection System")
    print(f"Input file : {INPUT_CSV_PATH}")
    print(f"Output dir : {OUTPUT_DIR}")

    df = load_dataframe(INPUT_CSV_PATH)
    if "at_risk" in df.columns:
        df = df.drop(columns=["at_risk"])
    print(f"\nShape: {df.shape}")
    print(df.head())

    marks_summary = compute_box_summary(df["marks"], "marks")
    attendance_summary = compute_box_summary(df["attendance"], "attendance")
    print_box_summary(marks_summary)
    print_box_summary(attendance_summary)

    plot_single_boxplot(
        series=df["marks"].rename("marks"),
        title="Boxplot of Marks",
        ylabel="Marks",
        threshold=PASSING_MARKS_THRESHOLD,
        threshold_label=f"passing (<{PASSING_MARKS_THRESHOLD})",
        output_path=OUTPUT_DIR / "boxplot_marks.png",
    )
    plot_single_boxplot(
        series=df["attendance"].rename("attendance"),
        title="Boxplot of Attendance",
        ylabel="Attendance (%)",
        threshold=MIN_ATTENDANCE_PERCENTAGE,
        threshold_label=f"minimum (<{MIN_ATTENDANCE_PERCENTAGE}%)",
        output_path=OUTPUT_DIR / "boxplot_attendance.png",
    )
    plot_side_by_side_boxplots(
        marks_series=df["marks"],
        attendance_series=df["attendance"],
        output_path=OUTPUT_DIR / "boxplot_marks_vs_attendance.png",
    )

    report_spread_comparison(marks_summary, attendance_summary)

    enriched = add_risk_columns(df, marks_summary, attendance_summary)
    print_risk_table(enriched)

    print("\nData Scientist Note:")
    print("- Boxplots reveal median, quartiles, spread, and outliers visually.")
    print("- Lower-quartile and IQR outliers are strong project risk signals.")
    print("- Saved images live in `outputs/` for reports and review.")


if __name__ == "__main__":
    main()
