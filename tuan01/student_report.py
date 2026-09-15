import csv
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Student:
    name: str
    math: float
    physics: float
    english: float

    def average(self) -> float:
        return (self.math + self.physics + self.english) / 3


def read_students(file_path: Path) -> list[Student]:
    students: list[Student] = []

    with file_path.open("r", encoding="utf-8", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            student = Student(
                name=row["name"],
                math=float(row["math"]),
                physics=float(row["physics"]),
                english=float(row["english"]),
            )
            students.append(student)

    return students


def classify_student(average: float) -> str:
    if average >= 8.0:
        return "Excellent"
    if average >= 6.5:
        return "Good"
    if average >= 5.0:
        return "Average"
    return "Fail"


def main() -> None:
    file_path = Path(__file__).parent / "students.csv"
    students = read_students(file_path)

    for student in students:
        average = student.average()
        classification = classify_student(average)

        print(
            f"Student: {student.name} | "
            f"Average: {average:.2f} | "
            f"Classification: {classification}"
        )


if __name__ == "__main__":
    main()
