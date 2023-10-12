import random

code = str(random.randint(1000, 9999))
print(code)
guessed_codes = []
correct_numbers = []
tries = 0
#Creates game loop
while True:
    user_input = str(input("Guess the code: ")) #Takes user input

    if user_input in code:
        correct_numbers.append(user_input)
        print("Correct guess")
        if set(correct_numbers) == set(code):
            print(f"You got it, {code} was the code!")
            break    
    else: 
        tries += 1
        if tries == 5:
            print(f"You lost, {code} was the code.")
            break
    part_of_code_to_display = ""
    for number in code:
        if number in correct_numbers:
            part_of_code_to_display += number
        else: 
            part_of_code_to_display += "_"
    print(part_of_code_to_display)