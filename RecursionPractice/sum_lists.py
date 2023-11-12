def sum_lists(li, i=0):
    if len(list(li)) == 1:
        return li[i]
    
    else:
        return li[i] + sum_lists(li[i:], i + 1)
    

sum_lists([1, 2, [3,4], [5,6]])