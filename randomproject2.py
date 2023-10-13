
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
h1 = hashlib.new('sha256')
h1.update(c)
c1 = h1.hexdigest()
c2 = c1.encode()
h2 = hashlib.new('sha256')
h2.update(c2)
c3 = h2.hexdigest()
print(c3)

