import random
#HangMan: track attempts, check userGuess against guessWord, & limit 10 tries.
MAXTRIES = 10
userGuess=[]
wrong = []
runGame = True
tries = 0
#Assign line number, grab word at line number..
lineNum = random.randint(1,113908)
fin = open("words.txt")
for i in range(lineNum):
    guessWord = fin.readline().strip()
#Populate output text fields..
for c in guessWord:
    userGuess.append('_')
for i in range(MAXTRIES):
    wrong.append(' ')
while tries < MAXTRIES and runGame == True:
    validGuess = False
    validInput = False
    #print our current progress on guessing..
    print("".join(userGuess))
    #print out our wrong guesses..
    print("Wrong guesses :", "".join(wrong), "\n")
    #Grab one, nonwhitespace character..
    while validInput == False:
        guessChar= input("Guess a letter :")
        guessChar= ''.join(guessChar.split())
        if len(guessChar) == 1:
            validInput = True
    #If letter already guessed, no penalty, enter a different one..
    if guessChar in wrong:
        print("That letter has already been guessed!")
    else:
        #parse and replace '_' with correct letter guessed at appropriate indices...
        for i in range(len(guessWord)):
            if guessWord[i] == guessChar:
                userGuess[i] = guessChar
                validGuess = True
        # If not found, penalize! Replace ' ' at indexed attempt
        if not validGuess and tries < MAXTRIES:
            wrong[tries] = guessChar
            tries +=1
    #Fare ye well, Man.
    if(tries == MAXTRIES):
        print("Better luck next time! The word was:", guessWord)
    #The Jury Pardons him.
    if ("".join(userGuess) == "".join(guessWord)):
        print("Congrats! You guessed it!", guessWord)
        runGame = False
