def sum_lists(li, i=0):
    if len(li) == 1:
        return li
    print(sum_lists(li[i:], i+1))
    


sum_lists([1, 2, [3,4], [5,6]])