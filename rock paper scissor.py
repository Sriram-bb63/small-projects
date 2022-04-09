import random

print("\n\n\tWelcome!\nRock Paper Scissor")

x=[]
y=[]
def game():
    while len(x)<5 and len(y)<5:
        items=["r","p","s"] 
        pcturn=random.choice(items)
        print("Your score=",len(x))
        print("Computer score=",len(y))
        print("\nYour turn!")
        turn=input("Enter your choice: ")
        print("Computer choice:",pcturn)
        if turn not in items:
            print("\n!!!!!!!!!!\nEnter only valid inputs\n!!!!!!!!!!")
            hlp()
        print("\n")
        if pcturn==turn:
            print("DRAW")
            game()                  
        elif pcturn=="r" and turn=="p":
            x.append(1)
            print("ONE POINT FOR YOU!")
            game()
        elif pcturn=="r" and turn=="s":
            y.append(1)
            print("ONE POINT FOR THE COMPUTER!")
            game()
        elif pcturn=="p" and turn=="r":
            y.append(1)
            print("ONE POINT FOR THE COMPUTER!")
            game()
        elif pcturn=="p" and turn=="s":
            x.append(1)
            print("ONE POINT FOR YOU!")
            game()
        elif pcturn=="s" and turn=="p":
            y.append(1)
            print("ONE POINT FOR THE COMPUTER!")
            game()
        elif pcturn=="s" and turn=="r":
            x.append(1)
            print("ONE POINT FOR YOU!")
            game()
        else:
            pass
        if len(x)>=5 or len(y)>=5:
            if len(x)>=5:
                print("You are the winner!")
                input("Press ENTER to go to start screen")
                startscreen()
            elif len(y)>=5:
                print("You lose! The computer won\nBetter luck next time :-)")
                input("Press ENTER to go to start screen")
                startscreen()

def hlp():
    print("\n->Valid user inputs:")
    print("\tRock=r\n\tPaper=p\n\tScissor=s\n")
    print("->Points to win: 5\n")
    print("->Please refrain from giving any input other than those mentioned above.")
    input("\nPress ENTER to go to start screen")
    startscreen()

def startscreen():
    print("\nTo know the RULES, press 1 and ENTER\nTo START, press 2 and ENTER")
    strt=(input())
    if strt=="2":
        game()
    elif strt=="1":
        hlp()
    else:
        print("Enter a valid input!")
        startscreen()

startscreen()
