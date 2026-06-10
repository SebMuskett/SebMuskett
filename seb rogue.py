import random, keyboard, time

# stores all areas
areas = {}

# tracks player score
score = 0

# tracks bonus score 
bonusScore = 0

# tracks area the player is in
currentArea = 1

# tracks how many ares created
numOfAreas = 0

# starting player HP
playerHP = 100

# maximum player HP
playerMaxHP = 100

# minimum player HP
playerMinHP = 0

# tracks whether player survived a fight
playerSurvivedFight = True

# tracks if player has beat game
beatGame= False

# starting coordinates
player_x, player_y = 0 , 0

# coordinates after moving
newX, newY = 0 , 0

# limiting player movement
xLimitR, xLimitL = 13 , 0
yLimitD, yLimitU = 12 , 0

# tracks if player has pickaxe
havePickaxe = False

# tracks if player has just entered the game, starts true
isFirstLoop = True

# tracks which way the player is facing for pickaxe usage
player_facing = "right"

# counts the amount of frames
frame = 0

# text colour codes
BLACK = "\033[30m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
GREY = "\033[90m"

# background colours
BG_BLACK = "\033[40m"
BG_RED = "\033[41m"
BG_GREEN = "\033[42m"
BG_YELLOW = "\033[43m"
BG_BLUE = "\033[44m"
BG_MAGENTA = "\033[45m"
BG_CYAN = "\033[46m"
BG_WHITE = "\033[47m"
BG_ORANGE = "\033[48;5;208m"

# reset to default
RESET = "\033[0m"

# object tiles
blankTile = GREY + " ∙ " + RESET
enemyTile = BG_RED + RED + " ! " + RESET
healTile = GREEN + " @ " + RESET
wallTile = BG_WHITE + WHITE + " • " + RESET
pickTile = BLUE + " ⛏ " + RESET
endTile = BG_GREEN + blankTile + RESET

# player tiles
playerTileRight = MAGENTA + " > " + RESET
playerTileUp = MAGENTA + " ^ " + RESET
playerTileLeft = MAGENTA + " < " + RESET
playerTileDown = MAGENTA + " v " + RESET
playerTileCurrent = playerTileRight

# ----------------------------------------------------------------------------------------- FUNCTIONS

# clear tile in front of player
def clearTile(currentArea,newY,newX):
    areas[currentArea][newY][newX] = blankTile

# judges how well the player did, displayed at the end  or if they die
def judge(score, won):
    if won:
        if score < 25:
            return "Bad score. Must have been too easy."
        elif score >= 25 and score < 40:
            return "Okay score. Try again to get a better one!"
        elif score >= 40 and score < 70:
            return "Good score! It can still be improved upon though."
        elif score >= 70 and score < 90:
            return "Great score! Aim for perfect next time!"
        else:
            return "Exellent score! Must have been difficult, well done!"

    elif not won:
        if score < 25:
            return "Bad score. Better luck next time!"
        elif score >= 25 and score < 40:
            return "Okay score. Try again and i'm sure you got this!"
        elif score >= 40 and score < 70:
            return "Good score! Unfortunate death."
        elif score >= 70 and score < 90:
            return "Great score! try to win next time!"
        else:
            return "Exellent score! Must have been VERY difficult to die and get this, well done!"

# heals HP up to maximum
def heal(HP):
    global playerHP, playerMaxHP
    for i in range(HP):
        if playerHP < playerMaxHP:
            playerHP += 1
        else:
            break

# takes away HP down to minimum, where the player dies
def fight():
    global playerHP, playerSurvivedFight
    damage = random.randint(20,50)
    for i in range(damage):
        if playerHP > playerMinHP:
            playerHP -= 1
            playerSurvivedFight = True
        else:
            playerSurvivedFight = False
            break

# prints "pickaxe" or nothing if player has it or not
def pickaxeOutput():
    global havePickaxe
    if havePickaxe:
        return "pickaxe"
    else:
        return "------"

# make new random area
def generateNewArea(amount):
    global numOfAreas
    
    newArea = [

    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile,blankTile],
    [f"FLOOR {amount}"]

    ]

    for Ycount in range(0,len(newArea[0])-2):

        for Xcount in range(0,14):
            
            # starting location and adjacent tiles are always empty - makes the game more consistently possible
            if (Ycount == 0 and Xcount == 0) or (Ycount == 1 and Xcount == 0) or (Ycount == 0 and Xcount == 1):
                continue

            # ending tile cannot be overridden
            elif Ycount == 12 and Xcount == 13:
                newArea[Ycount][Xcount] = endTile
                continue
            
            # generate random number for every tile
            tileObject = random.randint(1,1000)

            if tileObject <= 425:                        # 42.5% chance to be blank
                newArea[Ycount][Xcount] = blankTile

            elif tileObject > 425 and tileObject <= 930: # 48% chance to be a wall
                newArea[Ycount][Xcount] = wallTile

            elif tileObject > 930 and tileObject <= 990: # 6% chance to be an enemy
                newArea[Ycount][Xcount] = enemyTile

            elif tileObject > 990 and tileObject <= 997: # 0.7% chance to be healing
                newArea[Ycount][Xcount] = healTile

            else:                                        # 0.3% chance to be pickaxe
                newArea[Ycount][Xcount] = pickTile

    numOfAreas += 1

    areas[numOfAreas] = newArea

    return newArea

# output screen (happens every frame)
def printArea(areaParam):
    print()
    print()
    print("--------------------------------------------")

    # loop through all Y-axis 
    for Ycount in range(0,13):
        print("|",end="")

        # loop through all X-axis
        for Xcount in range(0,13):

            # print coordinate with no new line
            print(areaParam[Ycount][Xcount],end="")

        # print final X coordinate with new line
        print(areaParam[Ycount][13],end="")
        print("|")

    print("--------------------------------------------")

    print("                 ",areaParam[13][0])
    print("     Your HP:",playerHP,"  Your inventory:",pickaxeOutput())

# checks if the tile the player is facing is a wall
def isWallTile(direction):
    global areas, currentArea, player_x, player_y

    if direction == "right":
        if areas[currentArea][player_y][player_x + 1] != wallTile:
            return False
    
    elif direction == "left":
        if areas[currentArea][player_y][player_x - 1] != wallTile:
            return False
        
    elif direction == "up":
        if areas[currentArea][player_y - 1][player_x] != wallTile:
            return False
        
    elif direction == "down":
        if areas[currentArea][player_y + 1][player_x] != wallTile:
            return False

    return True

# refreses screen
def refresh():
    print("\033[2J", end="")

# ----------------------------------------------------------------------------------------- PRE-GAME

# generate 3 areas
for newAreaCount in range(3):
    generateNewArea(newAreaCount+1)

# tutorial
input(f"""
      
Welcome to my game!
      
You are the {playerTileCurrent}

Your goal is to get from the top left to the bottom right.

Travel between the different floors to bypass walls and enemies.

You have a maximum of 100 HP.

You can only hold 1 item in your inventory at once.

{wallTile} is a wall. you cannot pass through this.

{enemyTile} is an enemy. you will attack them if you walk into one, then they will attack back.

{healTile} is a healing item, it heals 25HP.

{pickTile} is a pickaxe. Once you have it, you can use it to mine a wall in front of you.

Controls:

    Arrow keys - move
    1 - move to floor 1
    2 - move to floor 2
    3 - move to floor 3
    Space - use pickaxe

Press enter to start.
""")

# refresh screen
refresh()

# automatically press up so the player only has to press enter to begin
playerInput = "w"
pressed = True

# ----------------------------------------------------------------------------------------- MAIN LOOP

# loop only while player is supposed to be playing (not dead & not got to the end)
while playerHP > 0 and not beatGame:

    frame += 1

    if not isFirstLoop:
        pressed = False

    areas[currentArea][player_y][player_x] = blankTile


    # ---------------------------------- detecting key presses
    if keyboard.is_pressed("up"):
        playerInput = "w"
        pressed = True
        player_facing = "up"
        playerTileCurrent = playerTileUp

    elif keyboard.is_pressed("left"):
        playerInput = "a"
        pressed = True
        player_facing = "left"
        playerTileCurrent = playerTileLeft

    elif keyboard.is_pressed("down"):
        playerInput = "s"
        pressed = True
        player_facing = "down"
        playerTileCurrent = playerTileDown

    elif keyboard.is_pressed("right"):
        playerInput = "d"
        pressed = True
        player_facing = "right"
        playerTileCurrent = playerTileRight


    elif keyboard.is_pressed("space"):
        playerInput = "space"
        pressed = True


    elif keyboard.is_pressed("1"):
        playerInput = "1"
        pressed = True

    elif keyboard.is_pressed("2"):
        playerInput = "2"
        pressed = True

    elif keyboard.is_pressed("3"):
        playerInput = "3"
        pressed = True
    time.sleep(0.1)

    # ---------------------------------- if player has pressed a button
    if pressed:

        # ---------------------------------- UP
        if playerInput == "w":
            if player_y > yLimitU and not isWallTile("up"):
                newX = player_x
                newY = player_y - 1

        # ---------------------------------- LEFT
        elif playerInput == "a":
            if player_x > xLimitL and not isWallTile("left"):
                newX = player_x - 1
                newY = player_y

        # ---------------------------------- DOWN
        elif playerInput == "s":
            if player_y < yLimitD and not isWallTile("down"):
                newX = player_x
                newY = player_y + 1

        # ---------------------------------- RIGHT
        elif playerInput == "d":
            if player_x < xLimitR and not isWallTile("right"):
                newX = player_x + 1
                newY = player_y


        # ---------------------------------------------- INTERACTIONS

        # -------------------------- HEAL TILE
        if areas[currentArea][newY][newX] == healTile:
            heal(25)
            clearTile(currentArea,newY,newX)
            player_x, player_y = newX, newY

            score += 5

        # -------------------------- ENEMY TILE
        elif areas[currentArea][newY][newX] == enemyTile:
            fight()
            if playerSurvivedFight:
                clearTile(currentArea,newY,newX)
                score += 20

        # -------------------------- PICKAXE TILE
        elif areas[currentArea][newY][newX] == pickTile:
            havePickaxe = True
            clearTile(currentArea,newY,newX)
            score += 10
        
        # -------------------------- NOTHING
        else:
            player_x, player_y = newX, newY


        # ---------------------------------------------- CHANGE FLOORS
        if playerInput == "1" or playerInput == "2" or playerInput == "3":
            playerInput = int(playerInput)

            # if space is available to move
            if (areas[playerInput][player_y][player_x] == blankTile or areas[playerInput][player_y][player_x] == healTile):
                # move there
                currentArea = playerInput

            # if player spawns on healing item
            elif areas[playerInput][player_y][player_x] == healTile:
                
                # heal 25 HP
                heal(25)
                
                # remove heal item
                areas[playerInput][player_y][player_x] = blankTile

                # move there
                currentArea = playerInput

            else:
                continue


        # ---------------------------------- PICKAXE
        if playerInput == "space":
            if havePickaxe:

                # mine in the direction the player is facing

                # ---------------------------------- RIGHT
                if player_facing == "right" and isWallTile("right"):
                    areas[currentArea][newY][newX + 1] = blankTile

                # ---------------------------------- LEFT
                elif player_facing == "left" and isWallTile("left"):
                    areas[currentArea][newY][newX - 1] = blankTile

                # ---------------------------------- UP
                elif player_facing == "up" and isWallTile("up"):
                    areas[currentArea][newY - 1][newX] = blankTile

                # ---------------------------------- DOWN
                elif player_facing == "down" and isWallTile("down"):
                    areas[currentArea][newY + 1][newX] = blankTile

                score += 10

            # refresh so it updates
            refresh()

            # remove pickaxe
            havePickaxe = False

        # move player icon to new location
        areas[currentArea][player_y][player_x] = playerTileCurrent

        # refresh so it updates
        print("\033[H", end="")

        # print area again
        printArea(areas[currentArea])

        # if player is overlapping with end tile
        if player_x == 13 and player_y == 12:
            beatGame = True

        if frame % 50 == 0:
            bonusScore += 1

    # all loops after first are not the first loop
    isFirstLoop = False

# when player has either died or won
if beatGame:
    print("\nCONGRATULATIONS! You got to the end!")
else:
    print("\nUnfortunately, you died. Better luck next time!")
    score -= 40

totalScore = score + bonusScore

time.sleep(0.8)

# output score
print("\nYour score:",totalScore,"\n")

time.sleep(0.8)

# output judgement
print(judge(totalScore, beatGame),"\n")

# ----------------------------------------------------------------------------------------- SCOREBOARD

time.sleep(0.8)

# wait until no relevant keys are pressed
while any(keyboard.is_pressed(k) for k in ["1", "2", "3", "up", "down", "left", "right", "space"]):
    time.sleep(0.05)
    
track = input("Do you want to put your score on the leaderboard? y or n > ")

if track == "y":
    scoreTracker = open("scores.txt","a")
    scoreTracker.write(f"{totalScore}\n")

    scoreFile = open("scores.txt","r")  
    highestScore = 0
    for line in scoreFile:
        score = int(line)
        if score > highestScore:
            highestScore = score

    if totalScore >= highestScore:
        print("\nWOW! You got the highest score of anyone so far! Great job!")
        highestScore = totalScore
        time.sleep(0.8)

    print(f"\nHighest score this evening: {highestScore}")
    scoreFile.close()
    scoreTracker.close()

time.sleep(0.8)

print("\nGame made by Seb :) feel free to play again for a better score!\n")

time.sleep(1)