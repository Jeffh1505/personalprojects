def tower_of_hanoi(n, start, end, aux):
    if n == 1:
        return print(f"Disk 1 moved from {start} to {end}")
    else:
        tower_of_hanoi(n - 1, start, aux, end)
        print(f"Disk {n} moved from {start} to {end}")
        tower_of_hanoi(n - 1, aux, end, start)

n = int(input("Enter the number of disks: "))
print(tower_of_hanoi(n,'A','B','C'))