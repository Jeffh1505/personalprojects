rows = 5
# outer loop
for i in range(0, rows + 1):
    # inner loop
    for j in range(rows - i, 0, -1):
        print(j, end=" ")
    print()