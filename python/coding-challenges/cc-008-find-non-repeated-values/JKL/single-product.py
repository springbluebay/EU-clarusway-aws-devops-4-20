def tekrar():
    #products = input("please enter the list: ")
    products = ["Pride and Prejudice", "To Kill a Mockingbird", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice", "In Cold Blood", "Wide Sargasso Sea",\
"One Hundred Years of Solitude", "Brave New World",  "The Great Gatsby", "Brave New World",\
"I Capture The Castle", "Brave New World", "The Great Gatsby", "The Great Gatsby",\
"One Hundred Years of Solitude", "Pride and Prejudice"]
    c = {}
    for i in products:
        if i in c:
            c[i] += 1
        else:
            c[i] = 1
    for i in c:
        if c[i] == 1 :
            print(i)

tekrar()