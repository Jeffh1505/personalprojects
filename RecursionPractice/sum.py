def main():
# compute and print 1 + 2 + ... + 10
    user_input = int(input("What number would you like to sum? "))
    print(sum(user_input))
def sum(x):
# you complete this function recursively
    if x == 1:
        return 1
    else: 
        return x + sum(x-1)
main()