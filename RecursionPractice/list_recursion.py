def list_recursion(li):
    if len(li) % 5 == 0:
        return li
    else:
        c = li[-1] + 1
        li.append(c)
        return list_recursion(li)
         
    

numbers = [1,3,4,5,10,11]
print(list_recursion(numbers))
