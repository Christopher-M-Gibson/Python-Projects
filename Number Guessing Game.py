#
# Christopher Gibson (christopher.mitchell.gibson@gmail.com)
# Guess the Number Game
# March 29, 2022
#

# Import random function
from random import randint

# Define the Play() function
def Play():

    # Describe the instructions of the game
    print("To play this game, the player will be asked to input an integer ranging from 1 to 100", "\n"
          " that they believe matches the randomized integer of the same range that the program", "\n"
          " generated. The program will then inform the user of whether their guess is too high,", "\n"
          " too low, or correct. The user will then guess again if their choice is incorrect. This", "\n"
          " repeats until the user guesses the correct number, where they then will be asked to either", "\n"
          " play again or exit the program.")
    print()

    # Determine random number
    number = randint(1, 100)

    # Initialize Guess
    Guess = 0
    NumGuess = 0
    
    # While the guess is not equal to the randomly generated number:
    while Guess != number:

        # Ask the user to guess a number through a try-except statement
        try:
            Guess = int(input("Please guess an integer value (1-100 only): "))
            print()
            Guess = int(Guess)
        except:
            print(" Error. Please try again.")
            print()

        # If the guess is less than the number,
        if Guess < number:

            # Tell user the number is too low, and to try again
            Result1 = "Your choice, " + str(Guess) + ", is too low. Try again."
            print(Result1)
            print()

            # Add 1 to NumGuess
            NumGuess += 1

        # If the guess is greater than the number,
        elif Guess > number:

            # Tell user the number is too high, and to try again
            Result2 = "Your choice, " + str(Guess) + ", is too high. Try again."
            print(Result2)
            print()

            # Add 1 to NumGuess
            NumGuess += 1

        # If the number is exact,
        elif Guess == number:

            # Craft Result3 statement
            Result3 = "Your choice, " + str(Guess) + ", is correct! Congratulations!"
            NumGuess += 1

            # Craft Result4 Statement
            if NumGuess == 1:
                Result4 = "It took you " + str(NumGuess) + " try to guess the correct number."
            else:
                Result4 = "It took you " + str(NumGuess) + " tries to guess the correct number."

            # End the program
            print(Result3)
            print(Result4)
            print()
    
# Define the main function
def main():

    # Describe the functionality of the program
    print("This program will allow the user to play a number guessing game. To play the game, type PLAY. To", "\n"
          " quit the game and end the program, type QUIT.")
    print()

    # Initialize Input
    Input = ""

    # while user has not typed QUIT:
    while Input != "QUIT":

        # Ask the user for the input
        Input = input("Do you want to play the game (PLAY) or quit (QUIT)? ")
        print()

        # If the user inputted PLAY, call the Play() function
        if Input == "PLAY":
            Play()
        
        # If the user inputted QUIT, end the main function
        elif Input == "QUIT":
            print("Goodbye!")

        # If the user inputted anything else, print out an error message
        else:
            print(" Error. Please type either PLAY or QUIT.")
            print()

# End the main function
main()
