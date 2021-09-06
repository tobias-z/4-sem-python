from enum import Enum
from modules.week3.data_sheet import DataSheet
from modules.week3.course import Course


class Gender(Enum):
    MALE = "MALE"
    FEMALE = "FEMALE"


class Student:
    def __init__(
        self, name: str, gender: Gender, data_sheet: DataSheet, img_url: str
    ) -> None:
        self.name = name
        self.gender = gender
        self.data_sheet = data_sheet
        self.img_url = img_url

    def get_avg_grade(self):
        grades = self.data_sheet.get_grades_as_list()
        if len(grades) is 0:
            return 0.0

        if type(grades[0]) is str:
            grades = list(map(int, grades))
        return sum(grades) / len(grades)

    def get_progression(self):
        ects_points = self.data_sheet.get_ects_points()
        percent = (sum(ects_points) / 150) * 100
        return percent

    def __repr__(self) -> str:
        return f"name: {self.name}, img_url: {self.img_url}, average grade: {self.get_avg_grade()}\n"
