"""End-to-end runner for the At-Risk Student Detection System.

This single entry point runs the project's key analytical pipeline in the
right order so a reviewer can reproduce all outputs with one command:

    python run_project.py

It groups scripts into logical phases, prints a clear banner per phase,
and reports total wall-clock time.
"""

from __future__ import annotations

import subprocess
import sys
import time
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent
SRC_DIR = PROJECT_ROOT / "src"


PIPELINE_PHASES: list[tuple[str, list[str]]] = [
    (
        "Phase 1 - Data Inspection",
        [
            "at_risk_csv_loader.py",
            "at_risk_inspect_dataframe.py",
            "at_risk_shape_and_dtypes.py",
        ],
    ),
    (
        "Phase 2 - Data Cleaning",
        [
            "at_risk_missing_values_detection.py",
            "at_risk_missing_value_handling.py",
            "at_risk_duplicate_handling.py",
            "at_risk_standardize_columns.py",
        ],
    ),
    (
        "Phase 3 - Summary Statistics",
        [
            "at_risk_summary_statistics.py",
            "at_risk_compare_distributions.py",
        ],
    ),
    (
        "Phase 4 - Visualization (EDA)",
        [
            "at_risk_histograms.py",
            "at_risk_boxplots.py",
            "at_risk_scatter.py",
        ],
    ),
    (
        "Phase 5 - Time-Series Trends",
        [
            "at_risk_trends.py",
        ],
    ),
    (
        "Phase 6 - Outlier Detection",
        [
            "at_risk_outliers.py",
        ],
    ),
]


def banner(text: str, char: str = "=") -> None:
    line = char * 78
    print(f"\n{line}\n{text}\n{line}")


def run_script(script_name: str) -> tuple[bool, float]:
    script_path = SRC_DIR / script_name
    if not script_path.exists():
        print(f"  [SKIP] {script_name} not found at {script_path}")
        return False, 0.0

    print(f"\n>>> Running: {script_name}")
    started = time.perf_counter()
    completed = subprocess.run(
        [sys.executable, str(script_path)],
        cwd=str(PROJECT_ROOT),
        text=True,
    )
    elapsed = time.perf_counter() - started
    success = completed.returncode == 0
    flag = "OK" if success else "FAIL"
    print(f"<<< {flag} ({elapsed:.2f}s) :: {script_name}")
    return success, elapsed


def main() -> int:
    banner("AT-RISK STUDENT DETECTION SYSTEM :: FULL PROJECT RUN")
    print(f"Project root : {PROJECT_ROOT}")
    print(f"Source dir   : {SRC_DIR}")
    print(f"Python       : {sys.executable}")

    overall_started = time.perf_counter()
    total_scripts = 0
    failed_scripts: list[str] = []

    for phase_name, script_list in PIPELINE_PHASES:
        banner(phase_name, char="-")
        for script_name in script_list:
            total_scripts += 1
            success, _ = run_script(script_name)
            if not success:
                failed_scripts.append(script_name)

    overall_elapsed = time.perf_counter() - overall_started

    banner("PROJECT RUN SUMMARY")
    print(f"Total scripts : {total_scripts}")
    print(f"Successful    : {total_scripts - len(failed_scripts)}")
    print(f"Failed        : {len(failed_scripts)}")
    if failed_scripts:
        print("Failed list   :")
        for name in failed_scripts:
            print(f"  - {name}")
    print(f"Total time    : {overall_elapsed:.2f}s")

    print("\nKey artifacts to review:")
    print("  data/processed/students_cleaned.csv")
    print("  data/processed/students_deduplicated.csv")
    print("  data/processed/students_standardized.csv")
    print("  data/processed/students_trend_summary.csv")
    print("  data/processed/students_outliers_snapshot.csv")
    print("  data/processed/students_outliers_last_week.csv")
    print("  outputs/histogram_marks.png, histogram_attendance.png, histogram_marks_vs_attendance.png")
    print("  outputs/boxplot_marks.png, boxplot_attendance.png, boxplot_marks_vs_attendance.png")
    print("  outputs/scatter_marks_vs_attendance_snapshot.png")
    print("  outputs/scatter_marks_vs_attendance_last_week.png")
    print("  outputs/trend_marks_per_student.png, trend_attendance_per_student.png, trend_class_average.png")
    print("  outputs/outliers_snapshot.png, outliers_last_week.png")

    return 0 if not failed_scripts else 1


if __name__ == "__main__":
    sys.exit(main())
