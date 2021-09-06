from modules.week3.course import Course
from typing import List


class DataSheet:
    def __init__(self) -> None:
        self.courses: List[Course] = list()

    def add_course(self, course: Course):
        self.courses.append(course)

    def get_grades_as_list(self):
        return [course.grade for course in self.courses if course.grade is not None]

    def get_ects_points(self):
        return [course.ECTS for course in self.courses]
