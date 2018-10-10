from random import randint, uniform, shuffle
from turtlegraphics import Turtle
from math import fabs, ceil, cos, sin

PI = 3.14159

def drawRect(turtle, x, y, width, height, rgb):
    #There is only one turtle, so it needs updated to display each object's stored color
    turtle.setColor(rgb[0],rgb[1],rgb[2])
    #Filled in rectangle
    #For all y coordinates in a square, draw a horizontal line that goes across the square
    for yIter in xrange(y, y+height):
        turtle.up()
        #Move to the starting x position
        turtle.move(x,yIter)
        turtle.setDirection(0)
        turtle.down()
        #Draw a line equal in length to the width of the rectangle
        turtle.move(width)

def recursDraw(turtle, x, y, angle, width, height, curRGB, colorStep, endRGB):
    #______________________________________________
    #turtle - This is supposed to be an instance of class Turtle
    #x, y - These are the coordinates of the square being drawn.
    #width and height - These are the width and height of the square being drawn.
    #angle - This is the direction the flare is going -- the direction the next square needs drawn in.
    #rgb - The color of the square being drawn.
    #colorStep - The rate of change of the color in rgb value format (for one step!)
    #______________________________________________
   
    
    #Offset the square randomly by up to 1/4 of that dimension
    dispX = int(ceil(width/4.))
    dispY = int(ceil(height/4.))
    dispX = randint(-dispX, dispX)
    dispY = randint(-dispY, dispY)

    #Check if the square that is being drawn will even show on the screen.
    #if not, skip this chunk of code below
    if ((x+dispX > -1*(turtle.getWidth()/2) and x+dispX < turtle.getWidth()/2) or (x+dispX+width > -1*(turtle.getWidth()/2) and x+dispX+width < turtle.getWidth()/2))   \
        and((y+dispY > -1*(turtle.getHeight()/2) and y+dispY < turtle.getHeight()/2) or (y+dispY+height > -1*(turtle.getHeight()/2) and y+dispY+height < turtle.getHeight()/2)):

            #This will be the amplitude for the trig funtions following
            x2 = width + randint(-width/4, width/4)
            y2 = height + randint(-height/4, height/4)
            
            #Calculate next position for the next Square (before the x,y gets altered )
            x2 *= cos(angle*PI/180.)
            y2 *= sin(angle*PI/180.)

            #Convert to int and add the previous coords
            x2 = int(ceil(x2)) + x
            y2 = int(ceil(y2)) + y

            #Wiggle the square coords            
            x += dispX
            y += dispY              
                
            #Draw the square starting at x, y (bottom-Left) and going to x+width, y+height
            #drawRect(turtle, x, y, width, height, rgb)
            newRGB = [0,0,0]
            #Alter the rgb value with colorStep
            for i in xrange(3):
                if (curRGB[i] + colorStep[i] <= 255  and curRGB[i] + colorStep[i] >= 1):
                    #Determine which side the curRGB is expected to be on (i.e. inbetween begRGB and endRGB)
                    if colorStep[i] >= 0:
                        #Then check to see if we haven't reached the end color yet.
                        if curRGB[i] <= endRGB[i]:
                            #If we haven't reached endRGB yet, then update the color
                            newRGB[i] = curRGB[i] + colorStep[i]
                    else:
                        #Then check to see if we haven't reached the end color yet.
                        if curRGB[i] >= endRGB[i]:
                            #If we haven't reached endRGB yet, then update the color
                            newRGB[i] = curRGB[i] + colorStep[i]

            #______________________________________________________________________________________________________________
            #It would be easy to just alter the width and height of the next square randomly
            #And for that matter, everything can be adjusted in numerous ways to get different effects.
            #
            #Just going at it plain for now -- testing...
            #
            #colorStep is also something that we can change as we go randomly.
            #______________________________________________________________________________________________________________

            #Then call recursDraw for the next Square
            return [(x, y, width, height, curRGB)] + recursDraw(turtle, x2, y2, angle, width, height, newRGB, colorStep, endRGB)
    else:

        return [(x, y, width, height, curRGB)]
    

def drawBackgroundArt(turtle, timeOfDay):
    """This function will represent the sky -- day and night -- """
    #______________________________________________
    #turtle - An instance of class Turtle, allows drawing to the screen
    #flareX - The x coordinate of the flare -- the area where the sun/moon will be
    #flareY - The y coordinate of the flare
    #timeOfDay - This will determine where the flareX and flareY is placed.
    #______________________________________________

    #On the 24-hr day, 0600 will denote sunrise and 1800 will denote sunset.
    #When the sun is out, each hour the background will be updated.
    #When the sun sets, the moon will rise and go across the sky until 0600 is again reached.

    #I reckon that the drawing only need updated every hour.
    #So here is the coresponding function to determine the height of the sun/moon above a base height in the sky.
    #Note that the base height will eventually be level with the sun/moon when it is setting/rising.

    #Where d(t) is the distance above the base height in correspondence with the current timeOfDay
    #And dist is the maximum distance above the base height.
    #the equation is d(t) = |dist*cos(time*(2*PI/24))|
    baseHeight = turtle.getHeight()/4
    maxDist = turtle.getHeight()/5

    #Calculate the sun/moon's y coord
    starY = int(ceil( baseHeight + fabs(maxDist*cos(timeOfDay*(2*PI/24.))) ))

    #Initialize these to None, so we can check whether they are valid or not
    moonX = None
    sunX = None
    
    #There are three different zones on the screen we need to account for on the x-axis: [00,06], [06,18], [18,24)
    #The intervals above were meant to be in interval notation!
    #Check for [00,06] zone
    if timeOfDay >= 0 and timeOfDay <= 6:
        #This is during the second half of the night.
        #moonX = int(ceil( (timeOfDay-6) / (-3/(turtle.getWidth()/4.)) ))        #I hope this works...
        #The function for the x-value is not meant for turtle...
        #CONVERT from [0,ScreenWidth] to [-ScreenWidth, ScreenWidth]
        moonX = int(ceil( timeOfDay / (-3/(turtle.getWidth()/4.)) ))
            
    #Check for [18,24)
    elif timeOfDay >= 18 and timeOfDay < 24:
        #This is during the first half of the night
        #moonX = int(ceil(( timeOfDay-30) / (-3/(turtle.getWidth()/4.)) ))
        #The function for the x-value is not meant for turtle...
        #CONVERT from [0,ScreenWidth] to [-ScreenWidth, ScreenWidth]
        moonX = int(ceil(( timeOfDay-24) / (-3/(turtle.getWidth()/4.)) ))
        
    #Check for [06,18]
    if timeOfDay >= 6 and timeOfDay <= 18:
        #Daytime!
        #sunX = int(ceil(( timeOfDay-18) / (-3/(turtle.getWidth()/4.)) ))
        #The function for the x-value is not meant for turtle...
        #CONVERT from [0,ScreenWidth] to [-ScreenWidth, ScreenWidth]
        sunX = int(ceil(( timeOfDay-12) / (-3/(turtle.getWidth()/4.)) ))

    #This list will contain tuple elements that give info on each square generated, for all squares
    rayList = []

    #The sun and the moon will be handled separately onto the screen so that both can be applied
    #at sunrise and sunset.
    if moonX != None:
        #Draw a moon using moonX and starY as the starting point.
        #Calculate the absolute angle that the moon rays will be going in.
        #The amplitude denotes the maximum angle displacement starting from 270 (degrees.)6
        absAngle = 60*sin(timeOfDay*(2*PI/24)) + 270

        #Now the other variables for the recursDraw need to be generated.
        #They include the width and height of the squares and the rgb and colorStep values of the squares in lists.
        width = 100
        height = 100

        #I think this'll make a white to grey fade
        startRGB = [255,255,255]
        endRGB = [185,185,185]
        colorStep = [(endRGB[0]-startRGB[0])/10,(endRGB[1]-startRGB[1])/10,(endRGB[2]-startRGB[2])/10]
        
        for i in colorStep:
            i = int(ceil(i))
            
        print moonX, starY, absAngle

        #Now we basically just need to draw the rays in relation to absAngle
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle-30, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle+30, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle-15, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle+15, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle-45, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle+45, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle-60, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle+60, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle-80, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, moonX-(width/2), starY-(height/2), absAngle+80, width, height, startRGB, colorStep, endRGB)

    if sunX != None:
        print sunX
        #Draw the sun with sunX and starY as the coords for the starting point of the sun rays
        #Again calculate the absolute angle, but of the sun's rays!
        absAngle = -60*sin(timeOfDay*(2*PI/24)) + 270

        #Now the other variables for the recursDraw need to be generated.
        #They include the width and height of the squares and the rgb and colorStep values of the squares in lists.    
        width = 100
        height = 100

        #I think this'll make a orange to yellow fade
        startRGB = [230,180,20]
        endRGB = [255, 255, 0]
        colorStep = [(endRGB[0]-startRGB[0])/10,(endRGB[1]-startRGB[1])/10,(endRGB[2]-startRGB[2])/10]
        
        for i in colorStep:
            i = int(ceil(i))
            
        print sunX, starY, absAngle

        #Now we basically just need to draw the rays in relation to absAngle
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle-30, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle+30, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle-15, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle+15, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle-45, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle+45, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle-60, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle+60, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle-80, width, height, startRGB, colorStep, endRGB)
        rayList += recursDraw(turtle, sunX-(width/2), starY-(height/2), absAngle+80, width, height, startRGB, colorStep, endRGB)

    return rayList
    
def main():
    finished = False
    while not finished:
        #Input loop (never trust a user!)
        gewd = False
        while not gewd:
            #Ask for the time
            time = raw_input("Enter the hour of day you wish to view (within interval [0,24)): ")
            
            #Error checking
            if time.isdigit() != True or int(time) >= 24 or int(time) < 0:
                print "Incorrect input"
            else:
                gewd = True

        #Initialize the turtle        
        paul = Turtle(900,700)
        
        #Draw the scene for the corresponding time as specified by the user..
        listOfSquares = drawBackgroundArt(paul, int(time))
        #Shuffling and drawing all of the squares generated for the scene
        shuffle(listOfSquares)
        for (x, y, width, height, color) in listOfSquares:
            drawRect(paul, x, y, width, height, color)

        #Check if the user would like to quit
        entry = raw_input("Leave this entry field blank to quit!")
        if entry == "":
            finished = True

        
main()


    
