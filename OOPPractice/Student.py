import csv


class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __repr__(self):
        return f"Name: {self.name} \nGrade: {self.grade}"
    
class Classroom:
    def __init__(self):
        self.students = []

    def amount_of_students(self):
        amount_of_students = 0
        for student in self.students:
            amount_of_students += 1
        return amount_of_students
    
    def add_student(self, student):
        self.students.append(student)

    def class_average(self):
        Sum_of_grades = 0
        for student in self.students:
            Sum_of_grades += student.grade

        return Sum_of_grades / Classroom.amount_of_students(self)

    def __repr__(self):
        return f"Students: {self.students} \nNumber of students: {Classroom.amount_of_students(self)} \nClass Average: {Classroom.class_average(self)}"


with open(r"C:\Users\summe\OneDrive\Desktop\personalprojects\OOPPractice\students.csv") as file:
    reader = csv.reader(file)
    for row in  reader:
        