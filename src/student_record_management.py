"""Milestone 4.15: Lists, Tuples, and Dictionaries mini project.

Student Record Management Mini System
-------------------------------------
This script demonstrates:
- list usage for dynamic student names
- tuple usage for fixed subjects
- dictionary usage for name -> marks mapping
"""


def print_section(title: str) -> None:
    print(f"\n=== {title} ===")


def list_demo(student_names: list[str]) -> list[str]:
    """Demonstrate list access, add, and remove operations."""
    print_section("Step 1 - List Operations")
    print("Initial student list:", student_names)
    print("First student (index 0):", student_names[0])

    student_names.append("Aman")
    print("After add (append 'Aman'):", student_names)

    removed = student_names.pop(1)
    print(f"After remove (pop index 1 -> '{removed}'):", student_names)
    print("Why list? Student roster changes over time.")
    return student_names


def tuple_demo(subjects: tuple[str, ...]) -> tuple[str, ...]:
    """Demonstrate tuple immutability with safe error handling."""
    print_section("Step 2 - Tuple Operations")
    print("Subjects tuple (fixed):", subjects)
    print("Second subject (index 1):", subjects[1])

    try:
        subjects[0] = "Biology"  # type: ignore[index]
    except TypeError as error:
        print("Tuple immutability demo:", error)
        print("Why tuple? Subjects are fixed for this milestone setup.")
    return subjects


def dictionary_demo(student_marks: dict[str, int]) -> dict[str, int]:
    """Demonstrate dictionary access, insert, and update."""
    print_section("Step 3 - Dictionary Operations")
    print("Initial marks dictionary:", student_marks)
    print("Marks for Aisha:", student_marks["Aisha"])

    student_marks["Aman"] = 84
    print("After adding Aman:", student_marks)

    student_marks["Rohit"] = 95
    print("After updating Rohit:", student_marks)
    print("Why dictionary? Fast name -> marks mapping.")
    return student_marks


def combine_and_report(
    student_names: list[str],
    subjects: tuple[str, ...],
    student_marks: dict[str, int],
) -> None:
    """Combine structures and print structured report output."""
    print_section("Step 4/5 - Combined Structured Report")
    print("Students :", student_names)
    print("Subjects :", subjects)
    print("Name->Marks Mapping:", student_marks)

    print("\nStudent Performance Table")
    print("-" * 32)
    print(f"{'Student':<12} {'Marks':>6}")
    print("-" * 32)
    for name in student_names:
        marks = student_marks.get(name, "N/A")
        print(f"{name:<12} {marks:>6}")
    print("-" * 32)


def structure_reasoning() -> None:
    """Explain why each collection type is chosen."""
    print_section("Step 6 - Choosing Data Structures")
    print("List       -> dynamic roster (add/remove students)")
    print("Tuple      -> fixed subjects (immutability protects config)")
    print("Dictionary -> name to marks mapping (quick lookup/update)")


def improvement_thinking(student_marks: dict[str, int]) -> None:
    """Show deeper upgrade direction without external libraries."""
    print_section("Step 7 - Upgrade Thinking")
    print("Challenge 1: add more subjects without rewriting logic.")
    print("Challenge 2: store subject-wise marks per student.")

    # Example scalable structure (dictionary of dictionaries)
    subject_wise_marks = {
        "Aisha": {"Math": 88, "Science": 81, "English": 86},
        "Rohit": {"Math": 95, "Science": 93, "English": 90},
        "Neha": {"Math": 78, "Science": 80, "English": 79},
    }
    print("Sample scalable structure:", subject_wise_marks)

    # Simple deeper metric: compute average from simple dictionary
    average = sum(student_marks.values()) / len(student_marks)
    print(f"Current class average (single-mark system): {average:.2f}")


def video_prep_points() -> None:
    """Print speaking points for a short milestone video."""
    print_section("Step 8 - Video Preparation Points")
    print("1) List: mutable ordered collection for student names.")
    print("2) Tuple: immutable ordered collection for fixed subjects.")
    print("3) Dictionary: key-value mapping for marks.")
    print("4) Key difference: dynamic vs fixed vs mapped lookup.")
    print("5) Project summary: add/update/access records cleanly.")


def main() -> None:
    student_names = ["Aisha", "Rohit", "Neha", "Karan"]
    subjects = ("Math", "Science", "English")
    student_marks = {"Aisha": 88, "Rohit": 91, "Neha": 79, "Karan": 85}

    student_names = list_demo(student_names)
    subjects = tuple_demo(subjects)
    student_marks = dictionary_demo(student_marks)
    combine_and_report(student_names, subjects, student_marks)
    structure_reasoning()
    improvement_thinking(student_marks)
    video_prep_points()

    print_section("Milestone 4.15 Outcome")
    print("Built: Student Record Management Mini System")
    print("Learned: list, tuple, dictionary usage with real workflow")
    print("Confidence: can choose and apply Python collections correctly")


if __name__ == "__main__":
    main()
