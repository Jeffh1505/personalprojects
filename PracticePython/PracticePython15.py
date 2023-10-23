def main():
    user_input = input("Please input a sentence: ")
    c = reverse_sentence(user_input)
    print(c)


def reverse_sentence(s):
    s = s.split(" ")
    reversed_list = s[::-1]
    reversed_string = ""
    for char in range(len(reversed_list)):
        reversed_string += reversed_list[char] + " "
    return reversed_string
main()