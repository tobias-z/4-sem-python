from modules.week3.data_sheet import DataSheet
from modules.week3.course import Course
from typing import List, TextIO
from typing_extensions import TypedDict
from modules.week3.student import Gender, Student
import random
import csv


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
    {
        "name": "Hans",
        "gender": Gender.MALE,
        "img_url": "https://student-image.com/hans",
    },
    {
        "name": "Alice",
        "gender": Gender.FEMALE,
        "img_url": "https://student-image.com/alice",
    },
    {
        "name": "Johan",
        "gender": Gender.MALE,
        "img_url": "https://student-image.com/johan",
    },
    {
        "name": "Carl-Emil",
        "gender": Gender.MALE,
        "img_url": "https://student-image.com/carl-emil",
    },
    {
        "name": "Amalie",
        "gender": Gender.FEMALE,
        "img_url": "https://student-image.com/amalie",
    },
    {
        "name": "Jens",
        "gender": Gender.MALE,
        "img_url": "https://student-image.com/jens",
    },
]

COURSES: List[Course] = [
    Course("CS", 105, "Thomas", 30, 12),
    Course("Math", 10, "Patrik", 30, 10),
    Course("English", 201, "Coleen", 30, 12),
    Course("Danish", 102, "Jens", 30, 7),
    Course("History", 7, "Jon", 30, 10),
]

GRADES = [0, 2, 4, 7, 10, 12]

STUDENT_FILE = "files/students.csv"


def __write_student_to_csv(file: TextIO, student: Student):
    for course in student.data_sheet.courses:
        row = f"{student.name}, {course.name}, {course.teacher}, {student.gender.value}, ?, {course.classroom}, {course.grade}, {student.img_url}\n"
        file.write(row)


def is_student_in_course(name: str, students: List[Student], the_corse: Course) -> bool:
    for student in students:
        if student.name == name:
            for course in student.data_sheet.courses:
                if (
                    course.name == the_corse.name
                    and course.grade is not None
                    and course.grade <= 0
                ):
                    return True

    return False


def create_students(amount: int = len(STUDENTS)):
    if amount > len(STUDENTS):
        raise Exception("We only have: " + str(len(STUDENTS)) + " students")

    students: List[Student] = []

    with open(STUDENT_FILE, "w") as file:
        file.write(
            "stud_name, course_name, teacher_name, gender, ects, classroom, grade, img_url\n"
        )

        while len(students) is not amount:
            data_sheet = DataSheet()
            student_data = random.choice(STUDENTS)
            if student_data["name"] in [student.name for student in students]:
                continue

            for course in random.choices(COURSES, k=random.randint(0, 10)):
                in_course = is_student_in_course(student_data["name"], students, course)
                if course in data_sheet.courses or in_course:
                    continue

                course.grade = random.choice(GRADES)
                data_sheet.add_course(course)

            student = Student(
                student_data["name"],
                student_data["gender"],
                data_sheet,
                student_data["img_url"],
            )

            __write_student_to_csv(file, student)
            students.append(student)

    return students


def __get_all_students(reader):
    students: List[Student] = []
    current_student: Student = None
    for row in reader:
        if current_student == None:
            current_student = Student(row[0], row[3], DataSheet(), row[7])

        if current_student.name != row[0]:
            print(current_student)
            students.append(current_student)
            current_student = Student(row[0], row[3], DataSheet(), row[7])

        current_student.data_sheet.add_course(
            Course(row[1], row[5], row[2], row[4], row[6])
        )

    students.append(current_student)
    return students


def read_students():
    with open(STUDENT_FILE) as file:
        reader = csv.reader(file)
        header = next(reader)
        print(header)
        all_students = __get_all_students(reader)
        return sorted(all_students, key=lambda student: student.get_avg_grade())
