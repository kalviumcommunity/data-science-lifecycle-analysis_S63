"""Milestone 4.22: Creating NumPy arrays from Python lists.

Project: At-Risk Student Detection System
Focus: upgrade list-based numeric data into NumPy arrays for efficient
       element-wise computation and scalable analytics.
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


# ---------------------------------------------------------------------------
# Section 3: Project Data (still in original list form)
# ---------------------------------------------------------------------------
def load_student_data() -> dict[str, list]:
    """Return the original Python-list dataset used by the project."""
    return {
        "names": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        "marks": [88, 49, 72, 83, 95],
        "attendance": [91, 79, 70, 86, 98],
    }


# ---------------------------------------------------------------------------
# Section 4: NumPy Conversion and Inspection
# ---------------------------------------------------------------------------
def convert_to_arrays(student_data: dict[str, list]) -> dict[str, np.ndarray]:
    """Convert numeric project lists into NumPy arrays."""
    return {
        "marks": np.array(student_data["marks"], dtype=float),
        "attendance": np.array(student_data["attendance"], dtype=float),
    }


def inspect_arrays(arrays: dict[str, np.ndarray]) -> None:
    """Print shape and dtype of each array for debugging clarity."""
    print("\n--- Array Inspection ---")
    for label, array in arrays.items():
        print(f"{label:<11}: shape={array.shape}, dtype={array.dtype}, values={array}")


# ---------------------------------------------------------------------------
# Section 5: Array-Based Computations
# ---------------------------------------------------------------------------
def compute_class_metrics(marks: np.ndarray, attendance: np.ndarray) -> dict[str, float]:
    """Return class-level metrics using vectorized array operations."""
    return {
        "average_marks": float(np.mean(marks)),
        "average_attendance": float(np.mean(attendance)),
        "highest_marks": float(np.max(marks)),
        "lowest_marks": float(np.min(marks)),
    }


def detect_at_risk(marks: np.ndarray, attendance: np.ndarray) -> np.ndarray:
    """Return a boolean array flagging at-risk students using vectorized logic."""
    return (marks < PASSING_MARKS_THRESHOLD) | (attendance < MIN_ATTENDANCE_PERCENTAGE)


# ---------------------------------------------------------------------------
# Section 6: Reporting
# ---------------------------------------------------------------------------
def print_class_metrics(metrics: dict[str, float]) -> None:
    print("\n--- Class Metrics ---")
    print(f"Average marks      : {metrics['average_marks']:.2f}")
    print(f"Average attendance : {metrics['average_attendance']:.2f}")
    print(f"Highest marks      : {metrics['highest_marks']:.2f}")
    print(f"Lowest marks       : {metrics['lowest_marks']:.2f}")


def print_risk_report(
    names: list[str],
    marks: np.ndarray,
    attendance: np.ndarray,
    risk_flags: np.ndarray,
) -> None:
    print("\n--- At-Risk Detection (Vectorized) ---")
    print(f"{'Name':<8} {'Marks':>6} {'Attend%':>8} {'Status':>10}")
    print("-" * 36)
    for index, name in enumerate(names):
        status = "At Risk" if bool(risk_flags[index]) else "Safe"
        print(f"{name:<8} {marks[index]:>6.1f} {attendance[index]:>8.1f} {status:>10}")
    print("-" * 36)
    print(f"Total at-risk count: {int(np.sum(risk_flags))}")


def list_vs_array_demo() -> None:
    """Show the behavioral difference between Python lists and NumPy arrays."""
    sample_list = [10, 20, 30]
    sample_array = np.array(sample_list)

    print("\n--- List vs Array ---")
    print("List + List       :", sample_list + sample_list)         # concatenation
    print("Array + Array     :", sample_array + sample_array)       # element-wise
    print("Array * 2         :", sample_array * 2)                  # vectorized scaling
    print("Array > 15 (mask) :", sample_array > 15)                 # boolean mask


# ---------------------------------------------------------------------------
# Section 7: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_data = load_student_data()
    arrays = convert_to_arrays(student_data)

    inspect_arrays(arrays)

    metrics = compute_class_metrics(arrays["marks"], arrays["attendance"])
    print_class_metrics(metrics)

    risk_flags = detect_at_risk(arrays["marks"], arrays["attendance"])
    print_risk_report(student_data["names"], arrays["marks"], arrays["attendance"], risk_flags)

    list_vs_array_demo()

    print("\nData Scientist Note:")
    print("- Arrays scale efficiently from 5 to 10,000+ students.")
    print("- Vectorized operations replace manual loops for speed and clarity.")


if __name__ == "__main__":
    main()
