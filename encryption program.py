import random
import string

char = " " + string.punctuation + string.digits + string.ascii_letters
char = list(char)
key = char.copy()

random.shuffle(key)

#encrypt

plaintext = input("Enter a message to encrypt : ")
randomtext = ""

for letter in plaintext :
    index = char.index(letter)
    randomtext += key[index]

print(f"original message : {plaintext}")
print(f"encrypted message : {randomtext}")

#dencrypt

randomtext = input("Enter a message to encrypt : ")
plaintext = ""

for letter in randomtext :
    index = key.index(letter)
    plaintext += char[index]

print(f"original message : {randomtext}")
print(f"encrypted message : {plaintext}")

