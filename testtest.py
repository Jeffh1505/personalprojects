class Child:
    def __init__(self, name, age, toys):
        self.name = name
        self.age = age # age in years
        self.toys = toys # number of toys owned by this child as an integer


children = [Child("Charlie",6,20), Child("Idris",7,25), Child("Alex",3,5), \
Child("Pax",3,12), Child("Zara",7,5)]


def sum_toys_per_age(persons):
    toy_dict = {}
    for person in persons:
        toy_dict[person.age] = person.toys

    return toy_dict

print(sum_toys_per_age(children))