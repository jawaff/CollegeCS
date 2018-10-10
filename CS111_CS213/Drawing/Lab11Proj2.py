"""
Authors: BreAnne Baird, Matthew Steele, Jacob Waffle
Program: Ch7 Project 7

Making random colored lines
Constants
    My turtle?
Inputs
    level
    xy1
    xy2
Computations
    Calculating the xm ym for the fractal
Display
    FRACTAL PICTURE!

"""

from turtlegraphics import Turtle
import random, pdb

def drawLine(turtle, x1, y1, x2, y2):
    '''Draw randomly colored line given the arguments'''
    turtle.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.up()
    turtle.move(x1,y1)
    turtle.down()
    turtle.move(x2,y2)

def fractal(turtle, x1, y1, x2, y2, level):
    '''Recursive function used for making a fractal'''
    if level == 0:
        drawLine(turtle, x1,y1,x2,y2)
    else:
        xm = (x1 + x2 + y1 - y2) / 2
        ym = (y1 + y2 + x2 - x1) / 2
        fractal(turtle, x1, y1, xm, ym, level-1)
        fractal(turtle, xm, ym, x2, y2, level-1)

def main():
    paul = Turtle(1024, 768)
    level = raw_input("Please enter a level for the fractals: ")
    gewd = False
    while not gewd:
        if not level.isalpha() and int(level) >= 0:
            print "Thanks for the correct input, bro."
            gewd = True
        else:
            level = raw_input("Enter a NUMBER that is greater than or equal to zero: ")
    xy1 = raw_input("Please enter an x and y coordinate with ONLY a space inbetween them: ")
    xy2 = raw_input("Now do the same thing for another coordinate: ")
    gewd = False
    while not gewd:
        xy1L = xy1.split()
        xy2L = xy2.split()
        if len(xy1L) == 2 and len(xy2L) == 2:
            gewd = True
        else:
            xy1 = raw_input("Please enter correct coordinates with a space inbetween: ")
            xy2 = raw_input("Now do the same thing for another coordinate: ")

    paul.setWidth(1)

    fractal(paul, int(xy1L[0]), int(xy1L[1]), int(xy2L[0]), int(xy2L[1]), int(level))
    raw_input("Press enter to exit!")
main()
