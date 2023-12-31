import random
def main():
    list_len = random.randint(1, 100)
    list = []
    for i in range(list_len):
        list.append(i)
    
    print(f"List: {list}")
    user_target = int(input("Please input a target in the list: "))
    list_index = binary_search(list, user_target, 0, len(list)-1)
    print(f"{user_target} is at index {list_index} in the list.")

def binary_search(list, target, low, high):
    middle = (low + high) // 2
    if target == list[middle]:
        return middle
    elif list[middle] > target:
        return binary_search(list, target, low, middle - 1)
    else:
        return binary_search(list, target, middle + 1, high)
    
if __name__ == "__main__":
    main()
