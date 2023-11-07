def main():
    user_base = int(input("What is your base? "))
    user_exp = int(input("What is your power? "))
    number = exponent(user_base, user_exp)
    print(f"Result: {number}")

def exponent(base, exp):
    if exp == 0:
        return 1
    else:
        result = base * exponent(base, exp - 1)
        return result

if __name__ == "__main__":
    main()