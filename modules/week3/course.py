class Course:
    def __init__(
        self, name: str, classroom: int, teacher: str, ECTS: int, grade: int = None
    ) -> None:
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.ECTS = ECTS
        self.grade = grade

    def __repr__(self) -> str:
        return f"name: {self.name}, grade: {self.grade}"
