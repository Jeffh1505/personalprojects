user_input = int(input("Please input a number: "))

for i in range(1, user_input):
    if user_input % i == 0:
        print(i)
    else:
        continue