def main():
    list = [3,4,5,6,7,8,9,10,11]
    print(binary_search(list, 5, list[0], list[8]))

def binary_search(list, target, low, high):
    middle = list[(high + low) // 2]
    if middle == target:
        return list[middle]
    elif middle > target:
        return binary_search(list[:middle], target, list[0], list[len(list[middle])])
    else:
        return binary_search(list[middle:], target, list[middle], list[len(list[middle:])])
    

main()