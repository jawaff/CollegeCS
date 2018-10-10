'''
Author: BreAnne Baird, Matthew Steele, Jacob Waffle
Program Ch7 project 3

Triangle fractal displayyyyyyy
constants
    PI
Inputs
    level
    distance
computations
    Calculating coordinates given a point, distance and angle
Display
    A fractal picture
'''
from turtlegraphics import Turtle
import random, math

PI = 3.14159265
#pdb.set_trace()
def drawLine(turtle, x1, y1, distance, angle):
    """Draw a line given a point, the distance of the line and the angle at which it is to be drawn."""
    turtle.setColor(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    turtle.up()
    turtle.move(x1,y1)
    turtle.down()
    turtle.setDirection(angle)
    turtle.move(distance)

def getOffset(x1, y1, angle, distance):
    '''Takes in an angle a distance and a point and returns the offset'''
    angle = angle%360
    #x = 0
    #y = 0
    x = (distance*(math.sin((90-angle)*PI/180)))
    y = (distance*(math.sin(angle*PI/180)))
    '''
    if angle < 90:
        angle = angle%90
        x = (distance*(math.sin((90-angle)*PI/180)))
        y = (distance*(math.sin(angle*PI/180)))

    elif angle < 180:
        angle = angle%90
        y = (distance*(math.sin((90-angle)*PI/180)))
        x = -1*(distance*(math.sin(angle*PI/180)))
        
    elif angle < 270:
        angle = angle%90
        x = -1*(distance*(math.sin((90-angle)*PI/180)))
        y = -1*(distance*(math.sin(angle*PI/180)))
        
    else:
        angle = angle%90
        y = -1*(distance*(math.sin((90-angle)*PI/180)))
        x = (distance*(math.sin(angle*PI/180)))
    '''
    #Adding offsets to first points to get second ones
    y += y1
    x += x1
    return x, y

def fractal(turtle, x1, y1, distance, angle, level):
    """Recursive function that results with a "side" of the fractal triangle"""
    if level == 0:
        drawLine(turtle, x1,y1,distance,angle)
    else:
        #pdb.set_trace()
        #getting the offsets for the four lines
        x2,y2 = getOffset(x1, y1, angle, distance/3)
        x3,y3 = getOffset(x2, y2, angle+60, distance/3)
        x4,y4 = getOffset(x3, y3, angle-60, distance/3)

        #Using the four points that were just calculated, recursively call fractal()
        fractal(turtle, x1, y1, distance/3, angle, level-1)
        fractal(turtle, x2, y2, distance/3, angle+60, level-1)
        fractal(turtle, x3, y3, distance/3, angle-60, level-1)
        fractal(turtle, x4, y4, distance/3, angle, level-1)

def main():
    """Gathering input and making the computer do stuff."""
    paul = Turtle(1024, 768)
    level = raw_input("Please enter a level for the fractals: ")
    distance = raw_input("Please enter a distance for your lines: ")
    gewd = False
    while not gewd:
        if not level.isalpha() and int(level) >= 0:
            if not distance.isalpha() and int(distance) >= 0:
                print "Thanks for the correct input, bro."
                gewd = True
            else:
                distance = raw_input("Enter a NUMBER that is greater than or equal to zero(talking about distance here): ")
        else:
            level = raw_input("Enter a NUMBER that is greater than or equal to zero(talking about level here): ")

    distance=float(distance)
    paul.setWidth(1)
    
    x = distance / 2.0
    y = -1*((distance*(math.sin(60)))/(math.sin(90))-distance/1.9)/2.0

    fractal(paul, -1*x, y, distance, 0, int(level))
    fractal(paul, (-1*x)+distance, y, distance, -120, int(level))
    fractal(paul, 0, -1*y, distance, 120, int(level))
    
    raw_input("Press enter to exit!")
main()
