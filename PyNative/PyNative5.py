numbers = [12, 75, 150, 180, 145, 525, 50]

for i in range(len(numbers)):
    if numbers[i] % 5 == 0 and numbers[i] <= 150:
        print(numbers[i])
    elif numbers [i] > 500:
        break