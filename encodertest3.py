def main():
    f = open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r')
    import random 
    words = []
    for line in f:
         line = line.strip().lower()
         words.append(line)
    s = input("Please input a word: ").lower()
    
    if s in words:
        x = caesar_cypher(s)
        a = encode_numerically(x)
        b = encode_binary(a)
        b = b.split("_")
        random.shuffle(b) #This shuffles the binary encoded string 
        return print("Encoded word:", b) 
    else:
        return print("That is not a word.")
def caesar_cypher(s):
    letter_to_number = {'a': "f", "b": "g", 'c':"h", 'd':"i", 'e': "j",'f':"k",'g':"l",
                    'h':"m", 'i':"n", 'j':"o", 'k':"p", 'l':"q", 'm':"r", 'n':"s",
                     'o':"t", 'p': "u", 'q': "v", 'r':"w", 's':"x", 't':"y", 'u':"z",
                     'v':"a", 'w':"b", 'x':"c", 'y':"d", 'z':"e"}
    encoded_word_list = []
    encoded_word = ""
    
    for char in s:
        encoded_word_list.append(letter_to_number[char])    
    for x in encoded_word_list:
        encoded_word += x
    return encoded_word    

def encode_numerically(s):
    #This function encodes the letter to a number 1 through 26
    letter_to_number = {'a': "1", "b": "2", 'c':"3", 'd':"4", 'e': "5",'f':"6",'g':"7",
                    'h':"8", 'i':"9", 'j':"10", 'k':"11", 'l':"12", 'm':"13", 'n':"14",
                     'o':"15", 'p': "16", 'q': "17", 'r':"18", 's':"19", 't':"20", 'u':"21",
                     'v':"22", 'w':"23", 'x':"24", 'y':"25", 'z':"26"}
    encoded_word_list = []
    encoded_word = ""
    
    for char in s:
        encoded_word_list.append(letter_to_number[char])    
    for x in encoded_word_list:
        encoded_word += x + "_"
    return encoded_word

def encode_binary(a):
    #This function encodes the number that results from encoding the word into binary
    number_to_binary = {'1': "1", '2': "10", '3':"11", '4': "100", 
                        '5': "101", '6': "110", '7':"111", '8': "1000", 
                        '9':"1001", '10':"101", '11':"1011", '12':"1100",
                        '13': "1101", '14':"1110", '15':"1111", '16':"10000",
                        '17':"10001", '18':"10010", '19':"10011", '20':"10100",
                        '21':"10101", '22':"10110", '23':"10111", '24':"11000",
                        '25':"11001", '26':"11010"}
    binary_encoded_list = []
    binary_encoded_word = ""
    split_a = a.split('_')
    
    split_a_2 = split_a[:-1]
    for number in split_a_2:
        binary_encoded_list.append(number_to_binary[number])
    for x in binary_encoded_list:
        binary_encoded_word += x + "_"
    return binary_encoded_word
main()
