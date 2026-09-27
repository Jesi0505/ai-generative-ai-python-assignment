def calculate_total(marks):
    return sum(marks)


def calculate_percentage(total, number_of_subjects):
    return total / number_of_subjects


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    else:
        return "F"


def check_result(marks):
    if all(mark >= 35 for mark in marks):
        return "PASS"
    else:
        return "FAIL"
