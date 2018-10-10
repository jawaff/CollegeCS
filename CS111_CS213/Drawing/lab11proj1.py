'''
Programmer: Jake Waffle
            BreAnne Baird
            Matt Steele
            
            
Created on Apr 19, 2012

drawing a circle with inputed radius and center point

Constants:  numSide: the number of sides of the polygon to make it look like a circle, less will start looking like a n-polygon

Variables:  radius, centY, centX, numSide, moveSeg

computations: compute moveSeg or the length of each of the 120 sides.
                (2*(pi)*radius)/numSide   circumference of a circle
                
inputs:     radius:     radius of a circle
            centX:      x-coord of center point
            centY:      y-coord of center point

outputs:    draws a circle at the required coordinates with a user provided radius
'''
from turtlegraphics import Turtle
from math import pi
# constants

numSide = 120
def drawCircle(turtle,radius,centerX,centerY):
    #move to center point without drawing
    turtle.up()
    turtle.move(centerX,centerY)
    #set direction to east
    turtle.setDirection(0)
    #move to initial drawing point and orient perpendicular to first radius move
    turtle.move(radius)
    turtle.down()#pen down/tail down
    turtle.setDirection(90)
    #computation of length of move
    moveSeg = 2.0 * pi * radius / numSide
    for each in xrange(numSide):
        turtle.move(moveSeg)
        turtle.turn(360/numSide)
        
        
        
    return

    
def main():
    
    #inputs
    radius1 = "alpha"
    centX1 = "alpha"
    centY1 = "alpha"
    
    #input error checking
    while radius1.isalpha() == True:
        radius1 = raw_input("Radius of the circle: ")
        if radius1.isdigit() == True:
            radius = int(radius1)
    
        elif radius1.isalpha() != True and radius1.isdigit != True:
            radius1 = "alpha" #catches the non-alpha, non-digit characters
            
    while centX1.isalpha() == True:
        centX1 = raw_input("X-coordinate of the center point.")
        if centX1.isdigit() == True:
            centX = int(centX1)
    
        elif centX1.isalpha() != True and centX1.isdigit != True:
            centX1 = "alpha"
            
    while centY1.isalpha() == True:
        centY1 = raw_input("Y-coordinate of the center point.")
        if centY1.isdigit() == True:
            centY = int(centY1)
    
        elif centY1.isalpha() != True and centY1.isdigit != True:
            centY1 = "alpha"
    
    
    
    
    
    #assign Turtle to t and set the the window to 500X600
    t = Turtle(500,600)
    t.setWidth(1)
    drawCircle(t,radius,centX,centY)
    # just to keep the window open
    raw_input("enter to continue")
main()
