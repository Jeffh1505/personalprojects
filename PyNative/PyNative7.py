rows = 5
# outer loop
for i in range(1, rows + 1):
    # inner loop
    for j in range(1, i + 1, -1):
        print(j, end=" ")
    print('')