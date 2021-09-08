from typing import List
from .student import Student
from .student_utils import write_student_to_csv
import csv


class NotEnoughStudentsException(Exception):
    pass


def get_students_closet_to_finish(students: List[Student]):
    if len(students) < 3:
        raise NotEnoughStudentsException(
            "Not enough students. Atleast three students are required"
        )

    students.sort(key=lambda student: student.get_progression(), reverse=True)
    return students[0:3]


def create_csv_for_three_students(students: List[Student]):
    students = get_students_closet_to_finish(students)
    with open("files/closest_students.csv", "w") as file:
        try:
            file.write(
                "stud_name, course_name, teacher_name, gender, ects, classroom, grade, img_url\n"
            )
            for student in students:
                write_student_to_csv(file, student)
        except Exception:
            file.write("No more students were found")
