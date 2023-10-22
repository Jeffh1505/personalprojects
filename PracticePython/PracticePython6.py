user_input = input("Please input a word: ").lower()
word_list = []
for char in user_input:
    word_list.append(char)

if word_list == word_list[::-1]:
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome")