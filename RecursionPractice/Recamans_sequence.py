def recaman(n):
    reacman_sequence_list = []
    reacman_sequence_list.append(n)
    print(reacman_sequence_list)
    if n == 0:
        return 0
    
    if n > 0 and n not in reacman_sequence_list:
        return recaman(n-1) - n
        
    else:
         return recaman(n-1) + n
         
    

print(recaman(6))
