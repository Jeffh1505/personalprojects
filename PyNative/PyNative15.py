def showEmployee(name, salary=9000):
    return name, salary

Ben, salary = showEmployee("Ben", 12000)
Jessa, salary = showEmployee("Jessa")

print(f"Name: {Ben}, {salary}")
print(f"Name: {Jessa}, {salary}")