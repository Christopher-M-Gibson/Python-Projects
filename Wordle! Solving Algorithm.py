#
# Christopher Gibson (christopher.mitchell.gibson@gmail.com)
# Wordle! Solving Algorithm
# May 14, 2022
#

# Import random library
from random import *

# Define the Download() function, which accepts no parameters
def Download():

    # Open and read the 5-Letter-Words.txt file
    file = "5-Letter-Words.txt"
    infile = open(file, "r", encoding = 'utf8')

    # Initialize the list of words
    WordList = []

    # Read the first line of the file
    line = infile.readline()

    # Use a while loop to fill in the list, where each entry is a word
    while line != "":

        # Remove the newline character from each line
        line = line.replace("\n", "")

        # Capitalize every word
        line = line.upper()

        # Append the line to the list
        WordList.append(line)

        # Read the next line of the file
        line = infile.readline()
    
    # Close the file
    infile.close()
    
    # return the list of words
    return WordList

# Define the CheckValidity() function, which accepts two parameters
def CheckValidity(Guess, WordList):

    # If the guess is in the WordList
    if Guess.upper() in WordList:

        # Print a blank line and set value of Valid
        print()
        Valid = "YES"

    # If the guess is not in WordList
    else:

        # Tell the user to try again and set value of Valid
        print(" Error. Check to see if the word was entered correctly.")
        print()
        Valid = "NO"

    # Return the value for Valid
    return Valid

# Define the CheckCorrectness() function, which accepts a parameter
def CheckCorrectness(Correct):

    # If the user responded YES
    if Correct == "YES":

        # Congratulate the user and update value of Correct
        CheckedCorrect = "YES"
        print()

    # If the user responsed NO
    elif Correct == "NO":

        # Update the value of CheckedCorrect
        CheckedCorrect = "NO"
        print()

    # If the user responded with something else:
    else:
        
        # Print an Error
        CheckedCorrect = "ERR"
        print(" Error. Please type either YES or NO.")
        print()

    # Return the value for CheckedCorrect
    return CheckedCorrect
        
# Define the CheckFeedback() function, which accepts one parameter
def CheckFeedback(Feedback):

    # Initialize CheckedFeedback and Check_No_Count
    CheckedFeedback = ""
    Check_No_Count = 0

    # Check whether the feedback string is 5 characters long
    if len(Feedback) != 5:

        # Set CheckedFeedback = NO and return it
        CheckedFeedback = "NO"
        return CheckedFeedback
    
    # Split the feedback into a list, where each character is an element
    FeedbackList = list(Feedback)

    # Use a for loop to check whether each element of the list is one of the three acceptable characters
    for i in range(0,5):

        # If the character is not an acceptable character,
        if (FeedbackList[i] != "-") and (FeedbackList[i] != "Y") and (FeedbackList[i] != "G"):

            # Add one to Check_No_Count
            Check_No_Count += 1

    # Depending on the value of Check_No_Count, set the value of CheckedFeedback
    if Check_No_Count > 0:
        CheckedFeedback = "NO"
    else:
        CheckedFeedback = "YES"

    # Return the value of CheckedFeedback
    return CheckedFeedback

# Define the Optimize() function, which accepts one parameter
def Optimize(PossGuess):

    # Initialize an empty dictionary
    LetterCount = {}
    
    # Set up a for loop that will go through each word in the list
    for word in PossGuess:

        # Split the word into a string, where each character is a element
        WordSpl = list(word)

        # Use a for loop that loops through all the characters in the word
        for i in range(0,5):

            # Set the value of dict.keys()
            keys = LetterCount.keys()

            # Use an if-else statement to keep the count of the characters
            if WordSpl[i] in keys:
                LetterCount[WordSpl[i]] += 1
            else:
                LetterCount[WordSpl[i]] = 1

    # Initialize an empty dictionary of the form Word : Total
    OptimalWord = {}

    # Set up a for loop that will go through the list of words again
    for word in PossGuess:

        # Split the word into a list, where each character is a element
        WordSpl = list(word)

        # Turn the list to string to remove duplicates, then back into a list
        WordSpl = set(WordSpl)
        WordSpl = list(WordSpl)
        
        # Initialze the total of the value of the frequency of characters in the word
        WordTotal = 0
        
        # Use a for loop that loops through all the characters in the word
        for i in range(0,len(WordSpl)):

            # Add the value of the character to the total
            WordTotal += LetterCount[WordSpl[i]]

        # Set the entry in the dictionary to be of the form Word : Total
        OptimalWord[word] = WordTotal

    # Sort the dictionary so the first entry is the word with the highest total value
    OptimalWord = sorted(OptimalWord.items(), key =
           lambda kv:(kv[1], kv[0]), reverse = True)

    # Let the first element of the dictionary be the optimal word to choose
    RecommendedWord = OptimalWord[0][0]
    
    # Return RecommendedWord
    return RecommendedWord

# Define the Solve function, which accepts zero parameters
def Solve(WordList):

    # Print out the instructions of the program
    print("=" * 120)
    print("Welcome to the Wordle Solving Algorithm. For each attempt, the algorithm will have you putin a word that you guessed", "\n"
          " in the Wordle!.py file. It will then ask whether the word was correct or not. If so, the algorithm will end. Otherwise,", "\n"
          " the program will ask the feedback Wordle gave. Using this, it will determine an optimal guess for the next attempt.")
    print()

    # Make a copy of the word list, which will be the list of possible guesses
    PossGuess = WordList.copy()
    
    # Set up a for loop that will go through each of the six attempts
    for i in range(0,6):
            
        # Print out the attempt number
        print("Attempt #" + str(i+1))
        print()

        #Initialize Valid and CheckedCorrect
        Valid = ""
        CheckedCorrect = ""
        CheckedFeedback = ""

        # Set up a for loop that ends once the word was deemed valid
        while Valid != "YES":

            # Recommend the best word for the user to select
            RecommendedWord = Optimize(PossGuess)

            # Print out a statement telling the user how many possible words remain
            print("     There are " + str(len(PossGuess)) + " possible choices for the true word.")
            print()
            # Print a statement recommended the best word to the user
            print("     We suggest trying the word " + RecommendedWord + " as a guess.")
            print()
            
            # Ask the user for the Guess that they inputted
            Guess = input("     What word did you guess? ")
        
            # Check whether the Guess was a valid guess using  CheckValidity() function
            Valid = CheckValidity(Guess, WordList)

        # Set up a while loop that ends once the guess was properly checked
        while (CheckedCorrect != "YES") and (CheckedCorrect != "NO"):
            
            # Ask the user whether the guess was correct
            Correct = input("     Was your guess correct? (YES) or (NO) ")

            # Check whether Correct is a valid response using the CheckCorrectness() function
            CheckedCorrect = CheckCorrectness(Correct)
            
        # If the guess was correct,
        if CheckedCorrect == "YES":

            # Congratulate the user
            print("     Congratulations! I hope the algorithm helped!")
            print("=" * 120)
            print()
            return

        # If the guess was wrong,
        elif CheckedCorrect == "NO":

            # Tell the user what what they need to do next
            print("     Please enter the feedback that was provided upon entering the word.")
            print("          If the letter was green, type 'G'")
            print("          If the letter was yellow, type 'Y'")
            print("          If the letter was grey, type '-'")
            print("     As to how to type it, if the word was WATER, and you guessed TIRES,", "\n"
                  "     you would type 'Y-YG-' (minus the quotation marks)")
            print()

            # Set up a while loop that ends once the feedback was checked
            while CheckedFeedback != "YES":
                
                # Tell the user to enter the feedback
                Feedback = input("     Please type in the feedback provided by Wordle: ")
                print()

                # Check whether the feedback provided was valid
                CheckedFeedback = CheckFeedback(Feedback)

                # If the value of CheckedFeedback was "NO",
                if CheckedFeedback == "NO":

                    # Print an error, tell the user to try again
                    print(" Error. Please ensure the Feedback is of an acceptable form.")
                    print()

            # Split the Feedback and the guess into a list, where each character is an element
            NewGuess = list(Guess.upper())
            NewFeed = list(Feedback)

            # Set the list of words to be a tuple
            GuessTuple = tuple(PossGuess)
            
            # Use a for loop to run through the list of WordList as a tuple
            for word in GuessTuple:
                
                # Use a for loop to run through each element of the word
                for i in range(0,5):

                    # If the letter is grey and is found in the word,
                    if (NewFeed[i] == "-") and (NewGuess[i] in word):

                        # Remove the word from the list of possible guesses
                        PossGuess.remove(word)
                        break

                    # If the letter is green and not in the same index,
                    elif (NewFeed[i] == "G") and (NewGuess[i] != word[i]):

                        # Remove the word from the list of possible guesses
                        PossGuess.remove(word)
                        break

                    # If the letter is yellow and is not found in the word,
                    elif (NewFeed[i] == "Y") and (NewGuess[i] not in word):

                        # Remove the word from the list of possible guesses
                        PossGuess.remove(word)
                        break

                    # If the letter is yellow and in the same index,
                    elif (NewFeed[i] == "Y") and (NewGuess[i] == word[i]):

                        # Remove the word from the list of possible guesses
                        PossGuess.remove(word)
                        break

        # if PossGuess is empty, print a statement for the user informing them the program failed
        if len(PossGuess) == 0:
            print(" Due to a technical error, the program cannot aid you for this Wordle.", "\n"
                  " You are on your own for this Wordle. We hope the algortihm can be of", "\n"
                  " assistance next time.")
            print()
            return
                        
# Define the main() function
def main():

    # Download the word list
    WordList = Download()

    # Describe the functionality of the program
    print("This program is a solving algorithm for Wordle, and is best used alongside the 'Wordle!.py' file created earlier.")
    print()
    # Initialize Input
    Input = ""
    
    # While the user has not typed "QUIT":
    while Input != "QUIT":

        # Ask the user for the input
        Input = input("Do you want to use the solving algorithm (YES) or quit (QUIT)? ")
        print()

        # If the user inputted YES, call the Solve() function
        if Input == "YES":
            Solve(WordList)

        # If the user inputted QUIT, end the main function
        elif Input == "QUIT":
            print("Goodbye!")

        # If th euser inputted anything else, print out an error message
        else:
            print(" Error. Please type either YES or QUIT.")
            print()

# End the main function
main()
