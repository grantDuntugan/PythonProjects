import random

#Hangman!

#ADD MORE WORDS IN THIS ARRAY vvv
words = ["sphynx", "hello"]
#THIS ARRAY ^^^

playing = 1
guessing = 1

def wordBuilder(s1, s2, char):
    s1list = list(s1)
    s2list = list(s2)

    for x in range(0, len(s1)):
        if char == s1list[x]:
            s2list[x] = char
    return "".join(s2list)

while playing == 1:
    guessedChars = []
    wordToGuess = words[random.randint(0, len(words)-1)]
    hiddenWord = ""
    hiddenWord = hiddenWord.ljust(len(wordToGuess), "X")
    attempts = 5
    
    print("A word has been selected!")
    guessing = 1

    while guessing == 1:
    
        charGuessed = input("Pick a character!\n")
        if len(charGuessed) != 1:
            print("Input one letter only!")
            continue

        charPosition = wordToGuess.find(charGuessed)

        if charGuessed in guessedChars:
            print("You already guessed that!")
            print(hiddenWord)

        elif charPosition != -1:
            guessedChars.append(charGuessed)
            print(charGuessed, "is in the word.")
            hiddenWord = wordBuilder(wordToGuess, hiddenWord, charGuessed)
            print(hiddenWord)
            

            if hiddenWord.find("X") == -1:
                print("Congrats! You guessed the word!")
                guessing = 0
                answer = input("Play again? Y/N\n")
                if answer != "Y" and answer != "y":
                    playing = 0
                    break
        elif charPosition == -1:
            guessedChars.append(charGuessed)
            attempts -= 1
            if attempts <= 0:
                print("You couldn't guess the word! Game Over.")
                guessing = 0
                answer = input("Play again? Y/N\n")
                if answer != "Y" and answer != "y":
                    playing = 0
                    break
            else:
                print("Nope! You have", attempts, "attempts left!")
                print(hiddenWord)
        
        
