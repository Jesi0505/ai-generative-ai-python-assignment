from grade_utils import (
    calculate_total,
    calculate_percentage,
    calculate_grade,
    check_result
)


def display_result(name, marks):
    total = calculate_total(marks)
    percentage = calculate_percentage(total, len(marks))
    grade = calculate_grade(percentage)
    result = check_result(marks)

    print("\n----- STUDENT RESULT -----")
    print("Student Name:", name)
    print("Marks:", marks)
    print("Total Marks:", total)
    print("Percentage:", round(percentage, 2), "%")
    print("Grade:", grade)
    print("Result:", result)


def main():
    print("===== STUDENT GRADE MANAGEMENT SYSTEM =====")

    name = input("Enter student name: ")

    subjects = ["Python", "Mathematics", "English", "Computer Science", "AI"]

    marks = []

    for subject in subjects:
        mark = float(input(f"Enter marks for {subject}: "))
        marks.append(mark)

    display_result(name, marks)


if __name__ == "__main__":
    main()
