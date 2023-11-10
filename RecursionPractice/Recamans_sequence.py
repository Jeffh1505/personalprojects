def recaman(n):
    reacman_sequence_list = []
    reacman_sequence_list.append(n)
    if n == 0:
        return 0
    
    if n > 0 and n not in reacman_sequence_list:
        c = recaman(n-1) - n
        return reacman_sequence_list
    else:
         c = recaman(n-1) + n
         return reacman_sequence_list
    

print(recaman(2))
