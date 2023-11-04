prime_numbers_list = []
for i in range(25, 50):
    for j in range(11):
        if j * i != i:
            prime_numbers_list.append(i)

print(prime_numbers_list)