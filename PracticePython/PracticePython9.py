import random
number_to_guess = random.randint(1,9)
another = True
while another:
    user_input = int(input("Please guess a number: "))
    if user_input == number_to_guess:
        print("You got it!")
    elif user_input > number_to_guess:
        print("Too high, try again.")
        continue
    elif user_input < number_to_guess:
        print("Too low, try again.")
        continue
    continue_game = input("Would you like to try again? (y/n): ")
    if continue_game == 'n':
        break
