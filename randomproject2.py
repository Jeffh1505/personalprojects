
from encodertest3 import encode_numerically
from encodertest3 import encode_binary
from encodertest3 import caesar_cypher
import hashlib
s = input("Input a word: ")
x = caesar_cypher(s)
a = encode_numerically(x)
b = encode_binary(a)
list_to_hash = ""
for i in b:
    list_to_hash += i
    c = list_to_hash.encode()
h = hashlib.new('sha256')
h.update(c)
c = h.hexdigest()
print(c)
