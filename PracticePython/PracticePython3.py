a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
user_input = input("Please input a number ")
for number in a:
    if number <= int(user_input):
        print(number)
    else:
        continue