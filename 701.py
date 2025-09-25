class Student:
    def __init__(self, name: str, student_id: int, grades: list[int]):
        self.name = name
        self.student_id = student_id
        self.grades = grades

    def GPA(self) -> float:
        return sum(self.grades) / len(self.grades)