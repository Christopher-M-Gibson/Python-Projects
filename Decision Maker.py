"""
Skills used: Libraries, Functions, While Loops, Try-Except Statements,
             For Loops, Variables
"""

# Import random library
import random

def main():

    # Instructions 
    print("This program is a decision maker. It will first ask about the", "\n"
          " question/issue you are deciding upon, and then ask how many", "\n"
          " choices there are, followed by what each choice is.", "\n"
          " After, the program will make a decision and present it.")
    print()

    # Have the user input their question
    Question = input("What question/issue are you looking for a choice on? ")
    print()

    # Ask the user how many choices there will be
    ChoiceNum = ''
    while type(ChoiceNum) != int:
        try:
            ChoiceNum = int(input("How many choices? (Numbers only): "))
            ChoiceNum = int(ChoiceNum)
        except:
            print(" Error. Please try again.")
            print()

    # Have the user enter the choices
    Choices = []
    for i in range(0, ChoiceNum):
        Response = ""
        Response = input("Please enter option "+str(i+1)+" : ")
        Choices.append(Response)
        
    # Give the decision to the user
    Decision = random.choice(Choices)
    print()
    print("==================================================================")
    print("For your question/ issue: " + Question + ",")
    print("After careful consideration, the program chooses: ")
    print(Decision)

main()
