import random
class Encoder:
    def __init__(self, string_to_encode) -> None:
        self.string_to_encode = string_to_encode
        self.encoded_string = ""

    def caesar_cypher(self, word):
        letter_to_number = {'a': "f", "b": "g", 'c':"h", 'd':"i", 'e': "j",'f':"k",'g':"l",
                        'h':"m", 'i':"n", 'j':"o", 'k':"p", 'l':"q", 'm':"r", 'n':"s",
                        'o':"t", 'p': "u", 'q': "v", 'r':"w", 's':"x", 't':"y", 'u':"z",
                        'v':"a", 'w':"b", 'x':"c", 'y':"d", 'z':"e"}
        encoded_word_list = []
        encoded_word = ""
        
        for char in word:
            encoded_word_list.append(letter_to_number[char])    
        for x in encoded_word_list:
            encoded_word += x
        return encoded_word    

    def encode_numerically(self, word):
        #This function encodes the letter to a number 1 through 26
        letter_to_number = {'a': "1", "b": "2", 'c':"3", 'd':"4", 'e': "5",'f':"6",'g':"7",
                        'h':"8", 'i':"9", 'j':"10", 'k':"11", 'l':"12", 'm':"13", 'n':"14",
                        'o':"15", 'p': "16", 'q': "17", 'r':"18", 's':"19", 't':"20", 'u':"21",
                        'v':"22", 'w':"23", 'x':"24", 'y':"25", 'z':"26"}
        encoded_word_list = []
        encoded_word = ""
        
        for char in word:
            encoded_word_list.append(letter_to_number[char])    
        for x in encoded_word_list:
            encoded_word += x + "_"
        return encoded_word

    def encode_binary(self, a):
        #This function encodes the number that results from encoding the word into binary
        if a == 0:
            return ''
        if a % 2 == 1:
            last_bit = '1'
        else:
            last_bit = '0'
        prefix = self.encode_binary(a//2)
        return prefix + last_bit
    def encode(self):
        f = open(r"C:\Users\summe\OneDrive\Desktop\E1006\dictionary.txt", 'r')
        import random 
        words = []
        for line in f:
            line = line.strip().lower()
            words.append(line)
        s = input("Please input a word: ").lower()
        
        if s in words:
            x = self.caesar_cypher(s)
            a = self.encode_numerically(x)
            a = a.split("_")
            a = a[:-1]
            b_list = []
            for number in a:
                number = int(number)
                b = self.encode_binary(number)
                b_list.append(b)
            
            random.shuffle(b_list) #This shuffles the binary encoded string 
            encoded_word_string = ""
            for i in range(len(b_list)):
                encoded_word_string += b_list[i] + "_"
            return print("Encoded word:", encoded_word_string) 
        else:
            return print("That is not a word.")