
from turtlegraphics import Turtle
from random import randint, random, uniform
from math import sin, cos, fabs, ceil

PI = 3.14159

def growTree(turtle,x,y,angle,width,length,height,level,gatherWght,yDistTravld):
    """This is a recursive program that draws and generates trees starting from a certain point. Then the function returns a list of tuples, so that the tree can be
    stored and drawn again."""
    #Calculate next point
    #angle += randint(-16,16)
    newX = x + (cos((angle*PI)/180.0))*(uniform(0.5, 1.5)*length)
    newY = y + (sin((angle*PI)/180.0))*(uniform(0.5, 1.5)*length)

    yDistTravld += fabs(newY-y)
    
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    #DRAW FROM x,y to newX,newY here with the given width!!!!!
    #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    turtle.up()
    turtle.move(x,y)
    turtle.down()
    turtle.setColor(0,0,0)
    turtle.setWidth(width)
    turtle.move(newX,newY)
    

    stop = False
    #yPeak - some distance
    yCondition = ((height-yDistTravld) + y) - int(ceil(random()*yDistTravld/4.))
    if newY >= yCondition:
        stop = True

    #Check if the base case hasn't been reached yet
    if level <= 10 and stop == False:
        #Check if we are going to branch
        coinToss = randint(1,10)
        if coinToss <= 4:   #40% chance of branching out
            coinToss2 = randint(1,10)
            if coinToss2 <= 6:  #Gives a 60 percent chance to split off of the main branch, 40% to split the main branch.
                #We are going to make a split
                if randint(0,1) == 0:
                    #Left Split
                    angleTwo = angle + randint(-15,15)   #Wiggle that tree!
                    angleOne = angle + 16 + int(ceil((1.-gatherWght)*44))   #60-16=44   [16,60] is the domain I want
                    widthOne = int(ceil((width/2.) + (uniform(-1,1)*width/10.))) #Use ceil to round up and then convert to int
                    widthTwo = width + int(ceil(uniform(-1,0.5)*(width/10.)*3))
                    lengthOne = length - int(ceil(random()*(length/10.)*2))   #subtract the length of the branch by up to 20% of the original
                    lengthTwo = length - int(ceil(random()*(length/10.)*1.5))     #Same as above, but by 15% of the original
                else:
                    #Right Split
                    angleOne = angle + randint(-15,15)   #Wiggle that tree!
                    angleTwo = angle - 16 - int(ceil((1.-gatherWght)*44))   #60-16=44   [16,60] is the domain I want
                    widthTwo = int(ceil((width/2.) + (uniform(-1,1)*(width/10.)))) #Use ceil to round up and then convert to int
                    widthOne = width + int(ceil(uniform(-1,0.5)*(width/10.)*3))
                    lengthTwo = length - int(ceil(random()*(length/10.)*2))   #subtract the length of the branch by up to 20% of the original
                    lengthOne = length - int(ceil(random()*(length/10.)*1.5))     #Same as above, but by 15% of the original
        
            else:
                #We are going to split the main branch into two divergent paths
                #90-180=-90
                #90-0 = 90
                #Bias towards wanting to point the absolute angle upward.
                if angle%360 > 180:
                    weight = (angle%360-270)/90     #angle%360-270 results with (-90,90), so the overall range is (-1,1)
                else:
                    weight = (90-angle%360)/90.     #90-angle%360 results with (-90,90), so the range is (-1,1)
                absAngle = angle + weight*15    #Add or subtract a maximum of 15degrees depending on the angle of the current overall branch

                angleOne = absAngle - 10 - int(ceil((1.-gatherWght)*50))    #angle-
                angleTwo = absAngle + 10 + int(ceil((1.-gatherWght)*50))    #Split off from the absAngle
                angleOne += randint(-10,10)   #Wiggle that tree!
                angleTwo += randint(-10,10)   #Wiggle that tree!
                widthTwo = width + int(ceil(uniform(-1,0.5)*(width/10.)*2))
                widthOne = width + int(ceil(uniform(-1,0.5)*(width/10.)*2))
                lengthTwo = length - int(ceil(random()*(length/10.)*2))   #subtract the length of the branch by up to 10% of the original
                lengthOne = length - int(ceil(random()*(length/10.)*2))

            gatherWghtOne = 0.0
            gatherWghtTwo = 0.0

            #Randomly alter the gatherWght of the new branches
            if gatherWght >= 0.2 and gatherWght <= 0.8:
                gatherWghtOne += uniform(-0.2,0.2)
                gatherWghtTwo += uniform(-0.2,0.2)
                
            elif gatherWght < 0 and gatherWght > 1:
                #This gatherWght broked!
                print "gatherWght has escaped the interval!"

            elif gatherWght >= 0.2:
                gatherWghtOne += uniform(-0.2,0)
                gatherWghtTwo += uniform(-0.2,0)
                
            elif gatherWght <= 0.8:
                gatherWghtOne += uniform(0,0.2)
                gatherWghtTwo += uniform(0,0.2)

            return [newX,newY,width,level] + growTree(turtle,newX,newY,angleOne,widthOne,lengthOne,height,level+1,gatherWghtOne,yDistTravld) + growTree(turtle,newX,newY,angleTwo,widthTwo,lengthTwo,height,level+1,gatherWghtTwo,yDistTravld)
        else:
            newAngle = angle + randint(-15,15)   #Wiggle that tree!
            newWidth = width + int(ceil(uniform(-1,0)*(width/10.)*2))
            newLength = length - int(ceil(random()*(length/10.)))

            newGatherWght = 0.0
            
            if gatherWght >= 0.2 and gatherWght <= 0.8:
                newGatherWght += uniform(-0.2,0.2)
                
            elif gatherWght < 0 and gatherWght > 1:
                #This gatherWght broked!
                print "gatherWght has escaped the interval!"

            elif gatherWght >= 0.2:
                newGatherWght += uniform(-0.2,0)
                
            elif gatherWght <= 0.8:
                newGatherWght += uniform(0,0.2)

            #We are just going to continue with the current branch
            return [newX, newY, width, level] + growTree(turtle,newX,newY,newAngle,newWidth,newLength,height,level+1,newGatherWght,yDistTravld)
            
    else:
        #Base Case
        return [(newX, newY,width,level)]

##def main():
##
##    finished = False
##    while not finished:
##        paul = Turtle(600,600)
##        gewd = False
##        """
##        while not gewd:
##            x = raw_input("Enter an x value!")
##            if x[0] == "-":
##                x = x[1:]
##                if x.isdigit():
##                    x = -1 * int(x)
##                    gewd = True
##            else:
##                if x.isdigit():
##                    x = int(x)
##                    gewd = True
##        """
##        x = 0
##        y = -250
##
##        width = randint(8,10)
##        #The first element is not put into the list by the growTree function
##        treeList = [(x,y,width,0)] + growTree(paul,x,y,randint(70,110),width,randint(20,50),randint(200,400),0,random(),0)
##        raw_input("Press enter for next tree!")
##
##main()
