#
# Christopher Gibson (christopher.mitchell.gibson@gmail.com)
# Wordle!
# May 8, 2022
#

# Import necessary libraries
from graphics import *
from random import *
from time import *

# Define the PlayClicked() function, which accepts two parameters
def PlayClicked(mouse, menu):

    # If the Play rectangle is not clicked, return False
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()

    # Get the x,y coordinates of the Play Rectangle
    x1, y1 = 75, 75
    x2, y2 = 225, 125

    # Return the coordinate of the click if it is inside the control rectangle labelled EXIT
    return (x1 < mx < x2) and (y1 < my < y2)

# Define the InstructClicked() function, which accepts two parameters
def InstructClicked(mouse, menu):

    # If the Instruct rectangle is not clicked, return False
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()

    # Get the x,y coordinates of the Instruct Rectangle
    x1, y1 = 75, 150
    x2, y2 = 225, 200

    # Return true if the mouse click is within the rectangular area, or false if not
    return (x1 < mx < x2) and (y1 < my < y2)

# Define the ExitClicked() function, which accepts two parameters
def ExitClicked(mouse, menu):

    # If the Exit rectangle is not clicked, return False
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()

    # Get the x,y coordinates of the Exit Rectangle
    x1, y1 = 75, 225
    x2, y2 = 225, 275

    # Return true if the mouse click is within the rectangular area, or false if not
    return (x1 < mx < x2) and (y1 < my < y2)
  
# Define the Menu() function, which accepts no parameters
def Menu():

    # Create a 300 x 300 Graphics window with a dark grey background
    menu = GraphWin("Menu Window", 300, 300)
    menu.setBackground("light grey")

    # Create a text object centered at the top that will display WORDLE!
    Title = Text(Point(150, 30), "WORDLE!")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(menu)

    # Create a horizontal line under the word "WORDLE" that spans the screen
    Bar = Line(Point(0,50), Point(300,50))
    Bar.setWidth(3)
    Bar.draw(menu)

    # Create the green Play Rectangle with the word "Play" in it
    PlayRect = Rectangle(Point(75, 75), Point(225, 125))
    PlayRect.setFill("green")
    PlayRect.draw(menu)
    PlayText = Text(Point(150, 100), "Play")
    PlayText.setSize(20)
    PlayText.setTextColor("black")
    PlayText.draw(menu)

    # Create the yellow Instructions Rectangle with the world "Instructions" in it
    InstructRect = Rectangle(Point(75, 150), Point(225, 200))
    InstructRect.setFill("yellow")
    InstructRect.draw(menu)
    InstructText = Text(Point(150, 175), "Instructions")
    InstructText.setSize(20)
    InstructText.setTextColor("black")
    InstructText.draw(menu)

    # Create the red Exit Rectangle with the word "Exit" in it
    ExitRect = Rectangle(Point(75, 225), Point(225, 275))
    ExitRect.setFill("red")
    ExitRect.draw(menu)
    ExitText = Text(Point(150, 250), "Exit")
    ExitText.setSize(20)
    ExitText.setTextColor("black")
    ExitText.draw(menu)

    # Initialize mouse click as false
    mouse = menu.checkMouse()
    mouse == False

    # Define a while loop so that a click on the EXIT rectangle closes the window
    while ExitClicked(mouse, menu) == False:

        # Check for a mouse click
        mouse = menu.checkMouse()

        # If the user clicks on the Play Rectangle,
        if PlayClicked(mouse, menu) == True:

            # Option 1 is to play the Wordle Game
            Decision = 1

            # Return the window, the rectangles, and the Play Decision
            return menu, PlayRect, PlayText, InstructRect, InstructText, ExitRect, ExitText, Decision

        # If the user clicks on the Instruct Rectangle.
        if InstructClicked(mouse, menu) == True:

            # Option 2 is to view the instructions
            Decision = 2

            # Return the window, the rectangles, and the Instruct Decision
            return menu, PlayRect, PlayText, InstructRect, InstructText, ExitRect, ExitText, Decision
        
    # Decision 3 is to close the window
    Decision = 3

    # Close the control window
    menu.close()

    # Return the window, the list of rectangles, and the exit decision
    return menu, PlayRect, PlayText, InstructRect, InstructText, ExitRect, ExitText, Decision

# Define the BackClicked() function, which accepts two parameters
def BackClicked(mouse, InstructWin):

    # If the back button has not been clicked, return false
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()

    # Get the x,y coordinates of the Back Rectangle
    x1, y1 = 50, 180
    x2, y2 = 200, 230

    # Return true if the mouse click is within the rectangular area, or false if not
    return (x1 < mx < x2) and (y1 < my < y2)
    
# Define the Instructions function, which accepts no parameters
def Instructions():

    # Draw in a 250 x 250 window with a light grey background
    InstructWin = GraphWin("Instructions", 250, 250)
    InstructWin.setBackground("light grey")

    # Create a text object centered at the top that will display WORDLE!
    Title = Text(Point(125, 30), "WORDLE!")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(InstructWin)

    # Create a horizontal line under the word "WORDLE" that spans the screen
    Bar = Line(Point(0,50), Point(300,50))
    Bar.setWidth(3)
    Bar.draw(InstructWin)    

    # Create a yellow back rectangle at the bottom of the window
    BackRect = Rectangle(Point(50, 180), Point(200, 230))
    BackRect.setFill("yellow")
    BackRect.draw(InstructWin)
    BackText = Text(Point(125, 205), "Back")
    BackText.setSize(25)
    BackText.setTextColor("black")
    BackText.draw(InstructWin)

    # Create the list of instructions and initialize value of ylevel1
    Instruct_List = ["In Wordle, you have six guesses to guess a",
                     "random five letter word. After each guess,",
                     "the game tells you which letters are not in",
                     "the word (in grey), which are in the word",
                     "but in the wrong location (in yellow), and",
                     "those in the right location (in green)."]
    ylevel1 = 75

    # Draw the instructions in
    for i in range(6):
        HowTo = Text(Point(125, ylevel1), Instruct_List[i])
        HowTo.setSize(8)
        HowTo.draw(InstructWin)
        ylevel1 += 15

    # Initialize mouse click as False
    mouse = InstructWin.checkMouse()
    mouse == False

    # Use while loop that ends when the Back rectangle is clicked
    while BackClicked(mouse, InstructWin) == False:

        # Check for a mouse click
        mouse = InstructWin.checkMouse()

    # Close the window
    InstructWin.close()

# Define the split function, which accepts one parameter
def split(Guess):

    # Return a list where each character of the string is a entry 
    return [char for char in Guess]

# Define the Download() function, which accepts no parameters
def Download():

    # Open and read the 5-Letter-Words.txt file
    file = "5-Letter-Words.txt"
    infile = open(file, "r", encoding = 'utf8')

    # Initialize the list of words
    AnsList = []

    # Read the first line of the file
    line = infile.readline()

    # Use a while loop to fill in the list, where each entry is a word
    while line != "":

        # Remove the newline character from each line
        line = line.replace("\n", "")

        # Capitalize every word (if not so already)
        line = line.upper()

        # Append the line to the list
        AnsList.append(line)

        # Read the next line of the file
        line = infile.readline()
    
    # Close the file
    infile.close()
    
    # return the list of words
    return AnsList

# Define the Pickword() function, which accpets a list as a parameter
def Pickword(AnsList):

    # Choose a random word from the list
    Answer = choice(AnsList)

    # Return the randomly generated word
    return Answer

# Define the CheckGuess() function, which accepts multiple parameters
def CheckGuess(Guess, Answer):

    # Initialize variables 
    length = len(Answer)
    Result = ["-"] * length

    # Handles the case in which the letter is in the correct position and word
    for index in range(length):
        if Guess[index] == Answer[index]:
            Result[index] = "green"
            Answer = Answer.replace(Guess[index], "-", 1)

    # for loop to handle the cases if there are duplicates
    for index in range(length):
        if (Guess[index] in Answer) and (Result[index] == "-"):
            Result[index] = "yellow"
            Answer = Answer.replace(Guess[index], "-", 1)

    # Return the Result
    return Result

# Define the Popup() Function, which accepts three parameters
def Popup(board, TextSet, Answer, Attempt):

    # Draw in a Red or Green Error Rectangle (depending on the TextSet #)
    if (TextSet == 1) or (TextSet == 2) or (TextSet == 4):
        RectColor = "red"
    else:
        RectColor = "green"
    PopupRect = Rectangle(Point(100, 300), Point(500, 500))
    PopupRect.setFill(RectColor)
    PopupRect.draw(board)

    # Draw in the Header for the Rectangle (depending on the TextSet #)
    if (TextSet == 1) or (TextSet == 4):
        HeaderText = "ERROR"
    elif (TextSet == 2):
        HeaderText = "YOU LOSE"
    else:
        HeaderText = "CONGRATS!"
    Header = Text(Point(300, 330), HeaderText)
    Header.setStyle("bold")
    Header.setSize(22)
    Header.draw(board)

    # Draw in the Body of Text (Depending on the TextSet #)
    if (TextSet == 1):
        Line_Text1 = "This word is not a valid guess"
        Line_Text2 = "Please try another word"
    elif (TextSet == 2):
        Line_Text1 = "You've used all available attempts"
        Line_Text2 = "The correct word was: " + Answer
    elif (TextSet == 3):
        Line_Text1 = "You have solved this Wordle!"
        Line_Text2 = "It took you " + str(Attempt+1) + " attempt(s)!"
    elif (TextSet == 4):
        Line_Text1 = "You have already tried this word"
        Line_Text2 = "Please try another word"
    TextLine1 = Text(Point(300, 365), Line_Text1)
    TextLine1.setStyle("bold")
    TextLine1.setSize(18)
    TextLine1.draw(board)
    TextLine2 = Text(Point(300, 400), Line_Text2)
    TextLine2.setStyle("bold")
    TextLine2.setSize(18)
    TextLine2.draw(board)
    TextLine3 = Text(Point(300, 470), "Click anywhere to dismiss")
    TextLine3.setStyle("bold")
    TextLine3.setStyle("italic")
    TextLine3.setSize(18)
    TextLine3.draw(board)

    # Wait for a mouse click
    board.getMouse()

    # Undraw everything
    PopupRect.undraw()
    Header.undraw()
    TextLine1.undraw()
    TextLine2.undraw()
    TextLine3.undraw()
    
    # Return
    return

# Define the makeGame() function, which accepts two parameters
def makeGame(Answer, AnsList):

    # Create a 600 x 800 Graphics window with a white background
    board = GraphWin("Wordle!", 600, 800)
    board.setBackground("white")

    # Create a text object centered at the top that will display WORDLE!
    Title = Text(Point(300, 35), "WORDLE!")
    Title.setStyle("bold")
    Title.setSize(30)
    Title.draw(board)

    # Create a horizontal line under the word "WORDLE" that spans the screen
    Bar = Line(Point(0,60), Point(600,60))
    Bar.setWidth(3)
    Bar.draw(board)
    
    # Create the entry box
    GEnt = Entry(Point(375,90), 10)
    GEnt.setSize(20)
    GEnt.setFill("white")
    GEnt.draw(board)

    # Create the Guess Text Object which will be next to the entry box
    GText = Text(Point(250, 90), "Guess:")
    GText.setSize(15)
    GText.draw(board)
    
    # Use a for loop to create the 7 horizontal lines
    HBarList = []
    ylevel = 120
    for i in range(0,7):
        GridHBar = Line(Point(50, ylevel), Point(550, ylevel))
        GridHBar.setWidth(3)
        GridHBar.draw(board)
        HBarList.append(GridHBar)
        ylevel += 100

    # Use a for loop to create the 6 vertical lines
    VBarList = []
    xlevel = 50
    for i in range(0,6):
        GridVBar = Line(Point(xlevel, 120), Point(xlevel, 720))
        GridVBar.setWidth(3)
        GridVBar.draw(board)
        VBarList.append(GridVBar)
        xlevel += 100

    # Write a note on the bottom of the screen using a for loop
    NoteTextList = ["To guess, click in the entry box, type a word, and then click elsewhere on the screen",
                    "Due to the program's set up, the user is disallowed from guessing the same word twice"]                
    ylevel = 735
    for i in range(0,2):
        Note = Text(Point(300, ylevel), NoteTextList[i])
        Note.setStyle("italic")
        Note.setSize(10)
        Note.draw(board)
        ylevel += 15
    
    # Initialize Number of Attempts, the list of already guessed words, and yvalue2 (for later)
    Attempt = 0
    ylevel2 = 170
    Guessed = []
    
    # Use a while loop to play the game, end condition is once 6 attempts have been reached
    while Attempt < 6:
        
        # Initialize Validity value
        Valid = ""
        
        # Set up while loop, where the loop ends once a word is deemed valid
        while Valid != "YES":
            
            # Wait for the user to click
            board.getMouse()

            # Get the string from the Entry Box
            Guess = GEnt.getText()

            # If the guess is not a valid guess, run the Popup function  to display an error and set value of Valid
            if Guess == "":
                Valid = "NO"
            elif Guess.upper() in Guessed:
                TextSet = 4
                Popup(board, TextSet, Answer, Attempt)
            elif not (Guess.upper() in AnsList):
                TextSet = 1
                Popup(board, TextSet, Answer, Attempt)
                Valid = "NO"
            else:
                Guessed.append(Guess.upper())
                Valid = "YES"

        # Turn the string into all uppercase (if not entered as such)
        Guess = Guess.upper()
        
        # Call the CheckGuess() function
        Result = CheckGuess(Guess, Answer)
    
        # Use a for loop and if-else statements to turn the "-" into "dark grey" 
        for i in range(0,5):
            if Result[i] == "-":
                Result[i] = "dark grey"
                
        # Use a for loop to draw the letter in the appropriate box
        LetList = []
        xlevel2 = 100
        for i in range(0,5):
            Letter = Text(Point(xlevel2, ylevel2), Guess[i])
            Letter.setSize(30)
            Letter.setTextColor(Result[i]) 
            Letter.draw(board)
            LetList.append(Letter)
            xlevel2 += 100
        ylevel2 += 100

        # If the guess is correct, tell the user they have won
        if Result == ["green", "green", "green", "green", "green"]:

                # Have the program wait a second
                sleep(1)
                
                # Run the Popup() function to tell the user that they have won
                TextSet = 3
                Popup(board, TextSet, Answer, Attempt)
                                
                # Use the break command (It prevents a getMouse in closed window error)
                break
            
        # Else, add one to the attempt
        else:
            Attempt += 1

    # At this point, the user has lost. 
    if Attempt == 6:

        # Have the program wait a second
        sleep(1)
        
        # Load the Popup() function to tell the user that they have lost
        TextSet = 2
        Popup(board, TextSet, Answer, Attempt)
        
    #Close the window
    board.close()
    
# Define main function
def main():

    # Display the main menu
    menu, PlayRect, PlayText, InstructText, InstructRect, ExitRect, ExitText, Decision = Menu()

    # Download the word list
    AnsList = Download()
    
    # While the user has not clicked the Exit rectangle
    while Decision != 3:

        # If the user clicks on the Instruct Rectangle
        if Decision == 2:

            # Close the Main menu
            menu.close()

            # Open the instructions window
            Instructions()

        # If the user clicks on the Play Rectangle
        if Decision == 1:

            # close the Main menu
            menu.close()

            # Create the word the user needs to guess
            Answer = Pickword(AnsList)
            
            # Allow the user to play the game
            makeGame(Answer, AnsList)
            
        # Reopen the Main menu
        menu, PlayRect, PlayText, InstructText, InstructRect, ExitRect, ExitText, Decision = Menu()
        
# End main function    
main()
