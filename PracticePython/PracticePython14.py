def main():
    list_to_add_stuff = []
    while True:
        user_input = input("Please input an element into the list: ")
        if user_input == "Exit":
            list_to_set = get_set(list_to_add_stuff)
            return print(list_to_set)
        else:
            list_to_add_stuff.append(user_input)
            continue
def get_set(li):
    return set(li)
main()