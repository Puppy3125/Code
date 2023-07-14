import hashlib, os, sys, time

text = input("Password: ")
first = text[0]
os.system('cls')

partHashed = hashlib.sha256(text.encode('utf-8'))
hashed = partHashed.hexdigest()
print("Guess the password!")
print("First letter:", first)
print('''
Hash: {}
The hash is a encoded version of the password.
'''.format(hashed))
def theFunPart():
    guess = input("Answer: ")
    partHashed2 = hashlib.sha256(guess.encode('utf-8'))
    hashed2 = partHashed2.hexdigest()
    if hashed2 != hashed:
        print("Try again")
        print("")
        return theFunPart()
    if hashed2 == hashed:
        print("You won!")
        time.sleep(5)
        sys.exit()
theFunPart()