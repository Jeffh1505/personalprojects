N = int(input())
numbers_for_tuple = input().split(' ')
tuple_for_list = []
for i in range(N):
    elements_of_tuple = int(numbers_for_tuple[i])
    tuple_for_list.append(elements_of_tuple)
    
final_tuple = tuple(tuple_for_list)
print(final_tuple)
print(hash(final_tuple))

print(hash(1, 2))