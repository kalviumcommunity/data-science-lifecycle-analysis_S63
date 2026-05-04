"""Milestone 4.42: Exploring Relationships Between Variables Using Scatter Plots.

Project: At-Risk Student Detection System
Focus: read the marks-attendance relationship visually and translate the
       four scatter quadrants into project risk decisions.

Constraints honored:
- No correlation coefficient is computed.
- No regression line is fitted.
- The script is purely visual + rule-based.
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

PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75


# Quadrant labels (visual reasoning, no math beyond comparisons)
QUADRANT_SAFE = "Safe"
QUADRANT_LOW_MARKS_ONLY = "Low marks only"
QUADRANT_LOW_ATTENDANCE_ONLY = "Low attendance only"
QUADRANT_HIGH_RISK = "High risk (both low)"

QUADRANT_COLORS = {
    QUADRANT_SAFE: "#2ca02c",                # green
    QUADRANT_LOW_MARKS_ONLY: "#ff7f0e",      # orange
    QUADRANT_LOW_ATTENDANCE_ONLY: "#1f77b4", # blue
    QUADRANT_HIGH_RISK: "#d62728",           # red
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
# Section 4: Quadrant Classification
# ---------------------------------------------------------------------------
def classify_quadrant(row: pd.Series) -> str:
    low_marks = row["marks"] < PASSING_MARKS_THRESHOLD
    low_attendance = row["attendance"] < MIN_ATTENDANCE_PERCENTAGE
    if low_marks and low_attendance:
        return QUADRANT_HIGH_RISK
    if low_marks and not low_attendance:
        return QUADRANT_LOW_MARKS_ONLY
    if not low_marks and low_attendance:
        return QUADRANT_LOW_ATTENDANCE_ONLY
    return QUADRANT_SAFE


def add_quadrant_column(df: pd.DataFrame) -> pd.DataFrame:
    enriched = df.copy()
    enriched["quadrant"] = enriched.apply(classify_quadrant, axis=1)
    enriched["at_risk"] = enriched["quadrant"] != QUADRANT_SAFE
    return enriched


# ---------------------------------------------------------------------------
# Section 5: Visual Pattern Reading (no statistics)
# ---------------------------------------------------------------------------
def describe_visual_pattern(df: pd.DataFrame) -> None:
    print("\n--- Visual Pattern Reading ---")
    high_marks_high_att = (
        (df["marks"] >= PASSING_MARKS_THRESHOLD)
        & (df["attendance"] >= MIN_ATTENDANCE_PERCENTAGE)
    ).sum()
    low_marks_low_att = (
        (df["marks"] < PASSING_MARKS_THRESHOLD)
        & (df["attendance"] < MIN_ATTENDANCE_PERCENTAGE)
    ).sum()
    pattern_supportive = high_marks_high_att + low_marks_low_att
    if pattern_supportive >= len(df) - 2:
        verdict = "an upward visual trend (high attendance tends to come with high marks)"
    else:
        verdict = "a mixed cloud (no single direction dominates)"
    print(f"Points supporting the upward pattern : {pattern_supportive}/{len(df)}")
    print(f"Visual reading                        : {verdict}")


# ---------------------------------------------------------------------------
# Section 6: Plotting Helper
# ---------------------------------------------------------------------------
def plot_scatter_with_quadrants(
    df: pd.DataFrame,
    title: str,
    output_path: Path,
) -> None:
    plt.figure(figsize=(10, 7))

    for quadrant_label, color in QUADRANT_COLORS.items():
        subset = df[df["quadrant"] == quadrant_label]
        if subset.empty:
            continue
        plt.scatter(
            subset["attendance"],
            subset["marks"],
            s=140,
            c=color,
            edgecolor="black",
            label=f"{quadrant_label} ({len(subset)})",
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
        linewidth=1.4,
        label=f"passing (marks <{PASSING_MARKS_THRESHOLD})",
    )
    plt.axvline(
        MIN_ATTENDANCE_PERCENTAGE,
        color="purple",
        linestyle="dashed",
        linewidth=1.4,
        label=f"attendance min (<{MIN_ATTENDANCE_PERCENTAGE}%)",
    )

    plt.title(title)
    plt.xlabel("Attendance (%)")
    plt.ylabel("Marks")
    plt.xlim(0, 105)
    plt.ylim(0, 105)
    plt.grid(linestyle=":", alpha=0.5)
    plt.legend(loc="lower right", fontsize=9)
    plt.tight_layout()
    output_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(output_path, dpi=120)
    plt.close()
    print(f"Saved -> {output_path}")


# ---------------------------------------------------------------------------
# Section 7: Reporting
# ---------------------------------------------------------------------------
def print_quadrant_breakdown(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- Quadrant Breakdown :: {label} ---")
    counts = df["quadrant"].value_counts()
    for quadrant in [
        QUADRANT_SAFE,
        QUADRANT_LOW_MARKS_ONLY,
        QUADRANT_LOW_ATTENDANCE_ONLY,
        QUADRANT_HIGH_RISK,
    ]:
        names = df.loc[df["quadrant"] == quadrant, "name"].tolist()
        print(f"  {quadrant:<22}: {counts.get(quadrant, 0)} -> {names}")


def print_risk_table(df: pd.DataFrame, label: str) -> None:
    print(f"\n--- Scatter-Aligned Risk Table :: {label} ---")
    cols = ["name", "marks", "attendance", "quadrant", "at_risk"]
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
    print(f"Snapshot file   : {SNAPSHOT_CSV}")
    print(f"Time-series file: {TIMESERIES_CSV}")
    print(f"Output dir      : {OUTPUT_DIR}")

    # --- Source 1: standardized snapshot ------------------------------------
    snapshot_df = load_snapshot(SNAPSHOT_CSV)
    print(f"\nSnapshot shape: {snapshot_df.shape}")
    print(snapshot_df.head())

    snapshot_enriched = add_quadrant_column(snapshot_df)
    describe_visual_pattern(snapshot_enriched)
    print_quadrant_breakdown(snapshot_enriched, "snapshot dataset")
    plot_scatter_with_quadrants(
        df=snapshot_enriched,
        title="Marks vs Attendance (snapshot dataset)",
        output_path=OUTPUT_DIR / "scatter_marks_vs_attendance_snapshot.png",
    )
    print_risk_table(snapshot_enriched, "snapshot dataset")

    # --- Source 2: last week from time-series -------------------------------
    last_week_df = load_last_week_snapshot(TIMESERIES_CSV)
    print(f"\nTime-series last-week shape: {last_week_df.shape}")
    print(last_week_df.head())

    last_week_enriched = add_quadrant_column(last_week_df)
    describe_visual_pattern(last_week_enriched)
    print_quadrant_breakdown(last_week_enriched, "last-week (time-series)")
    plot_scatter_with_quadrants(
        df=last_week_enriched,
        title="Marks vs Attendance (last-week of time-series)",
        output_path=OUTPUT_DIR / "scatter_marks_vs_attendance_last_week.png",
    )
    print_risk_table(last_week_enriched, "last-week (time-series)")

    print("\nData Scientist Note:")
    print("- Each point = one student in (attendance, marks) space.")
    print("- The two threshold lines split the chart into four risk quadrants.")
    print("- Correlation is not assumed; the chart is read visually only.")


if __name__ == "__main__":
    main()
