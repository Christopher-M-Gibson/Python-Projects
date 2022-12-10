'''
    Skills used: Libraries, functions, nested loops, while loops, for loops,
    if-else statements
'''

# Import necessary libraries
from graphics import *
from random import *
from time import *

''' The PlayClicked function, which checks whether the Play Rectangle was
clicked'''
def PlayClicked(mouse, menu):
    if not mouse:
        return False
    mx, my = mouse.getX(), mouse.getY()
    x1, y1 = 75, 75
    x2, y2 = 225, 125
    return (x1 < mx < x2) and (y1 < my < y2)

''' The InstructClicked function, which checks whether the Instruct Rectangle
was clicked'''
def InstructClicked(mouse, menu):
    if not mouse:
        return False
    mx, my = mouse.getX(), mouse.getY()
    x1, y1 = 75, 150
    x2, y2 = 225, 200
    return (x1 < mx < x2) and (y1 < my < y2)

''' The ExitClicked function, which checks whether the Exit Rectangle was
clicked'''
def ExitClicked(mouse, menu):
    if not mouse:
        return False
    mx, my = mouse.getX(), mouse.getY()
    x1, y1 = 75, 225
    x2, y2 = 225, 275
    return (x1 < mx < x2) and (y1 < my < y2)
  
# The Menu function, which creates the menu
def Menu():

    # Create a 300 x 300 Graphics window with a dark grey background
    menu = GraphWin("Menu Window", 300, 300)
    menu.setBackground("light grey")

    # Create the heading
    Title = Text(Point(150, 30), "HANGMAN")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(menu)
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

    # Create the yellow Instructions Rectangle labelled "Instructions"
    InstructRect = Rectangle(Point(75, 150), Point(225, 200))
    InstructRect.setFill("yellow")
    InstructRect.draw(menu)
    InstructText = Text(Point(150, 175), "Instructions")
    InstructText.setSize(20)
    InstructText.setTextColor("black")
    InstructText.draw(menu)

    # Create the red Exit Rectangle labelled "Exit" 
    ExitRect = Rectangle(Point(75, 225), Point(225, 275))
    ExitRect.setFill("red")
    ExitRect.draw(menu)
    ExitText = Text(Point(150, 250), "Exit")
    ExitText.setSize(20)
    ExitText.setTextColor("black")
    ExitText.draw(menu)

    # Create a while loop that runs until exit rectangle is clicked
    mouse = menu.checkMouse()
    mouse == False
    while ExitClicked(mouse, menu) == False:
        mouse = menu.checkMouse()

        # If user clicks on Play, play the game
        if PlayClicked(mouse, menu) == True:
            Decision = 1
            return menu, PlayRect, PlayText, InstructRect, InstructText, ExitRect, ExitText, Decision

        # If user clicks on Instructions, open instructions
        if InstructClicked(mouse, menu) == True:
            Decision = 2
            return menu, PlayRect, PlayText, InstructRect, InstructText, ExitRect, ExitText, Decision
        
    # Exit the game
    Decision = 3
    menu.close()
    return menu, PlayRect, PlayText, InstructRect, InstructText, ExitRect, ExitText, Decision

''' The BackClicked function, which checks whether the Back Rectangle was
clicked'''
def BackClicked(mouse, InstructWin):
    if not mouse:
        return False
    mx, my = mouse.getX(), mouse.getY()
    x1, y1 = 50, 180
    x2, y2 = 200, 230
    return (x1 < mx < x2) and (y1 < my < y2)

# The Instructions function, which displays how to play the game 
def Instructions():

    # Draw in a 250 x 250 window with a light grey background
    InstructWin = GraphWin("Instructions", 250, 250)
    InstructWin.setBackground("light grey")

    # Create the heading
    Title = Text(Point(125, 30), "HANGMAN")
    Title.setStyle("bold")
    Title.setSize(25)
    Title.draw(InstructWin)
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

    # Create and draw in the instructions for the game 
    Instruct_List = ["In Hangman, a secret word is generated from",
                     "a list of over 58,000 words. The player is",
                     "to guess the word by inputting a letter that",
                     "they believe the word contains. However,",
                     "each wrong guess brings the user closer to",
                     "losing, as a hanging man is slowly drawn in."]
    ylevel1 = 75
    for i in range(6):
        HowTo = Text(Point(125, ylevel1), Instruct_List[i])
        HowTo.setSize(8)
        HowTo.draw(InstructWin)
        ylevel1 += 15

    # Create while loop that runs until Back rectangle is clicked
    mouse = InstructWin.checkMouse()
    mouse == False
    while BackClicked(mouse, InstructWin) == False:
        mouse = InstructWin.checkMouse()
    InstructWin.close()

# The Download function, which imports the list of possible solutions
def Download():
    file = "Hangman-Words.txt"
    infile = open(file, "r", encoding = 'utf8')
    AnsList = []

    # While loop that reads each line of the file and adds it to the list 
    line = infile.readline()
    while line != "":
        line = line.replace("\n", "")
        line = line.lower()
        AnsList.append(line)
        line = infile.readline()

    # Close the file and end the function
    infile.close() 
    return AnsList

# The Pickword() function, which picks the solution from the list
def Pickword(AnsList):
    Answer = choice(AnsList)
    return Answer

''' The Clicked1_2 function, which checks whether any letter in the first two
rows was clicked'''
def Clicked1_2(mouse, board):
    if not mouse:
        return False
    mx, my = mouse.getX(), mouse.getY()
    x1, y1 = 0, 580
    x2, y2 = 600, 700
    return (x1 < mx < x2) and (y1 < my < y2)

''' The Clicked3 function, which checks whether any letter in the third row was
clicked'''
def Clicked3(mouse, board):
    if not mouse:
        return False
    mx, my = mouse.getX(), mouse.getY()
    x1, y1 = 120, 700
    x2, y2 = 480, 760
    return (x1 < mx < x2) and (y1 < my < y2)
    
'''The DrawDash function, which draws the correct number of dashes for the word
that needs to be solved'''
def DrawDash(Answer, board):

    # Find the length of the word and how many dashes are to be drawn
    Length = len(Answer)
    if (Length % 2)  == 0:
        HalfLen = Length // 2
        Start = 297 - (HalfLen*(20) + (HalfLen - 1)*(6))
    elif (Length % 2) != 0:
        HalfLen = (Length - 1) // 2
        Start = 290 - ((HalfLen*(20) + (HalfLen*(6))))

    # Use a for loop to draw in the dashes
    CenterList = []
    for i in range(0,Length):
        Dash = Line(Point(Start, 535), Point(Start+20, 535))
        Center = Start + 10
        CenterList.append(Center)
        Dash.setWidth(3)
        Dash.draw(board)
        Start += 26
    return CenterList                                  

# The FindGuess function, which determines what letter was guessed 
def FindGuess(mx, my):
    if (0<mx<60) and (580<my<640):
        Guess = "A"
        c1x, c1y = 0, 580
        c2x, c2y = 60, 640
    elif (60<mx<120) and (580<my<640):
        Guess = "B"
        c1x, c1y = 60, 580
        c2x, c2y = 120, 640
    elif (120<mx<180) and (580<my<640):
        Guess = "C"
        c1x, c1y = 120, 580
        c2x, c2y = 180, 640
    elif (180<mx<240) and (580<my<640):
        Guess = "D"
        c1x, c1y = 180, 580
        c2x, c2y = 240, 640
    elif (240<mx<300) and (580<my<640):
        Guess = "E"
        c1x, c1y = 240, 580
        c2x, c2y = 300, 640
    elif (300<mx<360) and (580<my<640):
        Guess = "F"
        c1x, c1y = 300, 580
        c2x, c2y = 360, 640
    elif (360<mx<420) and (580<my<640):
        Guess = "G"
        c1x, c1y = 360, 580
        c2x, c2y = 420, 640
    elif (420<mx<480) and (580<my<640):
        Guess = "H"
        c1x, c1y = 420, 580
        c2x, c2y = 480, 640
    elif (480<mx<540) and (580<my<640):
        Guess = "I"
        c1x, c1y = 480, 580
        c2x, c2y = 540, 640
    elif (540<mx<600) and (580<my<640):
        Guess = "J"
        c1x, c1y = 540, 580
        c2x, c2y = 600, 640
    elif (0<mx<60) and (640<my<700):
        Guess = "K"
        c1x, c1y = 0, 640
        c2x, c2y = 60, 700
    elif (60<mx<120) and (640<my<700):
        Guess = "L"
        c1x, c1y = 60, 640
        c2x, c2y = 120, 700
    elif (120<mx<180) and (640<my<700):
        Guess = "M"
        c1x, c1y = 120, 640
        c2x, c2y = 180, 700
    elif (180<mx<240) and (640<my<700):
        Guess = "N"
        c1x, c1y = 180, 640
        c2x, c2y = 240, 700
    elif (240<mx<300) and (640<my<700):
        Guess = "O"
        c1x, c1y = 240, 640
        c2x, c2y = 300, 700
    elif (300<mx<360) and (640<my<700):
        Guess = "P"
        c1x, c1y = 300, 640
        c2x, c2y = 360, 700
    elif (360<mx<420) and (640<my<700):
        Guess = "Q"
        c1x, c1y = 360, 640
        c2x, c2y = 420, 700
    elif (420<mx<480) and (640<my<700):
        Guess = "R"
        c1x, c1y = 420, 640
        c2x, c2y = 480, 700
    elif (480<mx<540) and (640<my<700):
        Guess = "S"
        c1x, c1y = 480, 640
        c2x, c2y = 540, 700
    elif (540<mx<600) and (640<my<700):
        Guess = "T"
        c1x, c1y = 540, 640
        c2x, c2y = 600, 700
    elif (120<mx<180) and (700<my<760):
        Guess = "U"
        c1x, c1y = 120, 700
        c2x, c2y = 180, 760
    elif (180<mx<240) and (700<my<760):
        Guess = "V"
        c1x, c1y = 180, 700
        c2x, c2y = 240, 760
    elif (240<mx<300) and (700<my<760):
        Guess = "W"
        c1x, c1y = 240, 700
        c2x, c2y = 300, 760
    elif (300<mx<360) and (700<my<760):
        Guess = "X"
        c1x, c1y = 300, 700
        c2x, c2y = 360, 760
    elif (360<mx<420) and (700<my<760):
        Guess = "Y"
        c1x, c1y = 360, 700
        c2x, c2y = 420, 760
    elif (420<mx<480) and (700<my<760):
        Guess = "Z"
        c1x, c1y = 420, 700
        c2x, c2y = 480, 760
    return Guess, c1x, c1y, c2x, c2y

# The Evaluate function, which determines the outcome of the guess 
def Evaluate(Guess, Answer, board, CenterList):

    # Initialize variables
    AnsSpl = list(Answer)
    In_Word = "NO"
    TrialCount = 0
    CorrectCount = 0
    
    # Determine if the guessed letter matches each letter of the solution
    for i in range(0, len(AnsSpl)):
        if Guess.lower() == AnsSpl[i]:
            Center = CenterList[i]
            CorrectCount += 1
            Index = Text(Point(CenterList[i], 522), Guess)
            Index.setSize(16)
            Index.draw(board)
            In_Word = "YES"

    # Determine the result of the individual trial 
    if In_Word == "YES":
        TrialCount = 0
    else:
        TrialCount = 1
    return TrialCount, CorrectCount

# The BodyDraw function, which draws a body part if a guess is wrong
def BodyDraw(board, Miss_Count):

    # Initialize variables
    AlreadyDrawn = ["NO", "NO", "NO", "NO", "NO", "NO", "NO"]
    ErrorNum = Miss_Count - 1

    # If statements depending on if the body part is already drawn in 
    if AlreadyDrawn[ErrorNum] == "YES":
        return
    else:

        # First wrong guess --> draw the gallows
        if ErrorNum == 0:
            Noose = Line(Point(300, 70), Point(300, 110))
            Noose.setWidth(7)
            Noose.draw(board)
            TopBar = Line(Point(150, 75), Point(300, 75))
            TopBar.setWidth(10)
            TopBar.draw(board)
            VertBar = Line(Point(155, 70), Point(155, 470))
            VertBar.setWidth(10)
            VertBar.draw(board)
            DTopBar = Line(Point(190, 74), Point(154, 110))
            DTopBar.setWidth(10)
            DTopBar.draw(board)
            DBottomBar = Line(Point(190, 466), Point(154, 430))
            DBottomBar.setWidth(10)
            DBottomBar.draw(board)
            BottomBar = Line(Point(150, 465), Point(450, 465))
            BottomBar.setWidth(10)
            BottomBar.draw(board)
            AlreadyDrawn[0] = "YES"

        # Second wrong guess --> Draw the head
        elif ErrorNum == 1:
            Head = Circle(Point(300, 140), 30)
            Head.setFill("yellow")
            Head.draw(board)
            EyeL = Text(Point(290, 133), "X")
            EyeR = Text(Point(310, 133), "X")
            EyeL.draw(board)
            EyeR.draw(board)
            Mouth = Line(Point(293, 155), Point(307, 155))
            Mouth.draw(board)
            AlreadyDrawn[1] = "YES"

        # Third wrong guess --> Draw the torso
        elif ErrorNum == 2:
            Body = Line(Point(300, 170), Point(300, 320))
            Body.setWidth(4)
            Body.draw(board)
            AlreadyDrawn[2] = "YES"

        # Fourth wrong guess --> Draw the right arm
        elif ErrorNum == 3:
            ArmR = Line(Point(300, 185), Point(240, 210))
            ArmR.setWidth(3)
            ArmR.draw(board)
            HandR = Circle(Point(242, 211), 10)
            HandR.setFill("yellow")
            HandR.draw(board)
            AlreadyDrawn[3] = "YES"

        # Fifth wrong guess --> Draw the left arm
        elif ErrorNum == 4:
            ArmL = Line(Point(300, 185), Point(360, 210))
            ArmL.setWidth(3)
            ArmL.draw(board)
            HandL = Circle(Point(358, 211), 10)
            HandL.setFill("yellow")
            HandL.draw(board)
            AlreadyDrawn[4] = "YES"

        # Sixth wrong guess --> Draw the right leg
        elif ErrorNum == 5:
            LegR = Line(Point(300, 320), Point(250, 400))
            LegR.setWidth(4)
            LegR.draw(board)
            FootR = Circle(Point(245, 403), 15)
            FootR.setFill("yellow")
            FootR.draw(board)
            AlreadyDrawn[5] = "YES"

        # Seventh wrong guess --> Draw the left leg
        elif ErrorNum == 6:
            LegL = Line(Point(300, 320), Point(350, 400))
            LegL.setWidth(4)
            LegL.draw(board)
            FootL = Circle(Point(355, 403), 15)
            FootL.setFill("yellow")
            FootL.draw(board)
            AlreadyDrawn[6] = "YES"

    return

# The Popup function, which draws the Pop up at the end of the game
def Popup(board, TextSet, Answer, Miss_Count):

    # Draw in a colored rectange (color depends on outcome)
    if (TextSet == 2):
        RectColor = "red"
    else:
        RectColor = "green"
    PopupRect = Rectangle(Point(100, 150), Point(500, 350))
    PopupRect.setFill(RectColor)
    PopupRect.draw(board)

    # Draw in header for rectangle (depends on outcome)
    if (TextSet == 2):
        HeaderText = "YOU LOSE"
    else:
        HeaderText = "CONGRATS!"
    Header = Text(Point(300, 180), HeaderText)
    Header.setStyle("bold")
    Header.setSize(22)
    Header.draw(board)

    # Draw in text of rectangle (depends on outcome)
    if (TextSet == 2):
        Line_Text1 = "The man has sadly been hung"
        Line_Text2 = "The word you failed to form was:"
        Line_Text3 = Answer.upper()
    else:
        Line_Text1 = "You have saved the man!"
        Line_Text2 = "The man is forever grateful"
        Line_Text3 = ""
    TextLine1 = Text(Point(300, 215), Line_Text1)
    TextLine1.setStyle("bold")
    TextLine1.setSize(18)
    TextLine1.draw(board)
    TextLine2 = Text(Point(300, 245), Line_Text2)
    TextLine2.setStyle("bold")
    TextLine2.setSize(18)
    TextLine2.draw(board)
    TextLine3 = Text(Point(300, 275), Line_Text3)
    TextLine3.setStyle("bold")
    TextLine3.setSize(18)
    TextLine3.draw(board)
    TextLine4 = Text(Point(300, 320), "Click anywhere to dismiss")
    TextLine4.setStyle("bold")
    TextLine4.setStyle("italic")
    TextLine4.setSize(18)
    TextLine4.draw(board)

    # Once the user clicks on the board, undraw everything
    board.getMouse()
    PopupRect.undraw()
    Header.undraw()
    TextLine1.undraw()
    TextLine2.undraw()
    TextLine3.undraw()
    return

# The makeGame function, which creates the game 
def makeGame(Answer, AnsList):

    # Create a 600 x 785 Graphics window with a white background
    board = GraphWin("Hangman", 600, 785)
    board.setBackground("white")

    # Create the header
    Title = Text(Point(300, 35), "HANGMAN")
    Title.setStyle("bold")
    Title.setSize(30)
    Title.draw(board)
    TBar = Line(Point(0,60), Point(600, 60))
    TBar.setWidth(3)
    TBar.draw(board)

    # Create the rectangle where that will display the hanging man
    PictureRect = Rectangle(Point(150, 70), Point(450, 470))
    PictureRect.draw(board)

    # Call the DrawDash function to draw in the spaces for the answer's letters 
    CenterList = DrawDash(Answer, board)
    
    # Create the space where all the potential guesses will be
    # Use a for loop to create the 4 horizontal lines
    HBarList = []
    ylevel = 580
    for i in range(0,4):
        GridHBar = Line(Point(0, ylevel), Point(600, ylevel))
        GridHBar.setWidth(3)
        GridHBar.draw(board)
        HBarList.append(GridHBar)
        ylevel += 60

    # Use a for loop to create the 9 vertical lines
    VBarList = []
    xlevel = 60
    for i in range(0,9):
        GridVBar = Line(Point(xlevel, 580), Point(xlevel, 760))
        GridVBar.setWidth(3)
        GridVBar.draw(board)
        VBarList.append(GridVBar)
        xlevel += 60

    # Draw two black rectangles in the last row
    BRect1 = Rectangle(Point(0, 700), Point(120, 760))
    BRect1.setFill("black")
    BRect1.draw(board)
    BRect2 = Rectangle(Point(480, 700), Point(600, 760))
    BRect2.setFill("black")
    BRect2.draw(board)
    
    # Write a note at the bottom of the screen
    NoteTextList = ["To make a guess, click on one of the letters above."]
    Note = Text(Point(300, 772), NoteTextList[0])
    Note.setStyle("italic")
    Note.setSize(10)
    Note.draw(board)

    # Initialize the number of misses
    Miss_Count = 0
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

    # Draw the letters into their respective slots
    X_Coor_1_2 = 30
    X_Coor_3 = 150
    for i in range(0,10):
        Letter1 = Text(Point(X_Coor_1_2, 610), Alphabet[i])
        Letter1.setSize(17)
        Letter1.draw(board)
        Letter2 = Text(Point(X_Coor_1_2, 670), Alphabet[i+10])
        Letter2.setSize(17)
        Letter2.draw(board)
        X_Coor_1_2 += 60
    for i in range(0,6):
        Letter3 = Text(Point(X_Coor_3, 730), Alphabet[i+20])
        Letter3.setSize(17)
        Letter3.draw(board)
        X_Coor_3 += 60
        
    # Initialize variables
    mouse = board.checkMouse()
    mouse == False
    Guessed = []
    CorrectTotal = 0
    
    # Use while loop to run until 7 attempts have been reached
    while Miss_Count < 7:
        mouse = board.getMouse()
        
        # Use while loop to run until a guess is made
        while (Clicked1_2(mouse, board) == False) and (Clicked3(mouse,board) == False):
            mouse = board.getMouse()

        # Determine the user's guess
        mx, my = mouse.getX(), mouse.getY()
        Guess, c1x, c1y, c2x, c2y = FindGuess(mx, my)

        # Case for when a guess is repeated
        if Guess in Guessed:
            Miss_Count += 0

        # In all other cases,
        else:

            # Run the Evaluate() function to evaluate the guess
            TrialCount, CorrectCount = Evaluate(Guess, Answer, board, CenterList)

            # Draw in the white rectangle over the guessed letter
            WhiteOut = Rectangle(Point(c1x+1, c1y+1), Point(c2x-1, c2y-1))
            WhiteOut.setFill("white")
            WhiteOut.draw(board)
            
            # Sum/append necessary values
            Miss_Count += TrialCount
            Guessed.append(Guess)
            
            # Determine if a body part needs to be drawn 
            if Miss_Count > 0:
                BodyDraw(board, Miss_Count)

        # Update the total amount of correct guesses
        CorrectTotal += CorrectCount
        
        # If the player obtains the correct word,
        if CorrectTotal == len(Answer):
            sleep(1)
            TextSet = 1
            Popup(board, TextSet, Answer, Miss_Count)
            break

    # If the user has lost the game,
    if Miss_Count == 7:
        sleep(1)
        TextSet = 2
        Popup(board, TextSet, Answer, Miss_Count)

    # Close the window
    board.close()            

def main():

    # Display the main menu
    menu, PlayRect, PlayText, InstructText, InstructRect, ExitRect, ExitText, Decision = Menu()

    # Download the word list
    AnsList = Download()
    
    # While loop that runs until the user clicks exit
    while Decision != 3:

        # If the user clicks on the isntructions rectangle,
        if Decision == 2:
            menu.close()
            Instructions()

        # If the user clicks on the Play Rectangle,
        if Decision == 1:
            menu.close()
            Answer = Pickword(AnsList)
            makeGame(Answer, AnsList)
            
        # Reopen the main menu
        menu, PlayRect, PlayText, InstructText, InstructRect, ExitRect, ExitText, Decision = Menu()
           
main()
