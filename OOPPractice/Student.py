class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name} \nAge: {self.age}"
    
class Classroom:
    def __init__(self, students) -> None:
        self.students = []

    def amount_of_students(self):
        amount_of_students = 0
        for student in self.students:
            amount_of_students += 1
        return amount_of_students
    
    def add_student(self, student):
        self.students.append()


student = Student("Bob", 10)

print(student)