"""Milestone 4.24: Basic Mathematical Operations on NumPy Arrays.

Project: At-Risk Student Detection System
Focus: replace per-student loops with vectorized array math for clarity,
       speed, and scalability.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
import numpy as np


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
PASSING_MARKS_THRESHOLD = 50
MIN_ATTENDANCE_PERCENTAGE = 75

GRACE_BONUS_POINTS = 2          # bonus added after re-evaluation policy
LATE_PENALTY_POINTS = 1         # penalty subtracted for late submissions
ATTENDANCE_SCALE_FACTOR = 1.05  # 5% boost when attendance is normalized


# ---------------------------------------------------------------------------
# Section 3: Project Data
# ---------------------------------------------------------------------------
def load_student_data() -> dict[str, list]:
    return {
        "names": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        "marks": [88, 49, 72, 83, 95],
        "attendance": [91, 79, 70, 86, 98],
    }


def to_arrays(student_data: dict[str, list]) -> dict[str, np.ndarray]:
    return {
        "marks": np.array(student_data["marks"], dtype=float),
        "attendance": np.array(student_data["attendance"], dtype=float),
    }


# ---------------------------------------------------------------------------
# Section 4: Element-Wise and Scalar Math
# ---------------------------------------------------------------------------
def apply_grace_bonus(marks: np.ndarray) -> np.ndarray:
    """Add a fixed grace bonus to all marks (scalar operation)."""
    return marks + GRACE_BONUS_POINTS


def apply_late_penalty(marks: np.ndarray) -> np.ndarray:
    """Subtract a late-submission penalty from all marks (scalar operation)."""
    return marks - LATE_PENALTY_POINTS


def normalize_attendance(attendance: np.ndarray) -> np.ndarray:
    """Scale attendance by a normalization factor and clip at 100."""
    scaled = attendance * ATTENDANCE_SCALE_FACTOR
    return np.minimum(scaled, 100.0)


def compute_overall_score(marks: np.ndarray, attendance: np.ndarray) -> np.ndarray:
    """Combine arrays element-wise into a weighted overall score."""
    return (marks * 0.7) + (attendance * 0.3)


# ---------------------------------------------------------------------------
# Section 5: Comparison and Combined Risk Detection
# ---------------------------------------------------------------------------
def detect_at_risk_vectorized(marks: np.ndarray, attendance: np.ndarray) -> np.ndarray:
    """Return a boolean array marking at-risk students using combined conditions."""
    low_marks = marks < PASSING_MARKS_THRESHOLD
    low_attendance = attendance < MIN_ATTENDANCE_PERCENTAGE
    return low_marks | low_attendance


def class_summary(marks: np.ndarray, attendance: np.ndarray) -> dict[str, float]:
    """Return aggregate metrics computed without any explicit loop."""
    return {
        "average_marks": float(np.mean(marks)),
        "average_attendance": float(np.mean(attendance)),
        "max_marks": float(np.max(marks)),
        "min_marks": float(np.min(marks)),
        "marks_std": float(np.std(marks)),
    }


# ---------------------------------------------------------------------------
# Section 6: List vs Array Behavior Demo
# ---------------------------------------------------------------------------
def list_vs_array_math() -> None:
    sample_list = [10, 20, 30]
    sample_array = np.array(sample_list)

    print("\n--- List vs Array Math ---")
    print("List + List       :", sample_list + sample_list)        # concatenation
    print("List * 2          :", sample_list * 2)                  # repetition
    print("Array + Array     :", sample_array + sample_array)      # element-wise sum
    print("Array * 2         :", sample_array * 2)                 # element-wise scale


# ---------------------------------------------------------------------------
# Section 7: Shape Safety
# ---------------------------------------------------------------------------
def ensure_same_shape(array_a: np.ndarray, array_b: np.ndarray) -> None:
    if array_a.shape != array_b.shape:
        raise ValueError(
            f"Shape mismatch: {array_a.shape} vs {array_b.shape}. "
            "Math operations require identical shapes."
        )


# ---------------------------------------------------------------------------
# Section 8: Reporting
# ---------------------------------------------------------------------------
def print_array(label: str, array: np.ndarray) -> None:
    print(f"{label:<28}: {np.round(array, 2)}")


def print_class_summary(metrics: dict[str, float]) -> None:
    print("\n--- Class Summary (loop-free) ---")
    print(f"Average marks      : {metrics['average_marks']:.2f}")
    print(f"Average attendance : {metrics['average_attendance']:.2f}")
    print(f"Highest marks      : {metrics['max_marks']:.2f}")
    print(f"Lowest marks       : {metrics['min_marks']:.2f}")
    print(f"Marks std-dev      : {metrics['marks_std']:.2f}")


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
    print(f"At-risk count (np.sum mask): {int(np.sum(risk_flags))}")


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_data = load_student_data()
    arrays = to_arrays(student_data)
    marks = arrays["marks"]
    attendance = arrays["attendance"]

    ensure_same_shape(marks, attendance)

    print("--- Original Arrays ---")
    print_array("Marks", marks)
    print_array("Attendance", attendance)

    print("\n--- Scalar Operations ---")
    print_array("Marks + grace bonus", apply_grace_bonus(marks))
    print_array("Marks - late penalty", apply_late_penalty(marks))
    print_array("Attendance normalized", normalize_attendance(attendance))

    print("\n--- Element-Wise Combination ---")
    overall_score = compute_overall_score(marks, attendance)
    print_array("Overall score (0.7m+0.3a)", overall_score)

    metrics = class_summary(marks, attendance)
    print_class_summary(metrics)

    risk_flags = detect_at_risk_vectorized(marks, attendance)
    print_risk_table(student_data["names"], marks, attendance, risk_flags)

    list_vs_array_math()

    print("\nData Scientist Note:")
    print("- Replaced per-student loops with vectorized array math.")
    print("- Same code scales from 5 students to 10,000+ without rewrites.")


if __name__ == "__main__":
    main()
