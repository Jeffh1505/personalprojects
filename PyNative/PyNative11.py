prime_numbers_list = []
for i in range(25, 50):
    for j in range(1, 11):
        if i % j == 1:
            prime_numbers_list.append(i)

print(prime_numbers_list)