from modules.week3.data_sheet import DataSheet
from modules.week3.course import Course
from typing import List, TextIO
from typing_extensions import TypedDict
from modules.week3.student import Gender, Student
import random


class TStudent(TypedDict):
    name: str
    gender: Gender
    img_url: str


STUDENTS: List[TStudent] = [
    {"name": "Bob", "gender": Gender.MALE, "img_url": "https://student-image.com/bob"},
    {
        "name": "Tobias",
        "gender": Gender.MALE,
        "img_url": "https://student-image.com/tobias",
    },
    {"name": "Jon", "gender": Gender.MALE, "img_url": "https://student-image.com/jon"},
    {
        "name": "Someone",
        "gender": Gender.FEMALE,
        "img_url": "https://student-image.com/someone",
    },
]

COURSES: List[Course] = [
    Course("CS", 105, "Thomas", 12),
    Course("Math", 10, "Patrik", 10),
    Course("English", 201, "Coleen", 12),
    Course("Danish", 102, "Jens", 7),
    Course("History", 7, "Jon", 10),
]

GRADES = [-3, 0, 2, 4, 7, 10, 12]


def __write_student_to_csv(file: TextIO, student: Student):
    for course in student.data_sheet.courses:
        row = f"{student.name}, {course.name}, {course.teacher}, {student.gender.value}, ?, {course.classroom}, {course.grade}, {student.img_url}\n"
        file.write(row)


def create_students(amount: int):
    students: List[Student] = []
    with open("files/students.csv", "w") as file:
        file.write(
            "stud_name, course_name, teacher_name, gender, ects, classroom, grade, img_url\n"
        )
        for _ in range(0, amount):
            data_sheet = DataSheet()
            for course in random.choices(COURSES, k=random.randint(0, 10)):
                if course in data_sheet.courses:
                    continue

                course.grade = random.choice(GRADES)
                data_sheet.add_course(course)

            student_data = random.choice(STUDENTS)

            student = Student(
                student_data["name"],
                student_data["gender"],
                data_sheet,
                student_data["img_url"],
            )

            __write_student_to_csv(file, student)
            students.append(student)

    return students
