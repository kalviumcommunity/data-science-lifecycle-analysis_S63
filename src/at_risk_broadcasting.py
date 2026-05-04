"""Milestone 4.26: Understanding NumPy Broadcasting.

Project: At-Risk Student Detection System
Focus: combine arrays of different shapes safely using broadcasting,
       and apply per-feature thresholds and weights without loops.
"""

# ---------------------------------------------------------------------------
# Section 1: Imports
# ---------------------------------------------------------------------------
import numpy as np


# ---------------------------------------------------------------------------
# Section 2: Constants and Configuration
# ---------------------------------------------------------------------------
GRACE_BONUS_POINTS = 2

# Per-subject minimum thresholds: [Math, Science, English]
SUBJECT_PASSING_THRESHOLDS = np.array([45.0, 40.0, 50.0])

# Per-subject weights for the overall score (must sum to ~1.0)
SUBJECT_WEIGHTS = np.array([0.5, 0.3, 0.2])

# Per-feature thresholds for the at-risk decision: [marks_min, attendance_min]
FEATURE_THRESHOLDS = np.array([50.0, 75.0])


# ---------------------------------------------------------------------------
# Section 3: Project Data
# ---------------------------------------------------------------------------
def load_student_data() -> dict[str, list]:
    """Per-subject marks plus attendance for each student."""
    return {
        "names": ["Aisha", "Rohit", "Neha", "Karan", "Isha"],
        # rows = students, cols = [Math, Science, English]
        "subject_marks": [
            [88, 81, 90],
            [44, 60, 55],
            [70, 38, 78],
            [83, 79, 82],
            [95, 92, 96],
        ],
        "attendance": [91, 79, 70, 86, 98],
    }


def to_arrays(student_data: dict[str, list]) -> dict[str, np.ndarray]:
    return {
        "subject_marks": np.array(student_data["subject_marks"], dtype=float),
        "attendance": np.array(student_data["attendance"], dtype=float),
    }


# ---------------------------------------------------------------------------
# Section 4: Step 1 - Scalar Broadcasting
# ---------------------------------------------------------------------------
def apply_grace_bonus_2d(subject_marks: np.ndarray) -> np.ndarray:
    """Add a single scalar to a 2D matrix - scalar broadcasts to every cell."""
    return subject_marks + GRACE_BONUS_POINTS


# ---------------------------------------------------------------------------
# Section 5: Step 3 and 4 - 1D over 2D Broadcasting
# ---------------------------------------------------------------------------
def passes_per_subject(subject_marks: np.ndarray) -> np.ndarray:
    """Compare each student's subject marks against per-subject thresholds.

    Shapes:
        subject_marks shape : (students, subjects)  e.g. (5, 3)
        thresholds shape    : (subjects,)           e.g. (3,)
    Broadcasting aligns thresholds across all student rows automatically.
    """
    return subject_marks >= SUBJECT_PASSING_THRESHOLDS


def weighted_overall_score(subject_marks: np.ndarray) -> np.ndarray:
    """Apply per-subject weights using broadcasting, then sum across subjects."""
    weighted = subject_marks * SUBJECT_WEIGHTS  # broadcast (5,3) * (3,) -> (5,3)
    return np.sum(weighted, axis=1)              # collapse to (5,)


# ---------------------------------------------------------------------------
# Section 6: Step 7 - Project Risk Detection via Broadcasting
# ---------------------------------------------------------------------------
def build_feature_matrix(
    overall_score: np.ndarray,
    attendance: np.ndarray,
) -> np.ndarray:
    """Combine overall score and attendance into a (students, 2) matrix."""
    return np.column_stack((overall_score, attendance))


def detect_at_risk_broadcast(feature_matrix: np.ndarray) -> np.ndarray:
    """Compare a (students, 2) matrix to a (2,) thresholds array via broadcasting.

    Each student is at risk if ANY feature falls below its threshold.
    """
    below_threshold = feature_matrix < FEATURE_THRESHOLDS  # shape (5, 2)
    return np.any(below_threshold, axis=1)                  # shape (5,)


# ---------------------------------------------------------------------------
# Section 7: Step 8 - Common Error Demo
# ---------------------------------------------------------------------------
def shape_mismatch_demo() -> None:
    """Trigger and catch a real broadcasting error."""
    print("\n--- Shape Mismatch Demo ---")
    matrix = np.zeros((5, 3))
    bad_thresholds = np.array([1.0, 2.0])  # (2,) cannot align with last axis 3
    try:
        _ = matrix + bad_thresholds
    except ValueError as error:
        print(f"Caught ValueError: {error}")
        print("Fix: ensure last axes are equal or one of them is 1.")


# ---------------------------------------------------------------------------
# Section 8: Reporting
# ---------------------------------------------------------------------------
def print_array(label: str, array: np.ndarray) -> None:
    print(f"{label}\n{np.round(array, 2)}\n")


def print_pass_fail_table(
    names: list[str],
    pass_mask: np.ndarray,
) -> None:
    print("--- Per-Subject Pass/Fail (broadcast comparison) ---")
    print(f"{'Name':<8} {'Math':>6} {'Sci':>6} {'Eng':>6}")
    print("-" * 30)
    for index, name in enumerate(names):
        flags = ["pass" if bool(value) else "fail" for value in pass_mask[index]]
        print(f"{name:<8} {flags[0]:>6} {flags[1]:>6} {flags[2]:>6}")
    print("-" * 30)


def print_risk_table(
    names: list[str],
    overall_score: np.ndarray,
    attendance: np.ndarray,
    risk_flags: np.ndarray,
) -> None:
    print("\n--- Risk Detection (broadcast against feature thresholds) ---")
    print(f"{'Name':<8} {'Score':>7} {'Attend%':>8} {'Status':>10}")
    print("-" * 36)
    for index, name in enumerate(names):
        status = "At Risk" if bool(risk_flags[index]) else "Safe"
        print(
            f"{name:<8} {overall_score[index]:>7.2f} "
            f"{attendance[index]:>8.1f} {status:>10}"
        )
    print("-" * 36)
    print(f"At-risk count : {int(np.sum(risk_flags))}")


# ---------------------------------------------------------------------------
# Section 9: Main Execution
# ---------------------------------------------------------------------------
def main() -> None:
    student_data = load_student_data()
    arrays = to_arrays(student_data)
    subject_marks = arrays["subject_marks"]
    attendance = arrays["attendance"]

    print("--- Shapes ---")
    print(f"subject_marks         : {subject_marks.shape}")
    print(f"attendance            : {attendance.shape}")
    print(f"SUBJECT_PASSING_THRESHOLDS : {SUBJECT_PASSING_THRESHOLDS.shape}")
    print(f"SUBJECT_WEIGHTS       : {SUBJECT_WEIGHTS.shape}")
    print(f"FEATURE_THRESHOLDS    : {FEATURE_THRESHOLDS.shape}\n")

    # Step 1: scalar broadcasting
    print_array("Subject marks + grace bonus (scalar broadcast)",
                apply_grace_bonus_2d(subject_marks))

    # Step 3 and 4: 1D over 2D broadcasting
    pass_mask = passes_per_subject(subject_marks)
    print_pass_fail_table(student_data["names"], pass_mask)

    overall_score = weighted_overall_score(subject_marks)
    print_array("\nOverall weighted score (broadcast + sum axis=1)", overall_score)

    # Step 7: project risk detection via broadcasting
    feature_matrix = build_feature_matrix(overall_score, attendance)
    print_array("Feature matrix (students, 2)", feature_matrix)

    risk_flags = detect_at_risk_broadcast(feature_matrix)
    print_risk_table(student_data["names"], overall_score, attendance, risk_flags)

    # Step 8: common error demo
    shape_mismatch_demo()

    print("\nData Scientist Note:")
    print("- Broadcasting stretches smaller arrays logically without copying data.")
    print("- It removes the need for loops when shapes align by the right side.")
    print("- This pattern is essential for per-feature thresholds and weights.")


if __name__ == "__main__":
    main()
