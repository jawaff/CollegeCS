'''
Author:Jacob Waffle, Carey Stirling
Program:Ch7 project4

Generating a piece of art
Constants
    width
    height
Inputs
    level
Compute
    pattern() directs the drawing of the squares
Display
    Shows the generated picture
'''
from turtlegraphics import Turtle
import random

def fillSquare(turtle, oldX, oldY, width, height):
    '''An abstract function for drawing a filled in square!'''
    #Random colors!
    turtle.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    #The arguments should be floats because of the division of stuff
    oldY = int(oldY)
    oldX = int(oldX)
    height = int(height)
    width = int(width)
    #For all of the y points implied by arguments
    for y in xrange(oldY, oldY-height,-1):
        turtle.up()
        #Move to the starting x position
        turtle.move(oldX,y)
        turtle.setDirection(0)
        turtle.down()
        #Draw a line equal in length to the width of the rectangle
        turtle.move(width)

def pattern(turtle, x, y, width, height, level):
    '''The recursive function that directs the drawing of the pretty squares!'''
    if level > 0:
        #Not done yet
        pattern(turtle,x+(width/3)-1,y-(height/3), 2*(width/3)+1, 2*(height/3), level -1)
        
    if level%2 == 0:
        #Horizontal dominance
        fillSquare(turtle,x,y,width/3,height)
        fillSquare(turtle,x,y,width,height/3)
        
    else:
        #Vertical dominance
        fillSquare(turtle,x,y,width,height/3)
        fillSquare(turtle,x,y,width/3,height)
    
def main():
    width = 1024
    height = 768
    paul = Turtle(width, height)
    level = raw_input("Enter a level: ")
    fillSquare(paul,-512.0, 384.0, 1024.0, 768.0)
    pattern(paul, -512.0, 384.0, 1024.0, 768.0, level)
    raw_input("Press enter to exit: ")
main()
