class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name} \nAge: {self.age}"
    
class Classroom:
    def __init__(self) -> None:
        self.students = []

    def amount_of_students(self):
        amount_of_students = 0
        for student in self.students:
            amount_of_students += 1
        return amount_of_students
    
    def add_student(self, student):
        self.students.append(student)

    def __repr__(self):
        
        return f"Students: {self.students} \nNumber of students: {Classroom.amount_of_students(self)}"


students = [Student("Bob", 10), Student("Jill", 9), Student("George", 12), Student("Jane", 8)]
classroom = Classroom()
for student in students:
    classroom.add_student(student)
print(classroom)