result = {}
name1 = 0 
name2 = 0
name3 = 0 
with open(r"C:\Users\summe\OneDrive\Desktop\personalprojects\PracticePython\nameslist.txt", "r") as file:

    for line in file:
        line = file.readline().strip()
        result.setdefault(line, []).append(1)
for i in result.values():
    for results in result.values():
        name1 += 1
        name2 += 1
        name3 += 1    
print(result)
print(name1)
print(name2)
print(name3)