prime_numbers_list = []
for i in range(25, 50):
    for j in range(1, 11):
        for c in range(i):
            if  j * c == i and j != 1:
                continue
            else:
                prime_numbers_list.append(i)

print(prime_numbers_list)