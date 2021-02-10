import random

#Number Guessing Game!
#Guess the random number that the program outputs!
#Mode 1: 1-10
#   Guess a number from 1-10.
#   Hints provided: Higher or Lower
#
#Mode 2: 1-100
#   Guess a number from 1-100.
#   Hints provided: Higher or Lower if within 10
#   Wrong Half if in wrong half of 100
#   Wrong Quarter if in right half, but wrong quarter of 100
#
#Try and get the right number in the least number of guesses!

#The number of guesses
numGuesses = 0;

#Game state
playing = 1;

#This function handles the "Play again?" question
def playAgain(response):
    if response == "Y" or response == "y":
        return 1
    else:
        return 0

while playing == 1:
    gameMode = int(input("What interval do you want? '1' for 1-10 and '2' for 1-100.\n"))

    #Gamemode checks
    if (gameMode == 1):
        #generate random number
        numToGuess = random.randint(1, 10)
        userGuess = 0
        while numToGuess != userGuess:
            #take the guess
            userGuess = int(input("Guess a number 1-10!\n"))
            numGuesses += 1

            if userGuess == numToGuess:
                print("You got it! It took", numGuesses, "guesses!\n")

                numGuesses = 0
                
                playing = playAgain(input("Play again? Y/N\n"))
            elif userGuess < numToGuess:
                print("Higher!")
            else:
                print("Lower!")

    elif (gameMode == 2):
        numToGuess = random.randint(1,100)
        userGuess = 0

        while numToGuess != userGuess:
            userGuess = int(input("Guess a number 1-100!\n"))
            numGuesses += 1

            if userGuess == numToGuess:
                print("You got it! It took", numGuesses, "guesses!\n")

                numGuesses = 0
                playing = playAgain(input("Play again? Y/N\n"))

            elif (userGuess < 50 and numToGuess >= 50) or (userGuess >= 50 and numToGuess < 50):
                print("Wrong half!\n")
                continue
            elif (userGuess < 25 and numToGuess >= 25) or (userGuess >= 25 and numToGuess < 25):
                print("Wrong quarter!\n")
                continue
            elif (userGuess < 75 and numToGuess >= 75) or (userGuess >= 75 and numToGuess < 75):
                print("Wrong quarter!\n")
                continue
            elif (userGuess < numToGuess):
                print("Higher!\n")
            else:
                print("Lower!\n")
        
    else:
        playing = playAgain(input("Couldn't read input. Try again? Y/N"))
    
    
