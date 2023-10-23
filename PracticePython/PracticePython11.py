def main():
    user_input = int(input("Please input a number: "))
    get_divisors(user_input)

def get_divisors(s):
    counter = 0

    for i in range(1,s):
        if s % i == 1:
          counter += 1  
        elif s % i == 0 and i != 1:
            return print(f"{s} is not prime")
    if counter != 0:
        return print(f"{s} is a prime number.")

main()