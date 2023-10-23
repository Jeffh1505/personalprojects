import random
def main():
    User_input = input("Would you like a password? (y/n): ")
    if User_input == 'y':
        c = generate_password()
        print("Password:", c)
    else:
        print("Ok, then.")

def generate_password():
    password_character_list = []
    possible_password_character_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'
                                        ,'I', 'J', 'K', 'L', 'M', 'N', 'O','P'
                                        ,'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X'
                                        ,'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f'
                                        ,'g', 'h', 'i', 'j','k', 'l', 'm','n'
                                        ,'o', 'p', 'q', 'r', 's', 't', 'u', 'v'
                                        ,'w', 'x', 'y', 'z', '!', '@', '#', '$'
                                        , '%', '^', '&', '*', '?','~']
    password = ""
    for i in range(15):
        numbers_to_add = str(random.randint(0, 9))
        characters = random.choice(possible_password_character_list)
        password_character_list.append(characters)
        password_character_list.append(numbers_to_add)
    for char in range(len(password_character_list)):
        password += password_character_list[char]
    return password
main()