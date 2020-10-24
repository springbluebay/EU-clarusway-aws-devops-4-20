import random

def passcreator():
    name = input("please enter your name and surname without gap :")
    name = name.lower()
    numbers = [ '0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]
    if " " in name:
        print("please do not use gap")
        return passcreator()
    resultstr = ''.join(random.choice(name) for i in range(3))
    resultnumber = random.randrange(1000, 9999)
    resultnumber = str(resultnumber)
    #resultnumber2 = ''.join(random.choice(numbers) for i in range(4))
    #randomnumber = str(random.sample(range(1000,10000),1))
    #resultstr1 = random.choices(a, k=3)
    #resultnumber1 = random.choices(numbers, k = 4)
    #resultstr1 = "".join(resultstr)
    #resultnumber1 = "".join(resultnumber)
    toplam = resultstr + resultnumber
    #print(toplam)
    print(toplam)
passcreator()
    

