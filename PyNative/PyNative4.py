user_input = int(input("Please input a number: "))

for i in range(1, 10):
    if i % user_input == 0:
        print(i)
    else:
        continue