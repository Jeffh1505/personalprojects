def main():
# compute and print 1 + 2 + ... + 10
    print(sum(450))
def sum(x):
# you complete this function recursively
    if x == 1:
        return 1
    else: return x + sum(x-1)
main()