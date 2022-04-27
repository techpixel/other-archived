import replit
from collections import OrderedDict
from pprint import pprint

#cipher_input = input("input: ")
#cipher_key = input("key: ")

cipher_input = "My ancestors are just plain dancers waiting their chance at freedom"

cipher_key = "yeaok"

replit.clear()

i = 0
newkey = ""
while len(cipher_input) > len(newkey):
    i = i % len(cipher_key)
    
    if cipher_input[len(newkey)] == " ":
        newkey += " "
    else:
        newkey += cipher_key[i]
        i += 1

replit.clear()

print(cipher_input)
print(newkey)

input()
replit.clear()

class CipherDict:
    def __init__(self, a,b):
        self.a = a
        self.b = b

    

input()