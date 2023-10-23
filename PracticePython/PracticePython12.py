def main():
    a = [5, 10, 15, 20, 25]
    b = get_first_and_last(a)
    print(b)

def get_first_and_last(li):
    for i in range(len(li)):
        return li[0], li[-1]
main()