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
            return 0
        return sum(grades) / len(grades)

    def __repr__(self) -> str:
        return f"name: {self.name}, gender: {self.gender}, img_url: {self.img_url} grades: {self.data_sheet.get_grades_as_list()} average grade: {self.get_avg_grade()}"
