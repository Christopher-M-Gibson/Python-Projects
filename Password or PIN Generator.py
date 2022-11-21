"""
Skills used:
    Functions, Libraries, While Loops, Try-Except Statements,
    If-Elif-Else Statements, For Loops, Inputs, Lists 
"""


# Import random library
from random import *

# PASSWORD() function, which creates the password
def PASSWORD():

    # Initialize character banks, answers, and give instructions
    CharBank = []
    LetterBank = []
    NumBank = []
    SpecBank = []
    Cap = ""
    Num = ""
    Spec = ""
    Length = ""
    print("You have chosen to create a PASSWORD.")
    print("For each of the following questions, answer YES or NO")
    print()
    
    # While loop for 1st question given to the user
    while Cap != "YES" and Cap != "NO":
        Cap = input("Does your password require at least one Uppercase letter and Lowercase Letter? ")
        Cap = Cap.upper()
        print()
        if Cap == "YES":
            for i in range(65, 91):
                CharBank.append(chr(i))
                LetterBank.append(chr(i))
            for i in range(97, 123):
                CharBank.append(chr(i))
                LetterBank.append(chr(i))
            break
        elif Cap == "NO":
            for i in range(65, 91):
                CharBank.append(chr(i))
                LetterBank.append(chr(i))
            break
        else:
            print(" Error. Please type YES or NO")
            print()

    # While loop for 2nd question given to the user
    while Num != "YES" and Num != "NO":
        Num = input("Does your password require at least one number? ")
        Num = Num.upper()
        print()
        if Num == "YES":
            for i in range(0, 10):
                CharBank.append(str(i))
                NumBank.append(str(i))
            break
        elif Num == "NO":
            break
        else:
            print(" Error. Please type YES or NO")
            print()
            
    # While loop for 3rd question given to the user 
    while Spec != "YES" and Spec != "NO":
        Spec = input("Does your password require at least one special character? ")
        Spec = Spec.upper()
        print()
        if Spec == "YES":
            for i in range(33, 47):
                CharBank.append(chr(i))
                SpecBank.append(chr(i))
            for i in range(58, 65):
                CharBank.append(chr(i))
                SpecBank.append(chr(i))
            for i in range(93, 96):
                CharBank.append(chr(i))
                SpecBank.append(chr(i))
            CharBank.append(chr(123))
            SpecBank.append(chr(123))
            CharBank.append(chr(125))
            SpecBank.append(chr(125))
            CharBank.append(chr(126))
            SpecBank.append(chr(126))
            CharBank.append(chr(91))
            SpecBank.append(chr(91))
            break
        elif Spec == "NO":
            break
        else:
            print(" Error. Please type YES or NO")
            print()

    # While loop for the 4th question given to the user
    while type(Length) != int:
        try:
            Length = int(input("Type PASSWORD length (between 8-32 char. only): "))
            print()
            Length = int(Length)
        except:
            print(" Error. Please try again.")
            print()

    # Create the password
    Password = []
    for i in range(0, Length):
        Password.append("A")
    if Cap == "YES":
        Password[0] = LetterBank[randint(0, 27)] 
        Password[1] = LetterBank[randint(27, 53)]
    elif Cap == "NO":
        Password[0] = LetterBank[randint(0, 27)]
        Password[1] = LetterBank[randint(0, 27)]
    if Num == "YES":
        Password[2] = NumBank[randint(0, len(NumBank)-1)]
    elif Num == "NO":
        Password[2] = LetterBank[randint(0, 27)]
    if Spec == "YES":
        Password[3] = SpecBank[randint(0, len(SpecBank)-1)]
    if Spec == "NO":
        Password[3] = LetterBank[randint(0, 27)]
    for i in range(4, Length-1):
        Password[i] = CharBank[randint(0, len(CharBank)-1)]
    shuffle(Password)
    Pass_String = ""
    for ele in Password:
        Pass_String += str(ele)
    print("Here is your PASSWORD:", Pass_String)
    print()                   
                 
# PIN Function, which creates a PIN of a specified digit amount
def PIN():
    print("You have chosen to create a PIN. Please answer the following:")

    # While loop that asks the user for the PIN length
    Length = ""
    while type(Length) != int:
        try:
            Length = int(input("Type PIN length (numbers only): "))
            print()
            Length = int(Length) 
        except:
            print(" Error. Please try again.")
            print()
    PIN = ""

    # Create the PIN
    for i in range(0,Length):
        Digit = randint(0,9)
        PIN += str(Digit)
    print("Here is your PIN:", PIN)
    print()

# main() function
def main():
    print("This program allows the user to create a PIN and/or a password.")
    print()
    print("The program will now ask the user what they want to create.", '\n'
          "     To create a password, type: PASSWORD", '\n'
          "     To create a PIN, type: PIN", '\n'
          "     To end the program, type: EXIT")
    print()

    # While loop that takes the input of the user and calls the appropriate
    # function
    Input = ""
    while Input != "EXIT":
        Input = input("What now does the user wish to create?: ")
        Input = Input.upper()
        print()
        if Input == "PASSWORD":
            PASSWORD()
        elif Input == "PIN":
            PIN()
        elif Input == "EXIT":
            print("Goodbye!")
        else:
            print(" Error. Please try again.")
            print() 

main()
