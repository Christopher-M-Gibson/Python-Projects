#
# Christopher Gibson (christopher.mitchell.gibson@gmail.com)
# Tic-Tac-Toe
# May 23, 2022
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
    menu = GraphWin("Main Menu", 300, 300)
    menu.setBackground("light grey")

    # Create a text object centered at the top that will display HANGMAN
    Title = Text(Point(150, 30), "TIC-TAC-TOE")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(menu)

    # Create a horizontal line under the word "HANGMAN" that spans the screen
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

            # Option 1 is to play the Hangman Game
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

    # Create a text object centered at the top that will display HANGMAN
    Title = Text(Point(125, 30), "TIC-TAC-TOE")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(InstructWin)

    # Create a horizontal line under the word "HANGMAN" that spans the screen
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
    Instruct_List = ["Tic-Tac-Toe is a turn-based game where two",
                     "opponents attempt to form a row of either",
                     "X's or O's in a 3 x 3 grid by selecting one",
                     "spot in which they want to place thier symbol.",
                     "Here, the user can either play against the",
                     "computer, or locally with another person."]
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

# Define the OnePlayClicked() function, which accepts two parameters
def OnePlayClicked(mouse, GameSelectWin):

    # If the One Player button has not been clicked, return false
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()
    
    # Get the x, y coordinates of the One Player Rectangle
    x1, y1 = 50, 75
    x2, y2 = 200, 125

    # Return true if the mouse click is within the rectangular area, or false if not
    return (x1 < mx < x2) and (y1 < my < y2)

# Define the TwoPlayClicked() function, which accepts two parameters
def TwoPlayClicked(mouse, GameSelectWin):
    
    # If the Two Player button has not been clicked, return false
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()
    
    # Get the x, y coordinates of the Two Player Rectangle
    x1, y1 = 50, 145
    x2, y2 = 200, 195

    # Return true if the mouse click is within the rectangular area, or false if not
    return (x1 < mx < x2) and (y1 < my < y2)

# Define the Back2Clicked function, which accepts two parameters
def Back2Clicked(mouse, GameSelectWin):

    # If the Two Player button has not been clicked, return false
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()
    
    # Get the x, y coordinates of the Two Player Rectangle
    x1, y1 = 50, 215
    x2, y2 = 200, 265

    # Return true if the mouse click is within the rectangular area, or false if not
    return (x1 < mx < x2) and (y1 < my < y2)

# Define the SecondaryMenu() Function, which accepts zero parameters
def SecondaryMenu():

    # Create a 250 x 250 window with a light grey window
    GameSelectWin = GraphWin("Game Selection", 250, 285)
    GameSelectWin.setBackground("light grey")

    # Create a text object centered at the top that will display "Select Mode"
    Title = Text(Point(125, 30), "Select Mode")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(GameSelectWin)

    # Create a horizontal line under the word "Select Mode" that spans the screen
    Bar = Line(Point(0,50), Point(300,50))
    Bar.setWidth(3)
    Bar.draw(GameSelectWin)

    # Create a green rectangle that says One Player in it
    OPlayRect = Rectangle(Point(50, 75), Point(200, 125))
    OPlayRect.setFill("green")
    OPlayRect.draw(GameSelectWin)
    OPlayText = Text(Point(125, 100), "One Player")
    OPlayText.setSize(20)
    OPlayText.setTextColor("black")
    OPlayText.draw(GameSelectWin)

    # Create a green rectangle that says Two Player in it
    TPlayRect = Rectangle(Point(50, 145), Point(200, 195))
    TPlayRect.setFill("green")
    TPlayRect.draw(GameSelectWin)
    TPlayText = Text(Point(125, 170), "Two Player")
    TPlayText.setSize(20)
    TPlayText.setTextColor("black")
    TPlayText.draw(GameSelectWin)
    
    # Create a yellow back rectangle at the bottom of the window
    BackRect = Rectangle(Point(50, 215), Point(200, 265))
    BackRect.setFill("yellow")
    BackRect.draw(GameSelectWin)
    BackText = Text(Point(125, 240), "Back")
    BackText.setSize(20)
    BackText.setTextColor("black")
    BackText.draw(GameSelectWin)

    # Initialize Mouse click as false
    mouse = GameSelectWin.checkMouse()
    mouse == False
    
    # Define a while loop so that a click on the Back rectangle closes the window
    while Back2Clicked(mouse, GameSelectWin) == False:

        # Check for a mouse click
        mouse = GameSelectWin.checkMouse()

        # If the user clicks on the One Player Rectangle,
        if OnePlayClicked(mouse, GameSelectWin) == True:

            # Option 1 is to play Tic-Tac-Toe against the computer
            Decision2 = 1

            # Return the window, the rectangles, and the One Player Decision
            return GameSelectWin, OPlayRect, OPlayText, TPlayRect, TPlayText, BackRect, BackText, Decision2

        # If the user clicks on the Two Player Rectangle,
        if TwoPlayClicked(mouse, GameSelectWin) == True:

            # Option 2 is to play Tic-Tac-Toe locally against anothe player
            Decision2 = 2
            
            # Return the window, the rectangles, and the Two Player Decision
            return GameSelectWin, OPlayRect, OPlayText, TPlayRect, TPlayText, BackRect, BackText, Decision2

    # Decision 3 is to head back to the main menu
    Decision2 = 3

    # Close the window
    GameSelectWin.close()

    # Return the window, the rectangles, and the Back Decision
    return GameSelectWin, OPlayRect, OPlayText, TPlayRect, TPlayText, BackRect, BackText, Decision2


# ==============================================================================================================#
# THIS FOLLOWING CODE PERTAINS TO FUNCTIONS WHICH ARE APPLICABLE TO BOTH THE ONE PLAYER AND TWO PLAYER GAME MODES
# ==============================================================================================================#

# Define the DrawBoard() function, which accepts zero parameters
def DrawBoard():

    # Create a 600 x 570 Graphics Window with a white background
    board = GraphWin("Hangman", 600, 570)
    board.setBackground("white")

    # Create a text object centered at the top that will display "TIC-TAC-TOE"
    Title = Text(Point(300, 35), "TIC-TAC-TOE")
    Title.setStyle("bold")
    Title.setSize(30)
    Title.draw(board)

    # Create a horizontal line under the word "TIC-TAC-TOE" that spans the screen
    TBar = Line(Point(0,60), Point(600,60))
    TBar.setWidth(3)
    TBar.draw(board)

    # Create a rectangle that will be the outer part of the board
    OuterRect = Rectangle(Point(75,70), Point(525,520))
    OuterRect.setWidth(3)
    OuterRect.draw(board)

    # Use a for loop to create the two horizontal lines
    HBarList = []
    ylevel = 220
    for i in range(0,2):
        GridHBar = Line(Point(75, ylevel), Point(525, ylevel))
        GridHBar.setWidth(3)
        GridHBar.draw(board)
        HBarList.append(GridHBar)
        ylevel += 150

    # Use a for loop to create the two vertical lines
    VBarList = []
    xlevel = 225
    for i in range(0,2):
        GridVBar = Line(Point(xlevel, 70), Point(xlevel, 520))
        GridVBar.setWidth(3)
        GridVBar.draw(board)
        VBarList.append(GridVBar)
        xlevel += 150

    # Create a line under the board that spans the screen
    BBar = Line(Point(0, 530), Point(600,530))
    BBar.setWidth(3)
    BBar.draw(board)

    # Return the board, the rectangle, and the lines
    return board, OuterRect, HBarList, VBarList

# Define the Pick_Starter_Icon() function, which accepts zero parameters
def Pick_Starter_Icon(Decision2):

    # Initialize the list of possible icons and the possible starter
    IconList = ["X", "O"]
    StarterList = ["", ""]

    # Depending on the value of Decision2, replace the values in StarterList
    if Decision2 == 1:
        StarterList[0] = "Player"
        StarterList[1] = "Computer"
    else:
        StarterList[0] = "Player One"
        StarterList[1] = "Player Two"
    
    # Randomly select the icon the Player (Or Player One) will have
    PlayerIcon = choice(IconList)

    # Use the value of PlayerOneIcon to select the icon Player Two will have
    if PlayerIcon == "X":
        OpponentIcon = "O"
    else:
        OpponentIcon = "X"

    # Randomly Select which player will start
    Starter = choice(StarterList)
    
    # Return the icons for the participants in the game
    return PlayerIcon, OpponentIcon, Starter

# Define the TurnStarter() Function, which accepts 4 parameters
def TurnStarter(board, Starter, PlayerIcon, OpponentIcon, Decision2):

    # Draw in a yellow rectangle that will appear on the screen
    StarterRect = Rectangle(Point(100, 200), Point(500, 400))
    StarterRect.setFill("yellow")
    StarterRect.draw(board)

    # Determine the TextList based on the value of Decision2
    if Decision2 == 1:
        TextList = ["The " + Starter + " will make the first move",
                    "The Player will be " + PlayerIcon,
                    "The Computer will be " + OpponentIcon]               
    else:
        TextList = [Starter + " will make the first move",
                "Player One will be " + PlayerIcon,
                "Player Two will be " + OpponentIcon]

    # Draw in the Text using a for loop
    InfoTextItemList = []
    ylevel = 220
    for i in range(0,3):
        InfoText = Text(Point(300, ylevel), TextList[i])
        InfoText.setSize(16)
        InfoText.setStyle("bold")
        InfoTextItemList.append(InfoText)
        InfoText.draw(board)
        ylevel += 40

    # Draw in the bottom text line that tells the user to click
    BottomTextLine = Text(Point(300,370), "Click anywhere to dismiss")
    BottomTextLine.setStyle("bold italic")
    BottomTextLine.setSize(18)
    BottomTextLine.draw(board)

    # Wait for a mouse click
    board.getMouse()

    # Undraw everything
    StarterRect.undraw()
    for i in range(0,3):
        InfoTextItemList[i].undraw()
    BottomTextLine.undraw()

    # Return
    return

# Define the ClickedBoard() function, which accepts two parameters
def ClickedBoard(mouse, board):

    # If a click is not inside the clickable area, return False
    if not mouse:
        return False

    # Get the x,y coordinates of the mouse click
    mx, my = mouse.getX(), mouse.getY()

    # Get the x,y coordinates of the corners of the rectangle
    x1, y1 = 75, 70
    x2, y2 = 525, 520

    # Return True if the mouse click is within the the rectangle
    return (x1 < mx < x2) and (y1 < my < y2)

# Define the FindMove() function, which accepts two parameters
def FindMove(mx, my):

    # Use the location of the mouse click to determine the move and center of the square
    if (75<mx<225) and (70<my<220):
        cx, cy = 150, 145
        Move = "TopLeft"
    elif (225<mx<375) and (70<my<220):
        cx, cy = 300, 145
        Move = "TopMid"
    elif (375<mx<525) and (70<my<220):
        cx, cy = 450, 145
        Move = "TopRight"
    elif (75<mx<225) and (220<my<370):
        cx, cy = 150, 295
        Move = "MidLeft"
    elif (225<mx<375) and (220<my<370):
        cx, cy = 300, 295
        Move = "MidMid"
    elif (375<mx<525) and (220<my<370):
        cx, cy = 450, 295
        Move = "MidRight"
    elif (75<mx<225) and (370<my<520):
        cx, cy = 150, 445
        Move = "BotLeft"
    elif (225<mx<375) and (370<my<520):
        cx, cy = 300, 445
        Move = "BotMid"
    elif (375<mx<525) and (370<my<520):
        cx, cy = 450, 445
        Move = "BotRight"

    # Return the guess and the center coordinates
    return cx, cy, Move

# Define the DetermineWinner Function, which accepts 3 parameters
def DetermineWinner(MoveDict, PlayerOneIcon, PlayerTwoIcon, Decision2):

    # Initialize the value of IsWinner, Winner, and WinningMoveSymbol
    IsWinner = ""
    Winner = ""
    WinningMoveSymbol = ""
    
    # Use if-else statements to determine if there is a winner
    if MoveDict["TopLeft"] == MoveDict["TopMid"] == MoveDict["TopRight"]:
        IsWinner = "YES"
        if MoveDict["TopLeft"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["MidLeft"] == MoveDict["MidMid"] == MoveDict["MidRight"]:
        IsWinner = "YES"
        if MoveDict["MidLeft"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["BotLeft"] == MoveDict["BotMid"] == MoveDict["BotRight"]:
        IsWinner = "YES"
        if MoveDict["BotLeft"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["TopLeft"] == MoveDict["MidLeft"] == MoveDict["BotLeft"]:
        IsWinner = "YES"
        if MoveDict["TopLeft"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["TopMid"] == MoveDict["MidMid"] == MoveDict["BotMid"]:
        IsWinner = "YES"
        if MoveDict["TopMid"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["TopRight"] == MoveDict["MidRight"] == MoveDict["BotRight"]:
        IsWinner = "YES"
        if MoveDict["TopRight"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["TopLeft"] == MoveDict["MidMid"] == MoveDict["BotRight"]:
        IsWinner = "YES"
        if MoveDict["TopLeft"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"
    elif MoveDict["TopRight"] == MoveDict["MidMid"] == MoveDict["BotLeft"]:
        IsWinner = "YES"
        if MoveDict["TopRight"] == PlayerOneIcon:
            Winner = "Player"
        else:
            Winner = "Opponent"

    # Based on the value of Decision2, rewrite the value of Player and Opponent for the Winner variable
    if (Decision2 == 1) and (Winner == "Player"):
        Winner = "Player"
    elif (Decision2 == 1) and (Winner == "Opponent"):
        Winner = "Computer"
    elif (Decision2 == 2) and (Winner == "Player"):
        Winner = "Player One"
    elif (Decision2 == 2) and (Winner == "Opponent"):
        Winner = "Player Two"
        
    # Return the value of IsWinner and Winner
    return IsWinner, Winner

# Define the WinorDraw function, which accepts two parameters
def WinOrDraw(board, TextSet, Winner, Decision2):
    
    # Draw in a red or green rectangle (depending on the TextSet #)
    if (TextSet == 2):
        RectColor = "red"
    else:
        RectColor = "green"
    PopupRect = Rectangle(Point(100, 200), Point(500, 350))
    PopupRect.setFill(RectColor)
    PopupRect.draw(board)

    # Draw in the Header for the Rectangle
    Header = Text(Point(300, 220), "The game has concluded!")
    Header.setStyle("bold")
    Header.setSize(22)
    Header.draw(board)

    # Draw in the first line of text
    TextLine1 = Text(Point(300, 255), "The game has ended in a:")
    TextLine1.setStyle("bold")
    TextLine1.setSize(18)
    TextLine1.draw(board)

    # Based on the value of Decision2 and TextSet, create the line for Line_Text2
    if (TextSet == 2):
        Line_Text2 = "DRAW"
    else:
        if Decision2 == 1:
            Line_Text2 = "victory by the " + Winner
        elif Decision2 == 2:
            Line_Text2 = "victory by " + Winner

    # Draw in the second line of text
    TextLine2 = Text(Point(300, 285), Line_Text2)
    TextLine2.setStyle("bold")
    TextLine2.setSize(18)
    TextLine2.draw(board)

    # Draw in the third line of text
    TextLine3 = Text(Point(300, 320), "Click anywhere to dismiss")
    TextLine3.setStyle("bold italic")
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

# ==============================================================================================#
# THIS FOLLOWING CODE PERTAINS TO FUNCTIONS WHICH ARE ONLY APPLICABLE TO THE ONE PLAYER GAME MODE
# ==============================================================================================#

# Define the FindCenter() function, which accepts one parameter
def FindCenter(Move):

    # Depending on the value of move, return the center of its area
    if Move == "TopLeft":
        cx, cy = 150, 145
    elif Move == "TopMid":
        cx, cy = 300, 145
    elif Move == "TopRight":
        cx, cy = 450, 145
    elif Move == "MidLeft":
        cx, cy = 150, 295
    elif Move == "MidMid":
        cx, cy = 300, 295
    elif Move == "MidRight":
        cx, cy = 450, 295
    elif Move == "BotLeft":
        cx, cy = 150, 445
    elif Move == "BotMid":
        cx, cy = 300, 445
    elif Move == "BotRight":
        cx, cy = 450, 445

    # Return the value of cx, cy
    return cx, cy

# Define the ComputerMove() function, which accepts multiple parameters
def ComputerMove(board, MoveDict, PlayerIcon, ComputerIcon, AvailableMoveList):

    # Make subsets of the MoveDict that will consist of all the winning combinations
    SubsetOne = {"TopLeft":MoveDict["TopLeft"],"TopMid":MoveDict["TopMid"],"TopRight":MoveDict["TopRight"]}
    SubsetTwo = {"MidLeft":MoveDict["MidLeft"],"MidMid":MoveDict["MidMid"],"MidRight":MoveDict["MidRight"]}
    SubsetThr = {"BotLeft":MoveDict["BotLeft"],"BotMid":MoveDict["BotMid"],"BotRight":MoveDict["BotRight"]}
    SubsetFou = {"TopLeft":MoveDict["TopLeft"],"MidLeft":MoveDict["MidLeft"],"BotLeft":MoveDict["BotLeft"]}
    SubsetFiv = {"TopMid":MoveDict["TopMid"],"MidMid":MoveDict["MidMid"],"BotMid":MoveDict["BotMid"]}
    SubsetSix = {"TopRight":MoveDict["TopRight"],"MidRight":MoveDict["MidRight"],"BotRight":MoveDict["BotRight"]}
    SubsetSev = {"TopLeft":MoveDict["TopLeft"],"MidMid":MoveDict["MidMid"],"BotRight":MoveDict["BotRight"]}
    SubsetEig = {"TopRight":MoveDict["TopRight"],"MidMid":MoveDict["MidMid"],"BotLeft":MoveDict["BotLeft"]}

    # Create a list of the subsets of dictionaries
    SubsetList = [SubsetOne, SubsetTwo, SubsetThr, SubsetFou, SubsetFiv, SubsetSix, SubsetSev, SubsetEig]

    # Initialize the Counters for PlayerIcon and ComputerIcon
    PICounter = 0
    CICounter = 0
    GenCounter = 0
    
    # Initialize two empty lists of how many of each Icon is in each subsetvv
    PICountList = []
    CICountList = []
    GenCountList = []
    
    # Use a for loop to run through each element of SubsetList
    for i in range(0,8):

        # Use a for loop to run through each element of each Subset
        for j in range(0,3):

            # If the element of the subset is an X or O, increment the appropriate counters
            if list(SubsetList[i].values())[j] == PlayerIcon:
                PICounter += 1
                GenCounter += 1
            elif list(SubsetList[i].values())[j] == ComputerIcon:
                CICounter += 1
                GenCounter += 1
                
        # Insert the value of the Counters into the appropriate lists
        PICountList.append(PICounter)
        CICountList.append(CICounter)
        GenCountList.append(GenCounter)

        # Reset the values of PICounter and CICounter to 0 for the next iteration
        PICounter = 0
        CICounter = 0
        GenCounter = 0

    # Loop through the list to check if the computer has two of three necessary spots
    for i in range(0,8):

        # If the position in CICountList is a 2,
        if (CICountList[i] == 2) and (GenCountList[i] != 3):

            # Loop through the elements of the Subsetlist
            for j in range(0,3):

                # Use an if statement to find the key of the value that is a number
                if type(list(SubsetList[i].values())[j]) == int:
                    Move = list(SubsetList[i].keys())[j]

            # Use the value of Move to find the center of the spot
            cx, cy = FindCenter(Move)

            # Draw in the icon at the center of the square that was clicked
            MadeMove = Text(Point(cx, cy), ComputerIcon)
            MadeMove.setSize(30)
            MadeMove.draw(board)

            # Remove the move from the Available move List
            AvailableMoveList.remove(Move)

            # Add an entry to dictionary in the form Move : Symbol
            MoveDict[Move] = ComputerIcon

            # Return the updated value of the dictionary and Available Move List
            return MoveDict, AvailableMoveList
            
    # Loop through the list to check if the player has two of three necessary spots
    for i in range(0,8):

        # If the position in PICountList is a 2:
        if (PICountList[i] == 2) and (GenCountList[i] != 3):

            # Loop through the elements of the appropriate SubsetList
            for j in range(0,3):

                # Use an if statement to find the key of the value that is a number
                if type(list(SubsetList[i].values())[j]) == int:
                    Move = list(SubsetList[i].keys())[j]

            # Use the value of Move to find the center of the spot
            cx, cy = FindCenter(Move)

            # Draw in the icon at the center of the square that was clicked
            MadeMove = Text(Point(cx, cy), ComputerIcon)
            MadeMove.setSize(30)
            MadeMove.draw(board)

            # Remove the move from the Available move List
            AvailableMoveList.remove(Move)

            # Add an entry to dictionary in the form Move : Symbol
            MoveDict[Move] = ComputerIcon

            # Return the updated value of the dictionary and Available Move List
            return MoveDict, AvailableMoveList

    # Initialize the lists of corners and sides
    CornersList = ["TopLeft", "TopRight", "BotLeft", "BotRight"]
    SidesList = ["TopMid", "MidLeft", "BotMid", "MidRight"]
    PotentialMoveC = []
    PotentialMoveS = []

    # Use a for loop to run through the list of Corners and Sides
    for i in range(0,4):

        # If a corner move is available,
        if CornersList[i] in AvailableMoveList:

            # Append it to the Potential Moves list
            PotentialMoveC.append(CornersList[i])

        # If a side move is available,
        if SidesList[i] in AvailableMoveList:

            # Append it to the Potential Moves Sides List
            PotentialMoveS.append(SidesList[i])

    # If a corner move can be made,
    if len(PotentialMoveC) > 0:

        # Make it
        Move = choice(PotentialMoveC)

    # If the center spot can be taken,
    elif "MidMid" in AvailableMoveList:

        # Take it
        Move = "MidMid"

    # Or else, take a side spot
    else:
        Move = choice(PotentialMoveS)

    # Use the value of Move to find the center of the spot
    cx, cy = FindCenter(Move)

    # Draw in the icon at the center of the square that was clicked
    MadeMove = Text(Point(cx, cy), ComputerIcon)
    MadeMove.setSize(30)
    MadeMove.draw(board)

    # Remove the move from the Available move List
    AvailableMoveList.remove(Move)

    # Add an entry to dictionary in the form Move : Symbol
    MoveDict[Move] = ComputerIcon

    # Return the updated value of the dictionary and Available Move List
    return MoveDict, AvailableMoveList
    
# Define the TicTacOne() function, which accepts zero parameters
def TicTacOne(Decision2):

    # Draw the board in
    board, OuterRect, HBarList, VBarList = DrawBoard()

    # Pick whether the Player or Computer Starts and what their icons are
    PlayerIcon, ComputerIcon, Starter = Pick_Starter_Icon(Decision2)       

    # Draw in the Player and Computer Icons at the Bottom of the Screen
    PlayerText = Text(Point(100,550), "  Player: " + PlayerIcon)
    PlayerText.setSize(20)
    PlayerText.draw(board)
    ComputerText = Text(Point(500, 550), "Computer: " + ComputerIcon)
    ComputerText.setSize(20)
    ComputerText.draw(board)

    # Load the TellStarter() function, which informs the player if they are starting or not
    TurnStarter(board, Starter, PlayerIcon, ComputerIcon, Decision2)
    
    # Initialize the turn number, as well as the dictionary of moves
    TurnNumber = 1
    MoveDict = {"TopLeft":0, "TopMid":1, "TopRight":2, "MidLeft":3, "MidMid":4,
                "MidRight":5, "BotLeft":6, "BotMid":7, "BotRight":8}

    # Initialize the list of moves that are available, as well as if there is a winner
    AvailableMoveList = ["TopLeft", "TopMid", "TopRight",
                         "MidLeft", "MidMid", "MidRight",
                         "BotLeft", "BotMid", "BotRight"]
    IsWinner = ""

    # Initialize Mouse click as false
    mouse = board.checkMouse()
    mouse == False

    # If the user was picked to go first
    if Starter == "Player":

        #  Create a while loop where the end conditions are either the player mas made 5 turns or a winner was found
        while (TurnNumber < 6) and (IsWinner == ""):
            
            # Initialize the value of Valid
            Valid = ""
            
            # Create a while loop that will run until a guess is deemed to be valid
            while Valid != "YES":
                
                # Let the user click on the screen
                mouse = board.getMouse()

                # Set up a while loop, where end condition is a move is made
                while ClickedBoard(mouse, board) == False:

                    # Wait for the user to click
                    mouse = board.getMouse()

                # Get the coordinates of the mouse click
                mx, my = mouse.getX(), mouse.getY()
                
                # Load the FindMove() function, which determines the move the player made based on the click
                cx, cy, Move = FindMove(mx,my)

                # If the move is still an available move
                if Move in AvailableMoveList:
        
                    # Draw in the icon at the center of the square that was clicked
                    MadeMove = Text(Point(cx, cy), PlayerIcon)
                    MadeMove.setSize(30)
                    MadeMove.draw(board)

                    # Remove the move from the Available move List
                    AvailableMoveList.remove(Move)

                    # Add an entry to dictionary in the form Move : Symbol
                    MoveDict[Move] = PlayerIcon

                    # The move is valid
                    Valid = "YES"

                # If the move is not an available move
                else:

                    # Do not draw anything in
                    Valid = "NO"
            
            # Load the DetermineWinner() function, which will evaluate if a winner is present
            IsWinner, Winner = DetermineWinner(MoveDict, PlayerIcon, ComputerIcon, Decision2)

            # If there is a winner
            if IsWinner == "YES":

                # Wait one second
                sleep(1)
                
                # Load the WinOrDraw() Function, which will notify the users who won
                TextSet = 1
                WinOrDraw(board, TextSet, Winner, Decision2)
                break

            # If AvailableMoveList is empty, break the loop
            if len(AvailableMoveList) == 0:
                break

            # Wait for one second
            sleep(1)
            
            # Load the ComputerMove() function, which is how the computer will make its move
            MoveDict, AvailableMoveList = ComputerMove(board, MoveDict, PlayerIcon, ComputerIcon, AvailableMoveList)

            # Load the DetermineWinner() function, which will evaluate if a winner is present
            IsWinner, Winner = DetermineWinner(MoveDict, PlayerIcon, ComputerIcon, Decision2)

            # If there is a winner
            if IsWinner == "YES":

                # Wait one second
                sleep(1)
                
                # Load the WinOrDraw() Function, which will notify the users who won
                TextSet = 1
                WinOrDraw(board, TextSet, Winner, Decision2)
                break
            
            # Add one to the TurnNumber
            TurnNumber += 1
        
    # If the computer was picked to go first
    elif Starter == "Computer":

        # Create a while loop that ends after 5 turns have been made or a winner was found
        while (TurnNumber < 6) and (IsWinner == ""):

            # Wait one second
            sleep(1)
            
            # Load the ComputerMove() function, which is how the computer will make its move
            MoveDict, AvailableMoveList = ComputerMove(board, MoveDict, PlayerIcon, ComputerIcon, AvailableMoveList)
        
            # Load the DetermineWinner() function, which will evaluate if a winner is present
            IsWinner, Winner = DetermineWinner(MoveDict, PlayerIcon, ComputerIcon, Decision2)

            # If there is a winner
            if IsWinner == "YES":

                # Wait one second
                sleep(1)
                
                # Load the WinOrDraw() Function, which will notify the users who won
                TextSet = 1
                WinOrDraw(board, TextSet, Winner, Decision2)
                break

            # If AvailableMoveList is empty, break the loop
            if len(AvailableMoveList) == 0:
                break
                
            # Initialize the value of Valid
            Valid = ""
            
            # Create a while loop that will run until a guess is deemed to be valid
            while Valid != "YES":
                
                # Let the user click on the screen
                mouse = board.getMouse()

                # Set up a while loop, where end condition is a move is made
                while ClickedBoard(mouse, board) == False:

                    # Wait for the user to click
                    mouse = board.getMouse()

                # Get the coordinates of the mouse click
                mx, my = mouse.getX(), mouse.getY()
                
                # Load the FindMove() function, which determines the move the player made based on the click
                cx, cy, Move = FindMove(mx,my)

                # If the move is still an available move
                if Move in AvailableMoveList:
        
                    # Draw in the icon at the center of the square that was clicked
                    MadeMove = Text(Point(cx, cy), PlayerIcon)
                    MadeMove.setSize(30)
                    MadeMove.draw(board)

                    # Remove the move from the Available move List
                    AvailableMoveList.remove(Move)

                    # Add an entry to dictionary in the form Move : Symbol
                    MoveDict[Move] = PlayerIcon

                    # The move is valid
                    Valid = "YES"

                # If the move is not an available move
                else:

                    # Do not draw anything in
                    Valid = "NO"
            
            # Load the DetermineWinner() function, which will evaluate if a winner is present
            IsWinner, Winner = DetermineWinner(MoveDict, PlayerIcon, ComputerIcon, Decision2)

            # If there is a winner
            if IsWinner == "YES":

                # Wait one second
                sleep(1)
                
                # Load the WinOrDraw() Function, which will notify the users who won
                TextSet = 1
                WinOrDraw(board, TextSet, Winner, Decision2)
                #break
            
            # Add one to the TurnNumber
            TurnNumber += 1

    # If all 9 turns have elapsed, and no one has won,
    if (TurnNumber == 5) and (IsWinner != "YES"):

        # Wait one second
        sleep(1)
        
        # Load the WinOrDraw() function, which will notify the user that a draw has occured
        TextSet = 2
        WinOrDraw(board, TextSet, Winner, Decision2)

    # Close the window
    board.close()
    
# ==============================================================================================#
# THIS FOLLOWING CODE PERTAINS TO FUNCTIONS WHICH ARE ONLY APPLICABLE TO THE TWO PLAYER GAME MODE
# ==============================================================================================#

# Define the TicTacTwo function, which accepts one parameter
def TicTacTwo(Decision2):

    # Draw the board in
    board, OuterRect, HBarList, VBarList = DrawBoard()

    # Load the Pick_Starter_Icon() function, which randomly selects who starts and the icons for each player
    PlayerOneIcon, PlayerTwoIcon, Starter = Pick_Starter_Icon(Decision2)

    # Determine the IconList based on the Starter and the Players' icons
    if (Starter == "Player One" and PlayerOneIcon == "X") or (Starter == "Player Two" and PlayerTwoIcon == "X"):
        IconList = ["X", "O", "X", "O", "X", "O", "X", "O", "X"]
    else:
        IconList = ["O", "X", "O", "X", "O", "X", "O", "X", "O"]
        
    # Draw in the Player One and Player Two icons at the bottom of the screen
    PlayerOne = Text(Point(100, 550), "Player One: " + PlayerOneIcon)
    PlayerOne.setSize(20)
    PlayerOne.draw(board)
    PlayerTwo = Text(Point(500, 550), "Player Two: " + PlayerTwoIcon)
    PlayerTwo.setSize(20)
    PlayerTwo.draw(board)

    # Load the TellStarter() function, which informs those playing who will start
    TurnStarter(board, Starter, PlayerOneIcon, PlayerTwoIcon, Decision2)
    
    # Initialize the turn number, as well as the dictionary of moves
    TurnNumber = 1
    MoveDict = {"TopLeft":0, "TopMid":1, "TopRight":2, "MidLeft":3, "MidMid":4,
                "MidRight":5, "BotLeft":6, "BotMid":7, "BotRight":8}

    # Initialize the list of moves that are available
    AvailableMoveList = ["TopLeft", "TopMid", "TopRight", "MidLeft", "MidMid", "MidRight", "BotLeft", "BotMid", "BotRight"]
    IsWinner = ""
    
    # Initialize Mouse click as false
    mouse = board.checkMouse()
    mouse == False
    
    # Create a while loop where end conditions are either 9 turns have elapsed or someone won
    while (TurnNumber < 10) and (IsWinner == ""):
        
        # Let the user click on the screen
        mouse = board.getMouse()

        # Set up a while loop, where end condition is a move is made
        while ClickedBoard(mouse, board) == False:

            # Wait for the user to click
            mouse = board.getMouse()

        # Get the coordinates of the mouse click
        mx, my = mouse.getX(), mouse.getY()

        # Load the FindMove() function, which determines the move the player made based on the click
        cx, cy, Move = FindMove(mx,my)

        # If the move is still an available move
        if Move in AvailableMoveList:
        
            # Draw in the icon at the center of the square that was clicked
            MadeMove = Text(Point(cx, cy), IconList[TurnNumber - 1])
            MadeMove.setSize(30)
            MadeMove.draw(board)

            # Remove the move from the Available move List
            AvailableMoveList.remove(Move)

            # Add an entry to dictionary in the form Move : Symbol
            MoveDict[Move] = IconList[TurnNumber - 1]
            
            # Add one to TurnNumber 
            TurnNumber += 1

        # If the move is not an available move
        else:

            # Do not draw anything in
            TurnNumber += 0

        # Load the DetermineWinner() function, which will evaluate if a winner is present
        IsWinner, Winner = DetermineWinner(MoveDict, PlayerOneIcon, PlayerTwoIcon, Decision2)

        # If there is a winner
        if IsWinner == "YES":

            # Wait one second
            sleep(1)
            
            # Load the WinOrDraw() Function, which will notify the users who won
            TextSet = 1
            WinOrDraw(board, TextSet, Winner, Decision2)

    # If all turns have been used
    if TurnNumber == 10:

        # Wait one second
        sleep(1)
        
        # Load the WinOrDraw() function, which will tell the users the game ended in a draw
        TextSet = 2
        WinOrDraw(board, TextSet, Winner, Decision2)

    # Close the window
    board.close()

#======================================================#
# THE FOLLOWING CODE IS RESERVED FOR THE MAIN() FUNCTION
#======================================================#        
      
# Define main function
def main():

    # Display the main menu
    menu, PlayRect, PlayText, InstructText, InstructRect, ExitRect, ExitText, Decision = Menu()
    
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

            # Open the secondary menu
            GameSelectWin, OPlayRect, OPlayText, TPlayRect, TPlayText, BackRect, BackText, Decision2 = SecondaryMenu()

            # While the user has not clicked the Back Rectangle
            while Decision2 != 3:

                # If the user clicks on the One Player Rectangle
                if Decision2 == 1:

                    # Close the secondary menu
                    GameSelectWin.close()

                    # Let the user play the one player version of Tic-Tac-Toe -----------------------------------------
                    TicTacOne(Decision2)

                # If the user clicks on the Two Player Rectangle
                if Decision2 == 2:

                    # Close the secondary menu
                    GameSelectWin.close()

                    # Let the user play the two player version of Tic-Tac-Toe 
                    TicTacTwo(Decision2)
                    
                # Reopen the Secondary Menu
                GameSelectWin, OPlayRect, OPlayText, TPlayRect, TPlayText, BackRect, BackText, Decision2 = SecondaryMenu()
                        
        # Reopen the Main menu
        menu, PlayRect, PlayText, InstructText, InstructRect, ExitRect, ExitText, Decision = Menu()
        
# End main function    
main()
