"""Milestone 4.39: Visualizing Data Distributions Using Histograms.

Project: At-Risk Student Detection System
Focus: turn the standardized dataset into clear histograms for marks and
       attendance, and connect the visual patterns to risk decisions.
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
HIST_BIN_EDGES = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


# ---------------------------------------------------------------------------
# Section 3: Loader
# ---------------------------------------------------------------------------
def load_dataframe(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    return pd.read_csv(csv_path)


# ---------------------------------------------------------------------------
# Section 4: Bin-Level Frequency Reporting (text-side companion)
# ---------------------------------------------------------------------------
def report_bin_frequencies(series: pd.Series, label: str) -> None:
    binned = pd.cut(series, bins=HIST_BIN_EDGES, include_lowest=True)
    counts = binned.value_counts().sort_index()
    print(f"\n--- Bin Frequencies :: {label} ---")
    for interval, count in counts.items():
        print(f"  {str(interval):<14}: {count}")


# ---------------------------------------------------------------------------
# Section 5: Plotting Helpers
# ---------------------------------------------------------------------------
def plot_single_histogram(
    series: pd.Series,
    title: str,
    xlabel: str,
    threshold: float,
    threshold_label: str,
    output_path: Path,
) -> None:
    plt.figure(figsize=(8, 5))
    plt.hist(series, bins=HIST_BIN_EDGES, edgecolor="black", color="#4C72B0")
    plt.axvline(
        threshold,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=threshold_label,
    )
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel("Number of students")
    plt.xticks(HIST_BIN_EDGES)
    plt.grid(axis="y", linestyle=":", alpha=0.5)
    plt.legend()
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)
    plt.close()
    print(f"Saved -> {output_path}")


def plot_side_by_side_histograms(
    marks_series: pd.Series,
    attendance_series: pd.Series,
    output_path: Path,
) -> None:
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))

    axes[0].hist(marks_series, bins=HIST_BIN_EDGES, edgecolor="black", color="#4C72B0")
    axes[0].axvline(
        PASSING_MARKS_THRESHOLD,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=f"passing (<{PASSING_MARKS_THRESHOLD})",
    )
    axes[0].set_title("Marks Distribution")
    axes[0].set_xlabel("Marks")
    axes[0].set_ylabel("Number of students")
    axes[0].set_xticks(HIST_BIN_EDGES)
    axes[0].grid(axis="y", linestyle=":", alpha=0.5)
    axes[0].legend()

    axes[1].hist(
        attendance_series, bins=HIST_BIN_EDGES, edgecolor="black", color="#55A868"
    )
    axes[1].axvline(
        MIN_ATTENDANCE_PERCENTAGE,
        color="red",
        linestyle="dashed",
        linewidth=1.5,
        label=f"minimum (<{MIN_ATTENDANCE_PERCENTAGE}%)",
    )
    axes[1].set_title("Attendance Distribution")
    axes[1].set_xlabel("Attendance (%)")
    axes[1].set_ylabel("Number of students")
    axes[1].set_xticks(HIST_BIN_EDGES)
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
def describe_shape(series: pd.Series, label: str) -> None:
    mean_value = series.mean()
    median_value = series.median()
    skew_signal = (
        "balanced (mean ~ median)"
        if abs(mean_value - median_value) < 1
        else (
            "left-skewed (mean < median)"
            if mean_value < median_value
            else "right-skewed (mean > median)"
        )
    )
    print(
        f"{label:<11}: mean={mean_value:.2f}, median={median_value:.2f} -> {skew_signal}"
    )


def report_visual_insights(df: pd.DataFrame) -> None:
    print("\n--- Visual Insights ---")
    describe_shape(df["marks"], "marks")
    describe_shape(df["attendance"], "attendance")

    low_marks_count = int((df["marks"] < PASSING_MARKS_THRESHOLD).sum())
    low_attendance_count = int((df["attendance"] < MIN_ATTENDANCE_PERCENTAGE).sum())

    print(f"\nStudents with marks below {PASSING_MARKS_THRESHOLD}      : {low_marks_count}")
    print(
        f"Students with attendance below {MIN_ATTENDANCE_PERCENTAGE}% : "
        f"{low_attendance_count}"
    )

    marks_widest_range = (df["marks"].max() - df["marks"].min())
    attendance_range = (df["attendance"].max() - df["attendance"].min())
    if marks_widest_range > attendance_range:
        print("Marks histogram is more spread out than attendance histogram.")
    else:
        print("Attendance histogram is more spread out than marks histogram.")


# ---------------------------------------------------------------------------
# Section 7: Project Risk Application
# ---------------------------------------------------------------------------
def add_risk_status(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["at_risk"] = (
        (enriched["marks"] < PASSING_MARKS_THRESHOLD)
        | (enriched["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    )
    return enriched


def print_risk_summary(df: pd.DataFrame) -> None:
    print("\n--- Risk Summary Aligned to Histograms ---")
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
    print(f"Input file : {INPUT_CSV_PATH}")
    print(f"Output dir : {OUTPUT_DIR}")

    df = load_dataframe(INPUT_CSV_PATH)
    if "at_risk" in df.columns:
        df = df.drop(columns=["at_risk"])

    print(f"\nShape: {df.shape}")
    print(df.head())

    report_bin_frequencies(df["marks"], "marks")
    report_bin_frequencies(df["attendance"], "attendance")

    plot_single_histogram(
        series=df["marks"],
        title="Histogram of Marks",
        xlabel="Marks",
        threshold=PASSING_MARKS_THRESHOLD,
        threshold_label=f"passing (<{PASSING_MARKS_THRESHOLD})",
        output_path=OUTPUT_DIR / "histogram_marks.png",
    )
    plot_single_histogram(
        series=df["attendance"],
        title="Histogram of Attendance",
        xlabel="Attendance (%)",
        threshold=MIN_ATTENDANCE_PERCENTAGE,
        threshold_label=f"minimum (<{MIN_ATTENDANCE_PERCENTAGE}%)",
        output_path=OUTPUT_DIR / "histogram_attendance.png",
    )
    plot_side_by_side_histograms(
        marks_series=df["marks"],
        attendance_series=df["attendance"],
        output_path=OUTPUT_DIR / "histogram_marks_vs_attendance.png",
    )

    report_visual_insights(df)

    enriched = add_risk_status(df)
    print_risk_summary(enriched)

    print("\nData Scientist Note:")
    print("- Histograms reveal where the bulk of values fall by bin.")
    print("- The dashed threshold line connects visuals to project risk rules.")
    print("- Saved images live in `outputs/` for reports and review.")


if __name__ == "__main__":
    main()
