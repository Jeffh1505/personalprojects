
while True:
    user_input_1 = input("Player 1: Please choose (r)ock, (p)aper or (scissors): ")
    user_input_2 = input("Player 2: Please choose (r)ock, (p)aper or (scissors): ")
    if user_input_1 == user_input_2:
        print("Draw")
        continue
    elif (user_input_1 == 'r' and user_input_2 == 'p') or (user_input_1 == 's' and user_input_2 == 'r') or (user_input_1 == 'p' and user_input_2 == 's'):
        print("User 2 wins")
        break
    elif (user_input_1 == 'p' and user_input_2 == 'r') or (user_input_1 == 'r' and user_input_2 == 's') or (user_input_1 == 's' and user_input_2 == 'p'):
        print("User 1 wins")
        break