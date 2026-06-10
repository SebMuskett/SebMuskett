import random
import time

#---------------------------ERROR HANDLING---------------------------#

class Error(Exception):
    pass

class TooSmallError(Error):
    pass
class TooLargeError(Error):
    pass
class WrongTypeError(Error):
    pass

#---------------------------FUNCTIONS---------------------------#

# make space between goes
def space(gap):
    for i in range(gap):
        print()

# functions to input data - boxes, presents, players
def getBoxes():
    flag = True
    while flag:
        boxes = input("How many boxes? ")

        try:
            boxes = int(boxes)

            if boxes < 1:
                raise TooSmallError
            else:
                flag = False

        except TooSmallError:
            print("1 or more boxes are required. Try again.")
        except Exception:
            print("Please input a number.")

    return boxes
def getPresents():
    flag = True
    while flag:
        presents = input("How many presents? ")

        try:
            presents = int(presents)

            if presents < 1:
                raise TooSmallError
            elif presents > boxes:
                raise TooLargeError
            else:
                flag = False

        except TooSmallError:
            print("Number must be 1 or above. Try again.")
        except TooLargeError:
            print("Presents must not exceed number of boxes.")
        except Exception:
            print("Please input a number.")
    return presents
def getPlayers():
    flag = True
    while flag:
        players = input("How many players? ")

        try:
            players = int(players)

            if players < 2:
                raise TooSmallError
            else:
                flag = False

        except TooSmallError:
            print("2 or more players must play. Try again.")
        except Exception:
            print("Please input a number.")
    return players

# create boxList, true is loaded, false is blank
def createBoxList():
    boxList = []
    for i in range(presents):
        boxList.append(True)
    for i in range(boxes-presents):
        boxList.append(False)

    return boxList

# check if player is not gifted
def isNotGifted(player):
    return players[player]

# gift player
def gift(player):
    global activePlayerIndex, activePlayerReal
    activePlayerIndex -= 1
    activePlayerReal =- 1
    players.remove(player)

# check if multiple players are not gifted
def someNotGifted():
    return len(players) > 0

# check if multiple gifts are remaining
def someGiftsRemaining():
    return (True in boxList)

# proceeds to next player or returns to first player
def nextPlayer(activePlayerReal, activePlayerIndex):
    if activePlayerReal == players[-1]:
        activePlayerReal = 1
        activePlayerIndex = 0
    else:
        activePlayerReal += 1
        activePlayerIndex += 1
    return activePlayerReal

# print all players that are not gifted
def printNotGifted():
    for player in players:
        print(player,end=" ")
    print()

# print all players that are gifted
def printGifted():
    if giftedPlayers == []:
        print("None")
    for player in giftedPlayers:
        print(player,end=" ")
    print()

# print amount of gifts or empties remaining
def getAmount(TorF):
    count = 0
    for item in boxList:
        if item == TorF:
            count += 1
    return count

#---------------------------SETUP---------------------------#

print("\nThis is an innocent game where you get presents!! YAY!!!")
print("It works coincidentally similarly to a specific... roulette game\n")

print("Boxes determines how many boxes there are to open.")
print("Presents determines how many presents are spread across those boxes.")
print("Each player opens 1 box per turn. If it's a gift, you're out! But you get a gift so it's good. Not like you die or anything. Who would make a game like that!")
print("Every box that is opened is removed from the pile, reducing the amount of boxes ramaining.\n")

# input data
boxes = getBoxes()
print()
presents = getPresents()
print()
noOfPlayers = getPlayers()

# create player list - contains not gifted players
players = []
for i in range(noOfPlayers):
    players.append(i+1)

# gifted players updates as players die
giftedPlayers = []

# create boxes
boxList = createBoxList()

# starting player
activePlayerIndex = 0
activePlayerReal = 1

#---------------------------GAME LOOP---------------------------#

# while more than 1 person is not gifted, keep playing
while someNotGifted() and someGiftsRemaining():

    space(30)

    print(f"\nPlayers not gifted: ",end="")
    printNotGifted()

    print("\nPlayers gifted: ",end="")
    printGifted()

    print(f"Chance of getting a gift: {getAmount(True)}/{len(boxList)} ({round(getAmount(True)/len(boxList)*100)}%)")

    input(f"\nPlayer {activePlayerReal}, press enter to open the mystery box!")
    print("You pull the ribbon...")

    time.sleep(2)
    # pick random item in boxList
    randNum = random.randint(0, len(boxList)-1)

    # if index of random number in boxList is True, player dies
    if boxList[randNum] == True:
        print("You got a present! Yay!")
        giftedPlayers.append(activePlayerReal)
        gift(activePlayerReal)
    else:
        print("It's empty. Unfortunate!")

    # remove present from boxList
    boxList.pop(randNum)

    time.sleep(1.5)

    # increment players
    activePlayerReal = nextPlayer(activePlayerReal, activePlayerIndex)


print(f"\nFinished!\n")
print(f"\nThe following people were gifted: ",end="")
printGifted()
print(". Lucky you!")
print(f"\nPlayers not gifted: ",end="")
printNotGifted()
print(". Better luck next time!")

