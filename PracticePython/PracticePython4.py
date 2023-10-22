user_input = int(input("Please input a number: "))

divisible_number_list = []

for i in range(1,user_input):
    if user_input % i == 0:
        divisible_number_list.append(i)
    else:
        continue
print(divisible_number_list)