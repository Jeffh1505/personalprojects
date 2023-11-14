class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Name: {self.name} \nAge: {self.age}"
    

student = Student("Bob", 10)

print(student)