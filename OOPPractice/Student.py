import numpy as np
import pandas as pd
from pandas.io.parsers import read_csv
import math
from dataclasses import dataclass

@dataclass
class Student:
    Name: str
    Grade: str
    
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
            Sum_of_grades += int(student.Grade)

        return Sum_of_grades / Classroom.amount_of_students(self)

    def __repr__(self):
        return f"Students: {self.students} \nNumber of students: {Classroom.amount_of_students(self)} \nClass Average: {Classroom.class_average(self)}"

df = read_csv(r"C:\Users\summe\OneDrive\Desktop\personalprojects-1\OOPPractice\students.csv")
print(df.describe())