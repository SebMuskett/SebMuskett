import random
mode = int(input("1 player or 2? "))
play = True

p1wins = 0
p2wins = 0
cpuwins = 0
draws = 0

def printscoreboard():
    print()
    print("scoreboard:")
    print("player 1 wins:",p1wins)
    if mode == 2:
        print("player 2 wins:",p2wins)
    else:
        print("cpu wins:",p2wins)
    print("draws:",draws)
    print()

def makeSpace():
    for i in range(50):
        print()

#---------------------------------------------------------------------------

if mode == 2:
    while play == True:
        p1input = input("p1, rock, paper or scissors? ")
        makeSpace()
        p2input = input("p2, rock, paper or scissors? ")
        print()
        
        # DRAW
        if p1input == "rock" and p2input == "rock":
            print("draw")
            draws += 1
        elif p1input == "paper" and p2input == "paper":
            print("draw")
            draws += 1
        elif p1input == "scissors" and p2input == "scissors":
            print("draw")
            draws += 1

        # P1 WIN
        elif p1input == "rock" and p2input == "scissors":
            print("p1 wins!")
            p1wins += 1
        elif p1input == "paper" and p2input == "rock":
            print("p1 wins!")
            p1wins += 1
        elif p1input == "scissors" and p2input == "paper":
            print("p1 wins!")
            p1wins += 1

        # P2 WIN
        else:
            print("p2 wins")
            p2wins += 1

        printscoreboard()

        playAgain = input("wanna play again? ")
        
        if playAgain != "no":
            play = True
        else:
            play = False

#---------------------------------------------------------------------------

elif mode == 1:
    while play == True:
        p1input = input("p1, rock, paper or scissors? ")
        print()
        
        num = random.randint(1,3)
        if num == 1:
            p2input = "rock"
        elif num == 2:
            p2input = "paper"
        elif num == 3:
            p2input = "scissors"

        print("the cpu chose",p2input)

        # DRAW
        if p1input == "rock" and p2input == "rock":
            print("draw")
            draws += 1
        elif p1input == "paper" and p2input == "paper":
            print("draw")
            draws += 1
        elif p1input == "scissors" and p2input == "scissors":
            print("draw")
            draws += 1

        # P1 WIN
        elif p1input == "rock" and p2input == "scissors":
            print("p1 wins!")
            p1wins += 1
        elif p1input == "paper" and p2input == "rock":
            print("p1 wins!")
            p1wins += 1
        elif p1input == "scissors" and p2input == "paper":
            print("p1 wins!")
            p1wins += 1

        # CPU WIN
        else:
            print("cpu wins")
            p2wins += 1

        printscoreboard()

        playAgain = input("wanna play again? ")
        
        if playAgain == "yes":
            play = True
        else:
            play = False