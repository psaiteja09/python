import random

t = ["r", "p", "s"]
us=0
cs=0

computer = t[random.randint(0,2)]

player = False

while player == False:
    player = input("r, p, s?")
    if player == "q":
        print("User Score is ",us)
        print("Computer Score is ",cs)
        if us == cs:
            print("Tie!")
        elif us > cs:
            print("You win the game!,congratulations")
        else:
            print("You loose the game!,Better luck next time")
        exit()
    if player == computer:
        print("Tie!")
    elif player == "r":
        if computer == "p":
            print(computer, "covers", player)
            cs=cs+1
            print("cs=",cs)
        else:
            print(player, "smashes", computer)
            us=us+1
            print("us=",us)
    elif player == "p":
        if computer == "s":
            print(computer, "cut", player)
            cs=cs+1
            print("cs=",cs)
        else:
            print(player, "covers", computer)
            us=us+1
            print("us=",us)
    elif player == "s":
        if computer == "r":
            print(computer, "smashes", player)
            cs=cs+1
            print("cs=",cs)
        else:
            print( player, "cut", computer)
            us=us+1
            print("us=",us)
    else:
        print("That's not a valid play. Check your spelling!")
    player = False
    computer = t[random.randint(0,2)]
    