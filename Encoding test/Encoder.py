import random
import hashlib
import secrets
class Encoder:
    def __init__(self, string_to_encode) -> None:
        self.string_to_encode = string_to_encode
        

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
    
    def binary_to_hash(self, b):
        
        list_to_hash = ""
        for i in b:
            list_to_hash += i

        c = list_to_hash.encode()
        h1 = hashlib.new('sha256')
        h1.update(c)
        c1 = h1.hexdigest()
        c2 = c1.encode()
        h2 = hashlib.new('sha256')
        h2.update(c2)
        c3 = h2.hexdigest()
        return c3
    
    def encode(self):
        f = open(r"C:\Users\summe\OneDrive\Desktop\personalprojects-1\Encoding test\dictionary.txt", 'r')
        
        words = []
        for line in f:
            line = line.strip().lower()
            words.append(line)
        s = self.string_to_encode.lower()
        
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
            c = self.binary_to_hash(b_list)
            
            
            encryped_string = secrets.token_hex() + c + secrets.token_hex()
            return print(encryped_string)
        else:
            return print("That is not a word.")

def main():
    user_input = input("Input a word to encrypt: ")
    encoder = Encoder(user_input)

    encoder.encode()

if __name__ == "__main__":
    main()
