from modules.week3.student_utils import create_students
from modules.week3.data_sheet import DataSheet
from modules.week3.student import Gender, Student
from modules.week3.course import Course
import unittest


class TestClasses(unittest.TestCase):
    def test_student(self):
        student = Student(
            "bob", Gender.MALE, DataSheet(), "https://student-image.com/bob"
        )
        student.data_sheet.add_course(Course("Math", 100, "The builder", 7))
        student.data_sheet.add_course(Course("CS", 10, "Thomas", 12))
        self.assertEqual(student.get_avg_grade(), 9.5)

    def test_create_students(self):
        students = create_students(5)
        for student in students:
            self.assertIsNotNone(student.name)
            self.assertIsNotNone(type(student.gender) == Gender)
            print(student)
