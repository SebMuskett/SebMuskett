letterdetec = ""
count = 0
guesses = 0
guess = ["_"]
realWord = input("what word? ")
word = list(realWord)

for i in range(len(word)-1):
    guess.append("_") # create approprite guess array

for b in range(50):
    print("")
#--------------------------------------------------------

while guess != word and guesses < 10: # repeat until win

    letterGuess = str(input("Guess a letter: "))

    if letterGuess in word: # correct check
        print("correct")
        count = 0 # start index 0

        for count in range(len(word)): # repeat for length of word
            letterdetec = word[count] 

            if guess[count] == "_": # check all that are blank
                if letterdetec == letterGuess:
                    guess[count] = letterGuess # if correct, add to guess
                    
            count = int(count) + 1 # next index
        print(guess)

    else:
        print("incorrect") # incorrect guess
        guesses = guesses + 1
        print("guesses remaining:",10-guesses) # guesses remaining

if guesses < 10:
    print("u win!!!") # win
else:
    print("u lose :(") # lose

