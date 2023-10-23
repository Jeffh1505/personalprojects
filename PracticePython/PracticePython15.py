def main():
    user_input = input("Please input a sentence: ")
    c = reverse_sentence(user_input)
    print(c)


def reverse_sentence(s):
    s = s.split(" ")
    print(s)
    reversed_list = ""
    for char in s:
        reversed_list += s[-1]
    return reversed_list
main()