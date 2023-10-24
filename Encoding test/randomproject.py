def main():
    f = open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r')
     
    words = []
    for line in f:
         line = line.strip().lower()
         words.append(line)
    s = input("Please input a word: ").lower()
    if s in words:
         a = numper_split(s)
         return print(a) 
    else:
         return print("That is not a word")

def numper_split(s):
     import random
     a = []
     
     b = str(random.randint(0,9))
     number_splitted_word = ""
     for i in s:
          a.append(i)
     for i in a:
          number_splitted_word += i + b
     return number_splitted_word
main()