import random
def rps():
    n = input("please choose one of them: rock, paper, scissor:?")
    n = n.lower()
    b = ["rock" , "paper", "scissor"]
    m = random.choice(b)
    computer = 0
    user = 0

    while computer < 3 or user < 3:
        if n not in b:
            print("please choose one of them: rock, paper, scissor:?")
            n = input("please choose one of them: rock, paper, scissor please:?").lower()
        elif n == "rock":
            if m == "rock":
                print("tie - no one wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
            elif m == "paper":
                computer += 1
                print("paper beats rock - computer wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
            elif m == "scissor":    
                user += 1
                print("rock beats scissors - user wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
        elif n == "paper":
            if m == "rock":
                user += 1
                print("paper beats rock - user wins")                
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
            elif m == "paper":
                print("tie - no one wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
            elif m == "scissor":
                computer += 1
                print("paper beats rock - computer wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")        
        elif n == "scissor":
            if m == "rock":
                computer += 1
                print("rock beats scissors - computer wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
            elif m == "paper":
                user += 1
                print("scissor beats paper - user wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
            elif m == "scissor":
                print("tie - no one wins")
                m = random.choice(b)
                #n = input("please choose one of them: rock, paper, scissor again:?")
        if computer == 3 or user  == 3:
            print(f"User won {user} time(s) and computer won {computer} time(s)")   
            break
        else:
            n = input("please choose one of them: rock, paper, scissor again:?")

rps()