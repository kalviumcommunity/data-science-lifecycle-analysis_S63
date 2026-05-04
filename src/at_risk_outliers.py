"""Milestone 4.43: Detecting Outliers (with project-aware interpretation).

Project: At-Risk Student Detection System
Focus: locate students who do not fit the typical pattern, classify them
       into meaningful project categories, and recommend an action -
       NEVER delete them blindly.

Constraints honored:
- No complex math beyond IQR comparisons.
- No automatic removal of outlier rows.
- Each outlier carries a category + recommended action.
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
SNAPSHOT_CSV = PROJECT_ROOT / "data" / "processed" / "students_standardized.csv"
TIMESERIES_CSV = PROJECT_ROOT / "data" / "raw" / "students_timeseries.csv"
OUTPUT_DIR = PROJECT_ROOT / "outputs"
PROCESSED_DIR = PROJECT_ROOT / "data" / "processed"

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75
HIGH_MARKS_THRESHOLD = 75
HIGH_ATTENDANCE_THRESHOLD = 80
EXTREME_LOW_MARKS = 40

OUTLIER_NONE = "Typical"
OUTLIER_UNUSUAL_PERFORMER = "Type 1: Unusual Performer"     # low att + high marks
OUTLIER_STRUGGLING_STUDENT = "Type 2: Struggling Student"   # high att + low marks
OUTLIER_CRITICAL_CASE = "Type 3: Critical Case"             # both low
OUTLIER_STATISTICAL = "Type 4: Statistical (IQR)"           # outside IQR whiskers

OUTLIER_COLORS = {
    OUTLIER_UNUSUAL_PERFORMER: "#9467bd",     # purple
    OUTLIER_STRUGGLING_STUDENT: "#ff7f0e",    # orange
    OUTLIER_CRITICAL_CASE: "#d62728",         # red
    OUTLIER_STATISTICAL: "#8c564b",           # brown
    OUTLIER_NONE: "#2ca02c",                  # green
}

OUTLIER_ACTIONS = {
    OUTLIER_UNUSUAL_PERFORMER: "Verify integrity, then mentor for engagement.",
    OUTLIER_STRUGGLING_STUDENT: "Offer learning support / tutoring; check method.",
    OUTLIER_CRITICAL_CASE: "Immediate counseling + parent meeting.",
    OUTLIER_STATISTICAL: "Investigate before any action; statistical edge case.",
    OUTLIER_NONE: "Monitor as part of regular review.",
}


# ---------------------------------------------------------------------------
# Section 3: Loaders
# ---------------------------------------------------------------------------
def load_snapshot(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    df = pd.read_csv(csv_path)
    if "at_risk" in df.columns:
        df = df.drop(columns=["at_risk"])
    return df


def load_last_week_snapshot(csv_path: Path) -> pd.DataFrame:
    if not csv_path.exists():
        raise FileNotFoundError(f"CSV not found at: {csv_path}")
    df = pd.read_csv(csv_path).sort_values(["name", "exam_week"])
    last = df.groupby("name").tail(1).reset_index(drop=True)
    return last[["name", "marks", "attendance"]]


# ---------------------------------------------------------------------------
# Section 4: IQR-Based Detection (boxplot rule)
# ---------------------------------------------------------------------------
def compute_iqr_bounds(series: pd.Series) -> dict:
    q1 = float(series.quantile(0.25))
    q3 = float(series.quantile(0.75))
    iqr = q3 - q1
    return {
        "q1": q1,
        "q3": q3,
        "iqr": iqr,
        "lower": q1 - 1.5 * iqr,
        "upper": q3 + 1.5 * iqr,
    }


def is_iqr_outlier(value: float, bounds: dict) -> bool:
    return value < bounds["lower"] or value > bounds["upper"]


# ---------------------------------------------------------------------------
# Section 5: Project-Aware Classification (no automatic removal)
# ---------------------------------------------------------------------------
def classify_outlier_type(
    row: pd.Series,
    marks_bounds: dict,
    attendance_bounds: dict,
) -> str:
    marks = row["marks"]
    attendance = row["attendance"]

    if marks < PASSING_MARKS_THRESHOLD and attendance < MIN_ATTENDANCE_PERCENTAGE:
        return OUTLIER_CRITICAL_CASE
    if marks < PASSING_MARKS_THRESHOLD and attendance >= HIGH_ATTENDANCE_THRESHOLD:
        return OUTLIER_STRUGGLING_STUDENT
    if marks >= HIGH_MARKS_THRESHOLD and attendance < MIN_ATTENDANCE_PERCENTAGE:
        return OUTLIER_UNUSUAL_PERFORMER
    if is_iqr_outlier(marks, marks_bounds) or is_iqr_outlier(
        attendance, attendance_bounds
    ):
        return OUTLIER_STATISTICAL
    return OUTLIER_NONE


def add_outlier_columns(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    marks_bounds = compute_iqr_bounds(enriched["marks"])
    attendance_bounds = compute_iqr_bounds(enriched["attendance"])

    enriched["marks_iqr_outlier"] = enriched["marks"].apply(
        lambda v: is_iqr_outlier(v, marks_bounds)
    )
    enriched["attendance_iqr_outlier"] = enriched["attendance"].apply(
        lambda v: is_iqr_outlier(v, attendance_bounds)
    )
    enriched["outlier_type"] = enriched.apply(
        lambda row: classify_outlier_type(row, marks_bounds, attendance_bounds),
        axis=1,
    )
    enriched["is_outlier"] = enriched["outlier_type"] != OUTLIER_NONE
    enriched["recommended_action"] = enriched["outlier_type"].map(OUTLIER_ACTIONS)
    return enriched, marks_bounds, attendance_bounds


# ---------------------------------------------------------------------------
# Section 6: Plotting (categorized scatter)
# ---------------------------------------------------------------------------
def plot_outlier_scatter(
    df: pd.DataFrame,
    title: str,
    output_path: Path,
) -> None:
    plt.figure(figsize=(10, 7))
    for outlier_type, color in OUTLIER_COLORS.items():
        subset = df[df["outlier_type"] == outlier_type]
        if subset.empty:
            continue
        plt.scatter(
            subset["attendance"],
            subset["marks"],
            s=160,
            c=color,
            edgecolor="black",
            label=f"{outlier_type} ({len(subset)})",
        )
        for _, row in subset.iterrows():
            plt.annotate(
                row["name"],
                (row["attendance"], row["marks"]),
                xytext=(6, 6),
                textcoords="offset points",
                fontsize=9,
            )

    plt.axhline(
        PASSING_MARKS_THRESHOLD,
        color="red",
        linestyle="dashed",
        linewidth=1.3,
        label=f"passing (<{PASSING_MARKS_THRESHOLD})",
    )
    plt.axhline(
        HIGH_MARKS_THRESHOLD,
        color="green",
        linestyle="dotted",
        linewidth=1.0,
        label=f"high marks (>={HIGH_MARKS_THRESHOLD})",
    )
    plt.axvline(
        MIN_ATTENDANCE_PERCENTAGE,
        color="purple",
        linestyle="dashed",
        linewidth=1.3,
        label=f"attendance min (<{MIN_ATTENDANCE_PERCENTAGE}%)",
    )
    plt.axvline(
        HIGH_ATTENDANCE_THRESHOLD,
        color="teal",
        linestyle="dotted",
        linewidth=1.0,
        label=f"high attendance (>={HIGH_ATTENDANCE_THRESHOLD}%)",
    )

    plt.title(title)
    plt.xlabel("Attendance (%)")
    plt.ylabel("Marks")
    plt.xlim(0, 105)
    plt.ylim(0, 105)
    plt.grid(linestyle=":", alpha=0.5)
    plt.legend(loc="lower right", fontsize=8)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)
    plt.close()
    print(f"Saved -> {output_path}")


# ---------------------------------------------------------------------------
# Section 7: Reporting
# ---------------------------------------------------------------------------
def print_iqr_bounds(label: str, bounds: dict) -> None:
    print(f"\n--- IQR Bounds :: {label} ---")
    print(
        f"  Q1={bounds['q1']:.2f}, Q3={bounds['q3']:.2f}, IQR={bounds['iqr']:.2f}, "
        f"lower={bounds['lower']:.2f}, upper={bounds['upper']:.2f}"
    )


def print_outlier_breakdown(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- Outlier Breakdown :: {label} ---")
    for outlier_type in [
        OUTLIER_NONE,
        OUTLIER_UNUSUAL_PERFORMER,
        OUTLIER_STRUGGLING_STUDENT,
        OUTLIER_CRITICAL_CASE,
        OUTLIER_STATISTICAL,
    ]:
        names = df.loc[df["outlier_type"] == outlier_type, "name"].tolist()
        action = OUTLIER_ACTIONS[outlier_type]
        print(f"  {outlier_type:<32}: {len(names):>2} -> {names}")
        print(f"    action: {action}")


def print_outlier_table(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- Outlier Detail Table :: {label} ---")
    cols = [
        "name",
        "marks",
        "attendance",
        "marks_iqr_outlier",
        "attendance_iqr_outlier",
        "outlier_type",
        "is_outlier",
    ]
    print(df[cols].to_string(index=False))


# ---------------------------------------------------------------------------
# Section 8: Main Execution
# ---------------------------------------------------------------------------
def run_for_dataset(
    df: pd.DataFrame,
    label: str,
    scatter_filename: str,
    csv_filename: str,
) -> None:
    print(f"\n=== Running outlier analysis on: {label} ===")
    print(f"Shape: {df.shape}")
    print(df.head())

    enriched, marks_bounds, attendance_bounds = add_outlier_columns(df)
    print_iqr_bounds("marks", marks_bounds)
    print_iqr_bounds("attendance", attendance_bounds)

    print_outlier_breakdown(enriched, label)
    print_outlier_table(enriched, label)

    plot_outlier_scatter(
        df=enriched,
        title=f"Outlier Categories - {label}",
        output_path=OUTPUT_DIR / scatter_filename,
    )

    out_csv = PROCESSED_DIR / csv_filename
    out_csv.parent.mkdir(parents=True, exist_ok=True)
    enriched.to_csv(out_csv, index=False)
    print(f"Saved -> {out_csv}")


def main() -> None:
    print("Project: At-Risk Student Detection System")
    print("Milestone 4.43 :: Outlier Detection (categorized, never auto-removed)")
    print(f"Snapshot file   : {SNAPSHOT_CSV}")
    print(f"Time-series file: {TIMESERIES_CSV}")
    print(f"Output dir      : {OUTPUT_DIR}")
    print(f"Processed dir   : {PROCESSED_DIR}")

    snapshot_df = load_snapshot(SNAPSHOT_CSV)
    last_week_df = load_last_week_snapshot(TIMESERIES_CSV)

    run_for_dataset(
        df=snapshot_df,
        label="snapshot dataset",
        scatter_filename="outliers_snapshot.png",
        csv_filename="students_outliers_snapshot.csv",
    )
    run_for_dataset(
        df=last_week_df,
        label="last-week (time-series)",
        scatter_filename="outliers_last_week.png",
        csv_filename="students_outliers_last_week.csv",
    )

    print("\nData Scientist Note:")
    print("- Outliers are NEVER deleted automatically.")
    print("- Each outlier carries a category and a recommended action.")
    print("- Statistical (IQR) and project-rule outliers are tracked separately.")


if __name__ == "__main__":
    main()
