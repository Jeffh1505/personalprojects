prime_numbers_list = []
for i in range(25, 50):
    for j in range(i//2):
        if i % j == 0:
            continue
        else:      
            prime_numbers_list.append(i)
print(prime_numbers_list)