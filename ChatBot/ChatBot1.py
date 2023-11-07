
dictionary = []
with open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r') as file:
    for line in file:
        dictionary.append(line.strip())


print(dictionary)