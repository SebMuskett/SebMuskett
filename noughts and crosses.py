#-------------------------------------------------------------------- VARIABLES & FUNCTIONS
# andre rumplestiltskin george huckleberry esquire bashford the 82th
# spongbop
# bink dink mcspink the 3rd wants to talk to you

won = False

topboard = [" "," "," "]
midboard = [" "," "," "] # board
botboard = [" "," "," "]

def printboard():
    print(f"""
     |      |     
  {topboard[0]}  |   {topboard[1]}  |  {topboard[2]}  
     |      |     
------------------
     |      |     
  {midboard[0]}  |   {midboard[1]}  |  {midboard[2]}  
     |      |     
------------------
     |      |     
  {botboard[0]}  |   {botboard[1]}  |  {botboard[2]}  
     |      |     
""")

def wincheck(player, pos1, pos2, pos3):
    global winner
    global won
    if pos1 == pos2 == pos3 and pos1 != " ":
        winner = player
        won = True

def row_any_space(row):
    return row[0]==" " or row[1]==" " or row[2]==" "

def any_playable_spaces():
    return row_any_space(topboard) or row_any_space(midboard) or row_any_space(botboard)

def have_i_won():
    global won
    return won

#-------------------------------------------------------------------- PLAY FUNCTION

def play(horizontal, vertical, player): # play function


            # top input
    if horizontal == "top":
        if vertical == "left": # top left
            if topboard[0] == " ":
                topboard[0] = player
            else:
                print("no")
        elif vertical == "middle": # top middle
            if topboard[1] == " ":
                topboard[1] = player
            else:
                print("no")
        elif vertical == "right": # top right
            if topboard[2] == " ":
                topboard[2] = player
            else:
                print("no")


            # middle input
    elif horizontal == "middle":
        if vertical == "left": # middle left
            if midboard[0] == " ":
                midboard[0] = player
            else:
                print("no")
        elif vertical == "right": # middle right
            if midboard[2] == " ":
                midboard[2] = player
            else:
                print("no")


            # bottom input
    elif horizontal == "bottom":
        if vertical == "left": # bottom left
            if botboard[0] == " ":
                botboard[0] = player
            else:
                print("no")
        elif vertical == "middle": # bottom middle
            if botboard[1] == " ":
                botboard[1] = player
            else:
                print("no")
        if vertical == "right": # bottom right
            if botboard[2] == " ":
                botboard[2] = player
            else:
                print("no")

#-------------------------------------------------------------------- GAME LOOP

while not have_i_won() and any_playable_spaces():
    # ^ if no one has won and the board isnt full

    p1input = input("player 1 input position: ") # p1 input
    if p1input != "middle": # "middle" check
        p1input = p1input.split()
        p1horizontal = p1input[0] # input split
        p1vertical = p1input[1]
        play(p1horizontal,p1vertical,"X") # play
    else:
        if midboard[1] != " ": # override check
            print("no")
        else:
            midboard[1] = "X" # "middle"

    for i in range(50):
        print()
    printboard()

    # P1 WIN CHECKS
    wincheck("X",topboard[0],topboard[1],topboard[2]) # top row
    wincheck("X",midboard[0],midboard[1],midboard[2]) # H middle row
    wincheck("X",botboard[0],botboard[1],botboard[2]) # bottom row
    wincheck("X",topboard[0],midboard[0],botboard[0]) # left row
    wincheck("X",topboard[1],midboard[1],botboard[1]) # V middle row
    wincheck("X",topboard[2],midboard[2],botboard[2]) # bottom row
    wincheck("X",topboard[0],midboard[1],botboard[2]) # TL diagonal
    wincheck("X",topboard[2],midboard[1],botboard[2]) # TR diagonal


    if not have_i_won() and any_playable_spaces():

        p2input = input("player 2 input position: ") # p2 input
        if p2input != "middle": # "middle" check
            p2input = p2input.split()
            p2horizontal = p2input[0] # input split
            p2vertical = p2input[1]
            play(p2horizontal,p2vertical,"O") # play
        else:
            if midboard[1] != " ": # override check
                print("no")
            else:
                midboard[1] = "O" # "middle"  

        for i in range(50):
            print()
        printboard()

        # P2 WIN CHECKS
        wincheck("O",topboard[0],topboard[1],topboard[2]) # top row
        wincheck("O",midboard[0],midboard[1],midboard[2]) # H middle row
        wincheck("O",botboard[0],botboard[1],botboard[2]) # bottom row
        wincheck("O",topboard[0],midboard[0],botboard[0]) # left row
        wincheck("O",topboard[1],midboard[1],botboard[1]) # V middle row
        wincheck("O",topboard[2],midboard[2],botboard[2]) # bottom row
        wincheck("O",topboard[0],midboard[1],botboard[2]) # TL diagonal
        wincheck("O",topboard[2],midboard[1],botboard[0]) # TR diagonal   
        

if not any_playable_spaces() and not have_i_won():
    print("TIE!")
elif have_i_won():
    print("CONGRATULATIONS,",winner,"WON!")