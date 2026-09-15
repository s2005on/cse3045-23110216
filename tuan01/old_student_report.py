import csv


def read_students(filename):
    students = []

    file = open(filename, "r", encoding="utf-8")
    reader = csv.DictReader(file)

    for row in reader:
        student = {
            "name": row["name"],
            "math": float(row["math"]),
            "physics": float(row["physics"]),
            "english": float(row["english"]),
        }
        students.append(student)

    file.close()
    return students


def calculate_average(student):
    total = student["math"] + student["physics"] + student["english"]
    return total / 3


def classify_student(average):
    if average >= 8.0:
        return "Excellent"
    elif average >= 6.5:
        return "Good"
    elif average >= 5.0:
        return "Average"
    else:
        return "Fail"


students = read_students("tuan01/students.csv")

for student in students:
    average = calculate_average(student)
    classification = classify_student(average)

    print(
        "Student: "
        + student["name"]
        + " | Average: "
        + str(round(average, 2))
        + " | Classification: "
        + classification
    )