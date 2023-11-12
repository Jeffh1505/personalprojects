def list_recursion(li):
    if len(li) % 5 == 0:
        return li
    else:
        new_list = li.append(li[:-1] + 1)
        return list_recursion(new_list)
    

numbers = [1,3,4,5,10,11]
list_recursion(numbers)
print(numbers)