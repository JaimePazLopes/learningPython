# Let's use while loops to create a guessing game.
# The Challenge:
#Write a program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
#    If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
#    On a player's first turn, if their guess is
#        within 10 of the number, return "WARM!"
#        further than 10 away from the number, return "COLD!"
#    On all subsequent turns, if a guess is
#        closer to the number than the previous guess return "WARMER!"
#        farther from the number than the previous guess, return "COLDER!"
#    When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
# You can try this from scratch, or follow the steps outlined below. A separate Solution notebook has been provided.
# Good luck!

from random import randint


def gameLoop():
    startInt = 1
    endInt = 100
    randomInt = randint(startInt, endInt)
    numberOfTries = 0
    bestGuessRange = 100
    gotCloser = False
    print("What is the number I am thinking?")
    while True:
        stringInput = input()
        if not stringInput.isdecimal():
            print("NUMBERRRR!!! TYPE A NUMBER!!!!! Try again, loser...")
            continue
        guessingNumber = int(stringInput)
        numberOfTries += 1
        if guessingNumber < startInt or guessingNumber > endInt:
            print("Are you stupid?!?!? I said numbers between 1 and 100!!! Try again...")
            continue
        if guessingNumber == randomInt:
            print("OMG!!! You got it!! Do you have some kind of magic power? Can you read my mind?")
            print(f"And you took only {numberOfTries} tries!! I though you would need 3 times more!!")
            break;
        else:
            tempGuess = abs(guessingNumber - randomInt)
            if bestGuessRange > tempGuess:
                bestGuessRange = tempGuess
                if gotCloser:
                    print("YES! You are getting really close!!")
                elif bestGuessRange <= 10:
                    gotCloser = True
                    print("WOW! OK, OK!! Keep going, you are almost there.")
            elif gotCloser:
                print("What are you doing!?! Why are you guessing so far!?!")

            if not gotCloser:
                print("WRONG!! WRONG!! WRONG!!")

    playAgain()

def playAgain():
    print("Do you want to play with me again?!?!?! Type Y for yes and N for no")
    playAgain = False
    while True:
        again = input()
        if again.upper() == "Y":
            print("MWAA HAA HAA!! Let's go again!!")
            playAgain = True
            break
        if again.upper() == "N":
            print("WHATTT!?!?!?! WHY!?!?!?! Am I not fun enough for you!?!?! \nYou are so boring... I will go away, I don't want to play with you anymore...")
            break
    if playAgain:
        gameLoop()
    else:
        input()


print("Welcome to the Fantabulous Guessing Game!!")
print("I will think in a number from 1 to 100 and you will have to guess. It will be a lot of FUNNN!!")
print("Let's start!!")
gameLoop()




