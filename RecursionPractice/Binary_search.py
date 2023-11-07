def main():
    list = [3,4,5,6,7,8,9,10,11]
    print(binary_search(list, 5, 3, 11))

def binary_search(list, target, low, high):
    middle = (high + low) // 2
    print(middle)
    if list[middle] == target:
        return list[middle]
    elif middle > target:
        return binary_search(list, target, middle + 1, high)
    else:
        return binary_search(list, target, low, middle-1)
    

main()