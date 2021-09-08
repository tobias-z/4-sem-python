from enum import Enum
from typing import List, Union
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

    def __get_ints_from_strs(self, lst: List[Union[str, int]]):
        if len(lst) is 0:
            raise Exception("ds")

        return list(map(int, lst))

    def get_avg_grade(self):
        try:
            grades = self.data_sheet.get_grades_as_list()
            grades = self.__get_ints_from_strs(grades)
            return sum(grades) / len(grades)
        except:
            return 0.0

    def get_progression(self):
        try:
            ects_points = self.data_sheet.get_ects_points()
            ects_points = self.__get_ints_from_strs(ects_points)
            percent = (sum(ects_points) / 150) * 100
            return percent
        except:
            return 0.0

    def __repr__(self) -> str:
        return f"name: {self.name}, img_url: {self.img_url}, average grade: {self.get_avg_grade()} progression: {self.get_progression()}\n"
