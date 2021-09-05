class Course:
    def __init__(
        self, name: str, classroom: int, teacher: str, grade: int = None
    ) -> None:
        self.name = name
        self.classroom = classroom
        self.teacher = teacher
        self.grade = grade
