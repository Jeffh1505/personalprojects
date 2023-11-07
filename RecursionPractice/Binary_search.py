def main():
    list = [3,4,5,6,7,8,9,10,11]
    print(binary_search(list, 5, 3, 11))

def binary_search(list, target, low, high):
    middle = (low + high) // 2
    print(middle)
    if target == list[middle]:
        return list[middle]
    elif target > list[middle]:
        return binary_search(list, target, low, middle + 1)
    else:
        return binary_search(list, target, middle - 1, high)
    

main()