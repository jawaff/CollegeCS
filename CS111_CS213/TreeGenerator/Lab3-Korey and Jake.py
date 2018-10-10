"""
Name: Korey Hill and Jake Waffle

File: Lab3-Korey and Jake.py

Description:

1. Significant Constants
    -PI (for the tree generation)

2. Inputs
    -NOTHING!

3. Computations
    -drawing a generic rectangle, circle and line
    -Generate a tree structure through recursion

4. Outputs
    -A house, a door, a person and some trees

"""
#turtlegraphics.py must be in the same directory as this script
from turtlegraphics import Turtle
from random import randint

from treeGenerator import growTree

class Shape(object):
    def __init__(self, turtle, color):
        """Initialize the variables needed for each shape."""
        self._turtle = turtle       #This stores the turtle object
        self._color = color         #storage of the color

    def getColor(self):
        """Returns the color of the shape."""
        return self._color

    def setColor(self, color):
        """Sets the color of the shape."""
        self._color = color

class Line(Shape):
    def __init__(self,turtle,color,x,y,x1,y1):
        """Initializes the derived shape, Line."""
        Shape.__init__(self, turtle,color)  #Initialize the inheritted class
        #Store variables
        self._x1 = x1
        self._x = x
        self._y1 = y1
        self._y = y
        
    def draw(self):
        """Draws the line that is represented by the stored variables."""
        # Color for line
        self._turtle.setColor(self._color[0],self._color[1],self._color[2])
        self._turtle.up() #Move without drawing
        self._turtle.move(self._x,self._y) #move to Coordinates
        self._turtle.down() #putting tail down to draw
        self._turtle.move(self._x1,self._y1)
        self._turtle.up()       
        

class Rectangle(Shape):
    def __init__(self, turtle, color, x, y, width, height):
        """Initialize the derived Rectangle shape."""
        Shape.__init__(self, turtle, color) #Initialize the inheritted class
        #Store variables
        self._x = x
        self._y = y
        self._width = width
        self._height = height
        
    def draw(self):
        """Draws a filled rectangle that is represented by the stored variables."""
        #There is only one turtle, so it needs updated to display each object's stored color
        self._turtle.setColor(self._color[0],self._color[1],self._color[2])
        #Filled in rectangle
        #For all y coordinates in a square, draw a horizontal line that goes across the square
        for y in xrange(self._y, self._y+self._height):
            self._turtle.up()
            #Move to the starting x position
            self._turtle.move(self._x,y)
            self._turtle.setDirection(0)
            self._turtle.down()
            #Draw a line equal in length to the width of the rectangle
            self._turtle.move(self._width)
        #Old outline for the rectangle
##        self._turtle.up()  #Move without drawing
##        self._turtle.move(self._x,self._y) #Move to (x, y)
##        self._turtle.setDirection(90)
##        self._turtle.down()
##        #Loop through two steps to eschew redundancy
##        for i in xrange(2):
##            self._turtle.move(self._height)    #Draw a side
##            self._turtle.turn(-90)  #Turn 90 degrees clockwise
##
##            self._turtle.move(self._width) #Draw a side
##            self._turtle.turn(-90)  #Turn 90 degrees clockwise
##            turtle.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
       
 
        
class Circle(Shape):
    def __init__(self, turtle, color, x, y, radius):
        """This constructor initializes variables and an inherited class that will be needed for each circle."""
        #Initialize the inherited object
        Shape.__init__(self, turtle, color)
        
        #(x,y) is the center of the circle
        self._x = x
        self._y = y
        self._radius = radius
        
    def draw(self):
        """Draws the circle that is represented by the stored variables."""
        #The circumference of the circle the user wants
        circumference = 2*3.14159*self._radius
        
        #Set up position
        self._turtle.up()
        self._turtle.move(self._x + self._radius, self._y)
        self._turtle.setDirection(90)
        self._turtle.down()
        
        #Draw the circle
        #120*3 = steps*lengthOfTurn(in degrees) = 360
        for i in xrange(120):
            self._turtle.move(circumference/120)
            self._turtle.turn(3)

        self._turtle.up()
            


def main():
    house = []  #A list containing all the primitives needed for drawing a house
    person = [] #A list containing all the primitives needed for drawing a person

    #Initialize the turtle
    paul = Turtle(900, 700)
    
    #Initializaing and appending objects that make up the house that we want to store into one list.
    #Initialize house1 and put into the according list
    house1 = Rectangle(paul, (randint(0,255), randint(0,255), randint(0,255)), -400, -200, 200, 200)   #House frame
    house.append(house1)    #Throw house1 into that list
    
    #Initialize house2 and put into the according list
    house2 = Rectangle(paul, (randint(0,255), randint(0,255), randint(0,255)), -350, -200, 40, 100)           #Door
    house.append(house2)
    
    house3 = Line(paul,(randint(0,255), randint(0,255), randint(0,255)),-400,0,-300,50)                    #roof left diag
    house.append(house3)
    
    house4 = Line(paul,(randint(0,255), randint(0,255), randint(0,255)),-200,0,-300,50)                       #roof right diag
    house.append(house4)

    #We don't need the list of coords returned by this func
    #Draw all the trees!!!!!!!!!!!!!!!!!!!!!!!!
    growTree(paul, -150, -200, 90, 9, 30, 300, 0, 0.5, 0)
    growTree(paul, 50, -200, 90, 9, 30, 300, 0, 0.5, 0)
    growTree(paul, 150, -200, 90, 9, 30, 300, 0, 0.5, 0)
    growTree(paul, 250, -200, 90, 9, 30, 300, 0, 0.5, 0)
    growTree(paul, 350, -200, 90, 9, 30, 300, 0, 0.5, 0)

    paul.setWidth(5)
    #Iterate through the house list
    for primitive in house:
        #Draw the current primitive
        primitive.draw()
    
    pers1 = Circle(paul, (randint(0,255), randint(0,255), randint(0,255)), 100, -130, 10)  #The head
    person.append(pers1)
    pers2 = Line(paul, (randint(0,255), randint(0,255), randint(0,255)), 100, -140, 100, -180)                 #The body line
    person.append(pers2)
    pers3 = Line(paul, (randint(0,255), randint(0,255), randint(0,255)), 80, -160, 100, -145)                 #larm
    person.append(pers3)
    pers4 = Line(paul, (randint(0,255), randint(0,255), randint(0,255)), 100, -145, 120, -160)                 #rarm
    person.append(pers4)
    pers5 = Line(paul, (randint(0,255), randint(0,255), randint(0,255)), 80, -200, 100, -180)                 #Left leg line
    person.append(pers5)
    pers6 = Line(paul, (randint(0,255), randint(0,255), randint(0,255)), 120, -200, 100, -180)                 #Right leg line
    person.append(pers6)
 
    #Iterate through the person list
    for primitive in person:
        #Draw the current Primitive
        primitive.draw()

main()
