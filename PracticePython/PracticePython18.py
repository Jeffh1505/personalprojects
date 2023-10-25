import random
def main():
    while True:
        user_input = input("Please input a number: ")
        c = cow_bulls(user_input)
        if c == "4 cows, 0 bulls":
            print("You got it")
            break
        else:
            print(c)
            continue
def cow_bulls(s):
    number_to_guess = str(random.randint(1000, 9999))
    cows = 0
    bulls = 0
    for num in range(len(number_to_guess)):
        if s[num] == number_to_guess[num]:
            cows += 1
        elif s[num] in number_to_guess and s[num] != number_to_guess[num]:
            bulls += 1
    return f"{cows} cows, {bulls} bulls"
main()