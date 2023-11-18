def even_numbers(n, x):
    even_numbers_list = []
    for i in range(n, x):
        if i % 2 == 0:
            even_numbers_list.append(i)
        else:
            continue
    return even_numbers_list
    

print(even_numbers(4, 30))