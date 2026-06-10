import time

inventory = []

# technical vars
gameRunning = True

cmdValid = False

# progression vars
haveBone = False

haveJewels = False

haveTranslator = False

haveQK = False

haveCodes = False

machineActivated = False

upgradedMachine = False

# dialogue vars
talkedToLizards = False

talkedToCaves = False

talkedToScientists = False

talkedToVictorians = False

# location vars
location = "laboratory"

directions = ["north","east","south","west"]

possibleCmd2s = {
    "places": ["laboratory","code room","break room","machine room","time machine","victorian times","stone age","future"],
    "items": ["dino bone","codes","crown jewels","translator","quantum knowledge","coffee"],
    "interactibles": ["scientists","code machine","cave people","queen victoria","lizard people"]
}


# ----------------------------------- STARTING FUNCTIONS ----------------------------------- #


# PRINT IN SEQUENCE
def printSequence(string):
    for letter in string:
        print(letter,end="",flush=True)
        time.sleep(0.03)
    print()


# PRINT IN SEQUANCE (no new line)
def printSequenceNNL(string):
    for letter in string:
        print(letter,end="",flush=True)
        time.sleep(0.03)


def objectCheck(object,subject):
    if object in possibleCmd2s[subject]:
        return True
    else:
        return False


# ----------------------------------- OUTPUT FUNCTIONS ----------------------------------- #


# PRINT ITEMS
def printItems():

    global locations, location

    if len(locations[location]["items"]) > 0: # if there are items

        print()

        printSequence("ITEMS:")
        
        for printItem in range(len(locations[location]["items"])): # for how many items there are

            time.sleep(0.25)

            printSequence(locations[location]["items"][printItem+1])  # print item
        
        time.sleep(0.5)

# PRINT DIRECTIONS
def printDirections():

    global locations, location

    printSequence("EXITS:")

    if "north" in locations[location]["exits"]: # print north if available
        
        printSequenceNNL("North - ")
        printSequence(locations[locations[location]["exits"]["north"]]["name"])

        time.sleep(0.25)

    if "south" in locations[location]["exits"]: # print south if available

        printSequenceNNL("South - ")
        printSequence(locations[locations[location]["exits"]["south"]]["name"])

        time.sleep(0.25)

    if "east" in locations[location]["exits"]: # print east if available

        printSequenceNNL("East - ")
        printSequence(locations[locations[location]["exits"]["east"]]["name"])

        time.sleep(0.25)

    if "west" in locations[location]["exits"]: # print west if available

        printSequenceNNL("West - ")
        printSequence(locations[locations[location]["exits"]["west"]]["name"])

        time.sleep(0.25)

    time.sleep(0.5)

# PRINT PEOPLE
def printPeople():

    global locations, location

    if len(locations[location]["people"]) > 0:

        print()

        printSequence("INTERACTIBLE:")

        time.sleep(0.5)

        printSequence(locations[location]["people"][1]) # prints the person

        time.sleep(0.5)

# PRINT INVENTORY
def printInventory():

    print()

    printSequenceNNL("Your inventory: ")

    if len(inventory) > 0:
        for prtInv in range(len(inventory)): # for how many items in inventory
            if prtInv != len(inventory): # if not the last item
                printSequenceNNL(inventory[prtInv]) # print item w/o new line
                print(end=" ")
            else: # if last item
                printSequence(inventory[prtInv]) # print w new line
    else:
        printSequence("Nothing")
    print()


# ----------------------------------- LOCATIONS ----------------------------------- #


locations = {}

# LABORATORY
locations["laboratory"] = {

    "name": "Laboratory",
    "desc": "A complicated and science-y looking lab stands before you.",
    "exits": {
        "north": "code room",
        "west": "break room",
        "south": "machine room"
    },
    "items":{

    },
    "people":{


    },
    "requirement": True

}

# CODE ROOM
locations["code room"] = { 

    "name": "Code room",
    "desc": "A room with technology out of your reach surrounds you.",
    "exits": {
        "south": "laboratory"
    },

    "items": {
        1:"codes",
    },
    "people": {

    },
    "requirement": True

}

# BREAK ROOM
locations["break room"] = {

    "name": "Break room",
    "desc": "You see a group of fellow scientists chatting over coffee.",
    "exits": {
        "east": "laboratory"
    },

    "items": {
        1:"coffee"
    },

    "people": {
        1: "scientists"
    },
    "requirement": True

}

# MACHINE ROOM
locations["machine room"] = {
    
    "name": "Machine room",
    "desc": "The intimidating machine stands before you. This is the culmination of years of scietific effort.",
    "exits": { 
        "north": "laboratory",
        "south": "time machine"
    },
    "items":{

    },

    "people": {
        1: "code machine"
    },
    "requirement": True

}

# TIME MACHINE
locations["time machine"] = {

    "name": "Time machine",
    "desc": "You are inside the machine. Infinite possibilities await.",
    "exits": {
        "north": "machine room",
        "south": "victorian times",
        "east": "future",
        "west": "stone age"
    },
    "items":{

    },
    "people":{

    },
    "requirement": False,
    "requiredItem": "the Codes."

}

# VICTORIAN TIMES
locations["victorian times"] = {

    "name": "Victoran times",
    "desc": "The smell of old air surrounds you as you see the royal castle towers over you. ",
    "exits": {
        "north": "time machine"
    },

    "items": {

    },

    "people": {
        1: "queen victoria"
    },
    "requirement": True

}

# STONE AGE
locations["stone age"] = {

    "name": "Stone age",
    "desc": "You marvel at the nature of prehistoric plants and ancient animals. Some primitive humans approach you.",
    "exits": {
        "east": "time machine"
    },

    "items": {
        1:"dino bone"
    },
    "people": {
        1:"cave people"
    },
    "requirement": False,
    "requiredItem": "to upgrade the machine."

}

# FUTURE
locations["future"] = {

    "name": "Future",
    "desc": "This is the future of humanity. lizard people walk about, flying cars soar through the skies.",
    "exits": {
        "west": "time machine"
    },

    "items": {

    },

    "people": {
        1: "lizard people" 
    },
    "requirement": False,
    "requiredItem": "to upgrade the time machine."

}


# ----------------------------------- ITEM USES ----------------------------------- #


def useCodes():

    global haveCodes, machineActivated

    if len(locations[location]["people"]) != 0:


        if locations[location]["people"][1] == "code machine":

            if not haveCodes:

                printSequence("Code machine: *BEEP* PLEASE INPUT CORRECT CODE.")

            if haveCodes:

                printSequence("Code machine: ACCESS GRANTED. YOU MAY NOW ENTER THE MACHINE.")
                locations["time machine"]["requirement"] = True

                machineActivated = True

                inventory.remove("codes")

        else:
            printSequence("You can't use this here.")

    else:
        printSequence("You can't use this here.")


def useCoffee():

    global location

    if location == "victorian times" and talkedToVictorians:
        printSequence("Queen Victoria: What could this be? Shall it solve my problem?")
        time.sleep(0.5)
        printSequence("You: Yes, it'll energise you right up.")
        time.sleep(0.5)
        printSequence("Queen Victoria: Oh! Yes, this is amazing! You shall be rewarded!")
        time.sleep(0.5)
        printSequence("Queen Victoria gave you the Crown Jewels.")
        inventory.append("crown jewels")
        inventory.remove("coffee")
        time.sleep(0.5)
        printSequence("You: I thank you greatly. This will aid humanity infinitely.")
    else:
        printSequence("You're not thirsty right now.") 


# ----------------------------------- DIALOGUE ----------------------------------- #


# SCIENTIST DIALOGUE
def scientistDiag():

    global talkedToScientists, haveQK, upgradedMachine

    print()

    #----------no QK----------#
    if not haveQK:

        #----------no jewels----------#
        if not haveJewels:

            #----------not talked----------#
            if not talkedToScientists:
            
                printSequence("Scientist: Hello, new scientist! Are you ready to test the machine?")

            #----------talked----------#
            else:

                printSequence("Are you ready to test the machine?")

            time.sleep(0.5)

            choice = input("Are you ready? Y or N > ")

            #----------not ready----------#
            if choice == "N":

                printSequence("You: Not quite, I'm just grabbing coffee.")
                if "coffee" not in inventory: # if player doesnt have coffee 
                    inventory.append("coffee") # give player coffee
                    del locations["break room"]["items"][1] # delete coffee from break room
                    talkedToScientists = True

            #----------ready----------#
            elif choice == "Y":

                printSequence("You: Yes, I'm just about to. I just need the codes.")

                time.sleep(0.5)

                printSequence("Scientist: Well, it's just in the code room. Too bad we don't have any gold or diamonds to upgrade it.")

                talkedToScientists = True

        #----------jewels + not upgraded----------#
        elif haveJewels and not upgradedMachine:

            printSequence("Scientist: Hey, you got... the Crown Jewels?? That's exactly what we need to upgrade the machine! We'll get to work ASAP.")

            inventory.remove("crown jewels")

            time.sleep(0.5)

            printSequence("The scientists get hard at work upgrading the machine...")

            time.sleep(1)

            printSequence("Scientist: Done! Sorry it took so long. You should be able to travel the the stone age and the future now.")

            time.sleep(0.5)

            printSequence("Scientist: Now, we will probably need to get a very, very old biological sample to create the Universal Translator. A fossil will do, if you can find one. Good luck again!")

            locations["stone age"]["requirement"] = True

            locations["future"]["requirement"] = True

            upgradedMachine = True

        #----------jewels + upgraded----------#
        elif haveJewels and upgradedMachine and not haveBone:
            printSequence("Scientist: Go, scientist. ")

        #----------dino bone----------#
        elif haveBone and upgradedMachine and not haveQK:
            printSequence("Scientist: WOW! This is impressive! An entire dinosaur bone! This will be perfect for making the translator. Give us a minute.")

            inventory.remove("dino bone")

            time.sleep(0.25)

            printSequence("The scientists get to creating the universal translator...")

            time.sleep(1)

            printSequence("Scientist: Aaaaand done! I hope you can gain the knowledge of those in the future.")

            inventory.append("translator")

    #----------QK----------#
    elif haveQK:

        printSequence("YOU GOT THE KNOWLEDGE?! Please, enlighten us!")

        global gameRunning
        gameRunning = False
    print()

# LIZARD PERSON DIALOGUE
def lizardDiag():

    global haveTranslator, talkedToLizards

    print()

    if not talkedToLizards:

        if haveTranslator:

            printSequence("Lizard person: Greetings, and welcome to the future. would you like our divine Quantum Knowledge?")
            printSequence("You: I would, it will aid the present humans greatly.")
            printSequence("They told you the Quantum knowlede!")
            inventory.append("quantum knowledge")

            talkedToLizards = True

        else:

            printSequence("Lizard person: Glorp zeep glap, zorbee gib.")
            printSequence("You: I need a translator to understand them.")
    else:
        printSequence("Lizard person: Go. Use this knowledge to benefit your species.")

# CAVE PERSON DIALOGUE
def cavediag():
    global talkedToCaves
    print()
    if not talkedToCaves:

        printSequence("Cave person: UNGA BUNGA!! Who? You?")

        time.sleep(0.5)

        printSequence("You: I am from the future. ")

        time.sleep(0.5)

        printSequence("Cave person: (complete gibberish you cannot understand, pointing at a very large bone sitting on a pile of hay)")

        time.sleep(0.5)

        printSequence("You: Shall i take the bone? It will aid in the creation of the universal translator.")

        time.sleep(0.5)

        printSequence("You grab the bone. The cave people don't seem aggrivated, so you keep it.")

        time.sleep(0.5)

        inventory.append("dino bone")

        talkedToCaves = True

    else:
        printSequence("The cave people continue to stare at you.")

# VICTORIAN DIALOGUE
def victorianDiag():

    global talkedToVictorians
    
    print()

    if not talkedToVictorians:

        printSequence("Queen Victoria: And who might thou be? This is a remarkable scenario. Your contraption simply appeared out of nowhere!")

        time.sleep(0.5)

        printSequence("You: I am from the future. I am in need of materials from this era. Any kind of gold and diamond would be appreciated.")

        time.sleep(0.5)

        printSequence("Queen Victoria: Well, we have a considerable amount of valuable material here. The most valuable of which is my Crown Jewels here.")

        time.sleep(0.5)
        printSequence("Queen Victoria: I have a problem, though. I cannot move from here as i am simply too tired (and can't be bothered)!")

        time.sleep(0.5)

        printSequence("You: I see. I will try and find a way of energising you.")

        talkedToVictorians = True

    elif talkedToVictorians and "crown jewels" not in inventory and not upgradedMachine:

        printSequence("Queen Victoria: Oh, the horror! You must bring me some kind of energising material!")

    else:

        printSequence("Queen Victoria: Now go! Before i regret this!")



# CODE MACHINE INTERACT
def codeMachineInteract():

    global machineActivated

    if not machineActivated:

        printSequence("Code machine: *BEEP* PLEASE INPUT CORRECT CODE.")

    else:
        printSequence("Code machine: ACCESS GRANTED. YOU MAY NOW ENTER THE MACHINE.")
        
        locations["time machine"]["requirement"] = True


#----------------------------------- OPENING -----------------------------------#


printSequence("""Welcome to my game! To act, type the first word, being what action you want to do, e.g. "go", "take", "drop", "interact" etc.. The second and/or third words will dictate what you do that action to, e.g. "go laboratory" would have you go the the laboratory, or "interact scientists" will have you talk to the scientists. Good luck!""")
printSequenceNNL("""Press enter when you're ready > """)
#input()

#----------------------------------- GAME LOOP -----------------------------------#

while gameRunning: # while player is alive and game not completed


    if "codes" in inventory:
        haveCodes = True
    if "crown jewels" in inventory:
        haveJewels = True
    if "dino bone" in inventory:
        haveBone = True
    if "translator" in inventory:
        haveTranslator = True
    if "quantum knowledge" in inventory:
        haveQK = True


    cmdValid = False # command automatically not valid


    print()

    printSequenceNNL("You are in the ") # print current location
    printSequence(locations[location]["name"])

    time.sleep(0.25)

    printSequence(locations[location]["desc"]) # print description of location 

    time.sleep(0.25)

    print()

    printDirections() # print available locations from current

    printItems() # print items in location

    printPeople() # print people in location

    printInventory() # print player inventory



    while cmdValid != True:

        print()

        cmd = input("Command > ") # take input


        if len(cmd) > 0: # split command

            cmdinp1 = (cmd.split())[0] # cmdinp1 is 1st word

            if len(cmd.split()) > 2: # if more than 2 words
                cmdinp2 = cmd.split()[1]+" "+(cmd.split())[2] # cmdinp2 is 2nd and 3rd words

            elif len(cmd.split()) == 2: # if 2 words
                cmdinp2 = (cmd.split())[1] # cmdinp2 is 2nd word
        

        if cmdinp1 == "go": # if player wants to go somewhere

            for directionCheck in directions: # check N, E, S, W for available locations
                if objectCheck(cmdinp2,"places"):

                    if (directionCheck in locations[location]["exits"]) and (locations[cmdinp2]["requirement"] == True): # if that direction is there and is accessible

                        if cmdinp2 in locations[location]["exits"][directionCheck]: # if that room is there

                            location = cmdinp2 # change locations
                            cmdValid = True # valid command, do not ask again

                    elif (directionCheck in locations[location]["exits"]) and (locations[cmdinp2]["requirement"] != True): # if direction is adjacent but inaccessible
                        printSequenceNNL("You cannot access this area yet. You need ")
                        printSequence(locations[cmdinp2]["requiredItem"])
                        break # break out of N E S W loop


        elif cmdinp1 == "take": # if player wants to take an item

            for delItemCount in range(len(locations[location]["items"])): # check every item in that location

                if objectCheck(cmdinp2,"items"):

                    if locations[location]["items"][delItemCount+1] == cmdinp2: # check if that item is the one the player wants

                        print()

                        printSequenceNNL("You took the ")
                        printSequence(cmdinp2)

                        inventory.append(cmdinp2) # add item to inventory

                        print()

                        del locations[location]["items"][delItemCount+1] # delete item from location

                        printItems() # print items in location

                        cmdVaid = True # valid command, do not ask again


        elif cmdinp1 == "drop": # if player wants to drop something

            if objectCheck(cmdinp2,"items"):

                if cmdinp2 in inventory: # if item is in inventory

                    print()

                    printSequenceNNL("You dropped the")
                    printSequence(cmdinp2) 

                    inventory.remove(cmdinp2) # remove item from inventory

                    locations[location]["items"][len(locations[location]["items"])+1] = cmdinp2 # next item in the area is the item the player dropped

                    printItems() # print items in location

                    print()

                    cmdVaid = True # valid command, do not ask again


        elif cmdinp1 == "interact": # if player wants to interact/talk

            if objectCheck(cmdinp2,"interactibles"):

                if len(locations[location]["people"]) > 0: # if there are people in location

                    if locations[location]["people"][1] == cmdinp2: # if person is in location

                        if cmdinp2 == "scientists":
                            scientistDiag() # talk to scientists

                        elif cmdinp2 == "lizard people":
                            lizardDiag() # talk to lizard people

                        elif cmdinp2 == "cave people":
                            cavediag() # talk to cave people

                        elif cmdinp2 == "queen victoria":
                            victorianDiag() # talk to victorian
                            
                        elif cmdinp2 == "code machine":
                            codeMachineInteract()

                        cmdValid = True # valid command, do not ask again


        elif cmdinp1 == "use": # if player wants to use an item

            if cmdinp2 == "codes":
                useCodes()

            elif cmdinp2 == "coffee":
                useCoffee()

            cmdValid = True # valid command, do not ask again


# ----------------------------------- AFTER GAME END ----------------------------------- #

print()
print()
print()
printSequence("CONGRATULATIONS! YOU SIGNIFICANTLY ADVANCED MODERN SCIENCE!") 
printSequence("thamks for playing my game, bye")

