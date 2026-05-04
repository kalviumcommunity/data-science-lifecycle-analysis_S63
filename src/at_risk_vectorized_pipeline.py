"""Milestone 4.25: Applying Vectorized Operations Instead of Python Loops.

Project: At-Risk Student Detection System
Focus: replace loop-based decision logic with NumPy vectorization, and
       prove the efficiency gain with a small benchmark.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
import time

import numpy as np


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75
BENCHMARK_STUDENT_COUNT = 100_000


# ---------------------------------------------------------------------------
# Section 3: Project Data
# ---------------------------------------------------------------------------
def load_student_data() -> dict[str, list]:
    return {
        "names": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        "marks": [88, 49, 72, 83, 95],
        "attendance": [91, 79, 70, 86, 98],
    }


def to_arrays(student_data: dict[str, list]) -> tuple[np.ndarray, np.ndarray]:
    marks = np.array(student_data["marks"], dtype=float)
    attendance = np.array(student_data["attendance"], dtype=float)
    return marks, attendance


# ---------------------------------------------------------------------------
# Section 4: Loop-Based Risk Detection (BEFORE)
# ---------------------------------------------------------------------------
def detect_at_risk_loop(marks: np.ndarray, attendance: np.ndarray) -> list[bool]:
    """Traditional Python loop version of at-risk detection."""
    risk_flags: list[bool] = []
    for index in range(len(marks)):
        is_low_marks = marks[index] < PASSING_MARKS_THRESHOLD
        is_low_attendance = attendance[index] < MIN_ATTENDANCE_PERCENTAGE
        risk_flags.append(bool(is_low_marks or is_low_attendance))
    return risk_flags


# ---------------------------------------------------------------------------
# Section 5: Vectorized Risk Detection (AFTER)
# ---------------------------------------------------------------------------
def detect_at_risk_vectorized(marks: np.ndarray, attendance: np.ndarray) -> np.ndarray:
    """Vectorized version: one expression replaces the entire loop."""
    return (marks < PASSING_MARKS_THRESHOLD) | (attendance < MIN_ATTENDANCE_PERCENTAGE)


# ---------------------------------------------------------------------------
# Section 6: Shape Safety
# ---------------------------------------------------------------------------
def ensure_same_shape(array_a: np.ndarray, array_b: np.ndarray) -> None:
    if array_a.shape != array_b.shape:
        raise ValueError(
            f"Shape mismatch: {array_a.shape} vs {array_b.shape}. "
            "Vectorized math requires identical shapes."
        )


# ---------------------------------------------------------------------------
# Section 7: Reporting
# ---------------------------------------------------------------------------
def print_risk_table(
    names: list[str],
    marks: np.ndarray,
    attendance: np.ndarray,
    risk_flags: np.ndarray,
) -> None:
    print("\n--- Vectorized At-Risk Detection ---")
    print(f"{'Name':<8} {'Marks':>6} {'Attend%':>8} {'Status':>10}")
    print("-" * 38)
    for index, name in enumerate(names):
        status = "At Risk" if bool(risk_flags[index]) else "Safe"
        print(f"{name:<8} {marks[index]:>6.1f} {attendance[index]:>8.1f} {status:>10}")
    print("-" * 38)
    print(f"At-risk count : {int(np.sum(risk_flags))}")


def print_boolean_array_demo(marks: np.ndarray, attendance: np.ndarray) -> None:
    print("\n--- Boolean Array Demo ---")
    print("marks < 50          :", marks < PASSING_MARKS_THRESHOLD)
    print("attendance < 75     :", attendance < MIN_ATTENDANCE_PERCENTAGE)
    combined = (marks < PASSING_MARKS_THRESHOLD) | (attendance < MIN_ATTENDANCE_PERCENTAGE)
    print("combined risk mask  :", combined)


# ---------------------------------------------------------------------------
# Section 8: Benchmark - Loop vs Vectorized
# ---------------------------------------------------------------------------
def benchmark_loop_vs_vectorized(num_students: int) -> dict[str, float]:
    """Generate a large dataset and time both implementations."""
    rng = np.random.default_rng(seed=42)
    marks = rng.uniform(0, 100, size=num_students)
    attendance = rng.uniform(0, 100, size=num_students)

    start_loop = time.perf_counter()
    flags_loop = detect_at_risk_loop(marks, attendance)
    loop_seconds = time.perf_counter() - start_loop

    start_vec = time.perf_counter()
    flags_vec = detect_at_risk_vectorized(marks, attendance)
    vectorized_seconds = time.perf_counter() - start_vec

    # Sanity check: results must agree.
    if not np.array_equal(np.array(flags_loop), flags_vec):
        raise RuntimeError("Loop and vectorized results disagree.")

    speedup = loop_seconds / vectorized_seconds if vectorized_seconds > 0 else float("inf")
    return {
        "students": num_students,
        "loop_seconds": loop_seconds,
        "vectorized_seconds": vectorized_seconds,
        "speedup_factor": speedup,
        "at_risk_count": int(np.sum(flags_vec)),
    }


def print_benchmark(report: dict[str, float]) -> None:
    print("\n--- Benchmark: Loop vs Vectorized ---")
    print(f"Dataset size       : {int(report['students'])} students")
    print(f"Loop runtime       : {report['loop_seconds']:.4f} sec")
    print(f"Vectorized runtime : {report['vectorized_seconds']:.4f} sec")
    print(f"Speedup factor     : {report['speedup_factor']:.1f}x")
    print(f"At-risk count      : {int(report['at_risk_count'])}")


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_data = load_student_data()
    marks, attendance = to_arrays(student_data)
    ensure_same_shape(marks, attendance)

    print_boolean_array_demo(marks, attendance)

    risk_flags = detect_at_risk_vectorized(marks, attendance)
    print_risk_table(student_data["names"], marks, attendance, risk_flags)

    benchmark_report = benchmark_loop_vs_vectorized(BENCHMARK_STUDENT_COUNT)
    print_benchmark(benchmark_report)

    print("\nData Scientist Note:")
    print("- Vectorization removed loops without changing results.")
    print("- The benchmark proves vectorized code scales for large datasets.")


if __name__ == "__main__":
    main()
