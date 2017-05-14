from random import randrange
from graphics import *

'''
Jayser Mendez - Extra Credit Assignment.

Write a program to play “Three Button Monte.” Your program should draw
three buttons labeled “Door 1”, “Door 2,” and “Door 3” in a window and
randomly select one of the buttons (without telling the user which one
is selected). The program then prompts the user to click on one of the
buttons.

A click on the special button is a win, and a click on one of
the other two is a loss. You should tell the user whether they won or
lost, and in the case of a loss, which was the correct button.Your
program should be entirely graphical; that is, all prompts
and messages should be displayed in the graphics window.   
'''

class Door:
    
    def __init__(self, win, center, width, height, text):
        '''
        Class to create Door object.
        '''

        # isClicked and isSecret should start as false.
        # The program will activate it depending on the state.
        self.isSecret = False
        self.isClicked = False

        # Colors to use on the program.
        self.gray = color_rgb(224,224,224)
        self.blue = color_rgb(0,128,255)
        self.red = color_rgb(234,53,65)
        self.green = color_rgb(51,229,70)

        # Get points of door center and calculate
        # min and max points of given center.
        x = center.getX()
        y = center.getY()
        self.xMin = x - (width / 2)
        self.xMax = x + (width / 2)
        self.yMin = y - (height / 2)
        self.yMax = y + (height / 2)
         
        # Create the door object based on a rectangle
        self.door = Rectangle(Point(self.xMin,self.yMax),
                              Point(self.xMax,self.yMin))
        
        self.door.setFill(self.blue)
        self.door.setWidth(0)
        self.door.draw(win)
         
        # Create the knob of the door.
        # X is the center of the door, but the knob is not at
        # the center. So, compensate it by adding ten
        self.doorKnob = Circle(Point(x+10 , y), 2.5)
        self.doorKnob.setFill(self.gray)
        self.doorKnob.setWidth(0)
        self.doorKnob.draw(win)
         
        # Create sign for door object
        p1 = self.door.getP1()
        p2 = self.door.getP2()
        x1 = p1.getX() + 2 # Add margin of 2
        y1 = p1.getY() - 2
        x2 = p2.getX() - 2 # Remove margin of 2 to compensate left side
        y2 = p2.getY() + 40 # Arbitary choosen (may not work with other door
                            # size)
        
        self.sign = Rectangle(Point(x1 , y1), Point(x2 ,y2))
        self.sign.setFill(self.gray)
        self.sign.setWidth(0)
        self.sign.draw(win)
         
        # Create label for sign on door.
        self.label = Text(self.sign.getCenter(), text)
        self.label.setSize(17)
        self.label.draw(win)
         
     
    def makeSecret(self):
        '''
        Funtion to set the door as secret.
        '''
        self.isSecret = True
         
     
    def fillGreen(self):
        '''
        Make correct door green meaning that it is the correct one.
        '''
        
        self.door.setFill(self.green)
        
             
    def fillRed(self):
        '''
        Make correct door red meaning that it is the incorrect one.
        '''
        self.door.setFill(self.red)
         

    def onClick(self,p):

        if (self.xMin <= p.getX() <= self.xMax
            and self.yMin <= p.getY() <= self.yMax):
            
            self.isClicked = True
            return True
        
        return False
    
     
    def openDoor(self):
        '''
        Function to reveal the secret door.
        '''
         
        if self.isSecret == True and self.isClicked == True:
            self.fillGreen()
            return True
         
        elif self.isSecret == False and self.isClicked == True:
            self.fillRed()
         
        elif self.isSecret == True and self.isClicked == False:
            self.fillGreen()
            return False
        
class Button:

    def __init__(self, win, name, x1, y1, x2, y2):

        self.p1 = (x1, y1)
        self.p2 = (x2, y2)

        self.B = Rectangle(Point(x1,y1), Point(x2,y2))
        self.B.draw(win)

        self.T = Text(self.B.getCenter(), name)
        self.T.draw(win)

        self.TurnInactive()

    def Clicked(self, pt):
        x = pt.getX()
        y = pt.getY()
        x1 = self.p1[0]
        y1 = self.p1[1]
        x2 = self.p2[0]
        y2 = self.p2[1]
        
        V = x1 <= x <= x2 and y1 <= y <= y2
        return V

    def changeColor(self, color):
        self.B.setFill(color)

    def textSize(self, size):
        self.T.setSize(size)

    def Undraw(self):
        self.B.undraw()
        self.T.undraw()

    def TurnActive(self):
        self.state = "active"
        self.B.setFill('darkgrey')
        self.B.setWidth(2)
        
    def TurnInactive(self):
        self.state = "inactive"
        self.B.setFill('lightgrey')
        self.B.setWidth(1)
        
class Game:

    def __init__(self):
        self.wins = 0
        self.looses = 0

    def incrementWins(self):
        self.wins += 1
        return self.wins
    

    def incrementLooses(self):
        self.looses += 1
        return self.looses
    

    def getLooses(self):
        return self.looses
    

    def getWins(self):
        return self.wins
    

    def secretDoor(self, door1, door2, door3):
     
        x = randrange(1,4)
     
        if x == 1:
            door1.makeSecret()
            
        elif x == 2 :
            door2.makeSecret()
            
        else:
            door3.makeSecret()
            

    def getInput(self, win, door1, door2, door3):
        
        p = win.getMouse()
      
        while (not door1.onClick(p)
               and not door2.onClick(p)
               and not door3.onClick(p)):
            
            p = win.getMouse()

    def getResults(self, err, door1 ,door2 ,door3):

        open1 = door1.openDoor()
        open2 = door2.openDoor()
        open3 = door3.openDoor()

        # Check if the selected door is the correct one.
        if open1 == True or open2 == True or open3 == True:
            err.setText('Cheers! That is the correct door! :)')
            self.incrementWins()
     
        else:
            if open1 == False:
                correctExit = '1'
            
            elif open2 == False:
                correctExit = '2'
            
            else:
                correctExit = '3'
              
            err.setText(
                "Looser! the correct door is exit {}!".format(correctExit)
                )
            self.incrementLooses()
    
            
def main():

    # Create main windows
    win = GraphWin('Three Button Monte - Extra Credit',690,600)
    win.setCoords(0,0,130,100)
    win.setBackground('white')

    # Create top title
    introTop = Text(Point(65,95),'Jayser Mendez - Extra Credit')
    introTop.setSize(17)
    introTop.draw(win)

    # Initialize the class Game
    game = Game()
    
    a = True
    while a == True:
        
        # Generate doors
        door1 = Door(win,Point(25,60),30,53,'Exit 1')
        door2 = Door(win,Point(65,60),30,53,'Exit 2')
        door3 = Door(win,Point(105,60),30,53,'Exit 3')

        # Create scoreboard 
        winsTxt = Text(Point(15, 90), "Wins: {}".format(game.getWins()))
        winsTxt.setSize(18)
        winsTxt.draw(win)

        looseTxt = Text(Point(105, 90), "Looses: {}".format(game.getLooses()))
        looseTxt.setSize(18)
        looseTxt.draw(win)
     
        # Create down title box
        introDown = Rectangle(Point(0,25),Point(131,9))
        introDown.setFill(color_rgb(224,224,224))
        introDown.setWidth(0)
        introDown.draw(win)

        # Create Instructions
        intro = Text(Point(65,17),'Tap the correct door to exit the stage :)')
        intro.setSize(18)
        intro.draw(win)

        game.secretDoor(door1, door2, door3)
        game.getInput(win, door1 ,door2 , door3)
        game.getResults(intro, door1 ,door2 , door3)

        # Update scoreboard
        winsTxt.setText("Wins: {}".format(game.getWins()))
        looseTxt.setText("Looses: {}".format(game.getLooses()))

        # Menu buttons
        retryBtn = Button(win, "Try Again", 35, 6, 60, 12)
        retryBtn.changeColor(color_rgb(0,128,255))
        retryBtn.textSize(18)
        
        quitBtn = Button(win, "Exit", 70, 6, 96, 12)
        quitBtn.changeColor(color_rgb(234,53,65))
        quitBtn.textSize(18)

        loop = True

        while loop == True:

            p = win.getMouse()
            
            if retryBtn.Clicked(p):
                winsTxt.undraw()
                looseTxt.undraw()
                retryBtn.Undraw()
                quitBtn.Undraw()
                loop = False
                break
            
            elif quitBtn.Clicked(p):
                win.close()
                

if __name__ == '__main__':
    main()

else:
    ''
