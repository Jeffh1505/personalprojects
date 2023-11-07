from Binary_search import binary_search

list = []
for i in range(1000):
    list.append(i)

print(f"367 is at index {binary_search(list, 367, 0, len(list)-1)}")