class Student:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def __repr__(self) -> str:
        return f"Name: {self.name} Age: {self.age}"
    

student = Student("Bob", 10)

print(student)