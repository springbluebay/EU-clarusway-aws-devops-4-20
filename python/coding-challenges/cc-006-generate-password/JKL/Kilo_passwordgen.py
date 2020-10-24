from random import randint

def passwordgen(text):
    password = ""
    while len(password) < 3:
        password += text[randint(0,len(text)-1)].lower()
    return password + str(randint(1000,9999))

def passwordgen2(text):
    return "".join([text[randint(0,len(text)-1)].lower() for _ in range(3)]) + str(randint(1000,9999))

def passwordgen3(text):
    password = ""
    while len(password) < 3:
        x = randint(0,len(text)-1)
        password += text[x].lower()
    x = randint(1000,9999)    
    password += str(x)
    return password    

text = input("Please enter your full name: ")
print(passwordgen(text))

