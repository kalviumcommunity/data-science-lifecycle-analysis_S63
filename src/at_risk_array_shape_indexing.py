"""Milestone 4.23: Array Shape, Dimensions, and Index Positions.

Project: At-Risk Student Detection System
Focus: understand 1D vs 2D structure, access student data by index,
       and apply indexing to project risk logic safely.
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

MARKS_COLUMN = 0
ATTENDANCE_COLUMN = 1


# ---------------------------------------------------------------------------
# Section 3: Project Data
# ---------------------------------------------------------------------------
def load_student_data() -> dict[str, list]:
    """Return original list-based project data."""
    return {
        "names": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        "marks": [88, 49, 72, 83, 95],
        "attendance": [91, 79, 70, 86, 98],
    }


# ---------------------------------------------------------------------------
# Section 4: 1D and 2D Array Construction
# ---------------------------------------------------------------------------
def build_1d_arrays(student_data: dict[str, list]) -> dict[str, np.ndarray]:
    """Return 1D arrays for marks and attendance."""
    return {
        "marks": np.array(student_data["marks"], dtype=float),
        "attendance": np.array(student_data["attendance"], dtype=float),
    }


def build_2d_array(arrays_1d: dict[str, np.ndarray]) -> np.ndarray:
    """Return 2D array where rows = students, columns = [marks, attendance]."""
    return np.column_stack((arrays_1d["marks"], arrays_1d["attendance"]))


# ---------------------------------------------------------------------------
# Section 5: Shape and Dimension Inspection
# ---------------------------------------------------------------------------
def inspect_structure(label: str, array: np.ndarray) -> None:
    """Print shape, ndim, and size to build structural intuition."""
    print(f"\n--- {label} ---")
    print(f"shape : {array.shape}")
    print(f"ndim  : {array.ndim}")
    print(f"size  : {array.size}")
    print(f"dtype : {array.dtype}")
    print(f"values:\n{array}")


# ---------------------------------------------------------------------------
# Section 6: Safe Indexing Helpers
# ---------------------------------------------------------------------------
def get_student_row(student_matrix: np.ndarray, student_index: int) -> np.ndarray:
    """Return a single student's feature row, with bounds check."""
    total_students = student_matrix.shape[0]
    if student_index < 0 or student_index >= total_students:
        raise IndexError(
            f"Invalid student_index={student_index}. Valid range: 0 to {total_students - 1}."
        )
    return student_matrix[student_index]


def get_feature_column(student_matrix: np.ndarray, column_index: int) -> np.ndarray:
    """Return a single feature column for all students, with bounds check."""
    total_features = student_matrix.shape[1]
    if column_index < 0 or column_index >= total_features:
        raise IndexError(
            f"Invalid column_index={column_index}. Valid range: 0 to {total_features - 1}."
        )
    return student_matrix[:, column_index]


# ---------------------------------------------------------------------------
# Section 7: Project Logic Using 2D Indexing
# ---------------------------------------------------------------------------
def detect_at_risk_2d(student_matrix: np.ndarray) -> np.ndarray:
    """Apply at-risk logic on a 2D matrix using column indexing."""
    marks = student_matrix[:, MARKS_COLUMN]
    attendance = student_matrix[:, ATTENDANCE_COLUMN]
    return (marks < PASSING_MARKS_THRESHOLD) | (attendance < MIN_ATTENDANCE_PERCENTAGE)


def print_student_table(
    names: list[str],
    student_matrix: np.ndarray,
    risk_flags: np.ndarray,
) -> None:
    print("\n--- Student Matrix (rows=students, cols=[marks, attendance]) ---")
    print(f"{'Idx':<4} {'Name':<8} {'Marks':>6} {'Attend%':>8} {'Status':>10}")
    print("-" * 42)
    for index, name in enumerate(names):
        marks = student_matrix[index, MARKS_COLUMN]
        attendance = student_matrix[index, ATTENDANCE_COLUMN]
        status = "At Risk" if bool(risk_flags[index]) else "Safe"
        print(f"{index:<4} {name:<8} {marks:>6.1f} {attendance:>8.1f} {status:>10}")
    print("-" * 42)


def safe_indexing_demo(student_matrix: np.ndarray) -> None:
    """Show how to handle out-of-range indices safely."""
    print("\n--- Safe Indexing Demo ---")
    try:
        get_student_row(student_matrix, 99)
    except IndexError as error:
        print(f"Caught IndexError: {error}")


# ---------------------------------------------------------------------------
# Section 8: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_data = load_student_data()
    arrays_1d = build_1d_arrays(student_data)
    student_matrix = build_2d_array(arrays_1d)

    inspect_structure("1D marks array", arrays_1d["marks"])
    inspect_structure("1D attendance array", arrays_1d["attendance"])
    inspect_structure("2D student matrix", student_matrix)

    print("\n--- Indexing Examples ---")
    student_one = get_student_row(student_matrix, 0)
    print(f"Student 0 ({student_data['names'][0]}) row : {student_one}")
    print(f"Student 0 marks (matrix[0, 0]) : {student_matrix[0, MARKS_COLUMN]}")
    print(f"Student 0 attendance (matrix[0, 1]) : {student_matrix[0, ATTENDANCE_COLUMN]}")

    all_marks_column = get_feature_column(student_matrix, MARKS_COLUMN)
    print(f"All marks column (matrix[:, 0]) : {all_marks_column}")

    risk_flags = detect_at_risk_2d(student_matrix)
    print_student_table(student_data["names"], student_matrix, risk_flags)

    safe_indexing_demo(student_matrix)

    print("\nData Scientist Note:")
    print("- 1D arrays store one feature; 2D matrices store many features per student.")
    print("- Always check shape before indexing to avoid silent logic bugs.")
    print("- This 2D structure scales to 1000+ students and many feature columns.")


if __name__ == "__main__":
    main()
