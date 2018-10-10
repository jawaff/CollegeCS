"""
Program: Lab9 Chapter 15 Project 10
Authors: Jake Waffle

1. Constants
    -START - This represents the character for the starting position of the maze.

    -FINISH - This represents the character for the finishing position of the maze.

2. Inputs
    -fileName - This is the name of the file that contains the maze.

3. Computations
    -readGetGrid(fileName) - In this function, we traverse the contents of our text file (fileName) and
    calculate the width and height of the maze while also saving each line of the text file into a list.
    Then we traverse the list that was just created and update (after initializing of course) our global maze variable.

    -searchForStart() - This function traverses the global maze variable and then returns its position.

    -findSolutionStack(locX, locY, direction) - This recursive function's purpose is to return ONLY the coordinates
    that make up the maze's path solution. It does this by going to the ends of all possible paths and then the path that
    contains the FINISH character will be the one that gets its coordinates rebuilt back to the start (using something like "return [curLocation] + partialPathSolution")

    -findSolutionQueue(startX, startY) - This function is quite different than its stack version (does not use recursion.) And it uses a queue to store the
    maze's path solution ultimately. And it basically runs down a single path until it hits a dead-end, then we dequeue the possible path solution items and put them back onto the queue after it is empty (the non-solution items get dequeued too.)
    Then we move down another sub path (adding onto the possible path solution in the queue) and go until we hit another dead-end or find the finish. And once we find
    the finish, the path solution is returned in the form of a list (which was converted from the queue, dunno how to make a class iterable.)

    -updateMaze(solutionList) - This traverses the path solution found by findSolution() and updates our global maze variable accordingly.

4. Outputs
    -A prompt that asks to enter a file name for the maze file.
    
    -A maze as it is after loading from the maze file and before alterations with the path solution (the maze's dimensions are also printed right before the maze)

    -The following lines are done for both the stack and the queue solutions.
    
    -The list of coordinates for the path solution is displayed along with the updated maze (with markers for the path solution) and its dimensions (if a path solution was found.) A message also is printed to signify that a path solution was found.
    
    -If a path solution wasn't found, a message will be printed saying this and the previous maze is then printed again along with its dimensions.

    -The updated maze is also saved to a text file (with saveMaze()) if it was successful in finding a solution.

"""

from lab9_grid import Grid, Queue

file_Name = None
maze = None
maze2 = None

START = "P"
FINISH = "T"

def readGetGrid():
    """This reads the map file and returns an assembled grid of the map"""
    #This says that we are going to be updating the maze globally (not locally like it would at default.)
    global maze, maze2
    
    #Try to open the maze's file, but return None if the file didn't load correctly.
    try:
        f = open(file_Name, 'r')
    except Exception:
        #We return None to break out of this function because loading failed
        return None
    
    lines = []
    
    rows = 0

    #Iterates through the file, where each element in f is a line from the file
    for line in f:
        if line != "":
            lines.append(line)
            rows += 1

    columns = len(lines[0])-1    #The minus 1 accounts for the newline character at the end of each line in the file. We're not counting it as an element in the grid!
    
    #print columns, rows

    #Create a grid with the dimensions found
    grid = Grid(rows, columns, 0)
    grid2 = Grid(rows, columns, 0)      #Hopefully this new grid doesn't share memory with its previous one...

    #Adding to the grid 
    for j in xrange(rows):
        line = lines[j]
        for i in xrange(columns):
            grid.setItem(j,i,line[i])
            grid2.setItem(j,i,line[i])

    #Updates the maze globally (since "global maze" at the top of this function)
    maze = grid
    maze2 = grid2

def searchForStart():
    """Returns the position of the start (P) within the grid."""
    for row in xrange(maze.getHeight()):
        for col in xrange(maze.getWidth()):
            if maze.getItem(row,col) == START:
                return row, col
                
def findSolutionStack(locX, locY, direction):
    """This recursively finds the path solution and the direction denotes the area that we came from.
    So Right, Left, Up, Down = 1, 2, 3, 4 and 0 = starting point"""
    #Base case
    if maze.getItem(locY,locX) == FINISH:
        return [(locX,locY)]
    else:
        #Depending on which path will lead to the exit, we will return one of four possible path steps.
        #But the path step that is returned is not decided until the exit has been found.
        
        #Right
        if direction != 1 and (maze.getItem(locY,locX+1) == " " or maze.getItem(locY,locX+1) == FINISH):
            pathStack = findSolutionStack(locX+1,locY, 2) #Going to the right, came from the left
            #maze.setItem(locY,locX+1,"@")
            if pathStack != None:
                item = pathStack.pop()
                pathStack.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == FINISH:
                    return [(locX,locY)] + pathStack
            
        #Left
        if direction != 2 and (maze.getItem(locY,locX-1) == " " or maze.getItem(locY,locX-1) == FINISH):
            pathStack = findSolutionStack(locX-1,locY, 1) #Going to the left, came from the right
            #maze.setItem(locY,locX-1,"@")
            if pathStack != None:
                item = pathStack.pop()
                pathStack.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == FINISH:
                    return [(locX,locY)] + pathStack
    
        #Up
        if direction != 3 and (maze.getItem(locY+1,locX) == " " or maze.getItem(locY+1,locX) == FINISH):
            pathStack = findSolutionStack(locX,locY+1, 4) #Going up, came from down
            #maze.setItem(locY+1,locX,"@")
            if pathStack != None:
                item = pathStack.pop()
                pathStack.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == FINISH:
                    return [(locX,locY)] + pathStack
           
        #Down     
        if direction != 4 and (maze.getItem(locY-1,locX) == " " or maze.getItem(locY-1,locX) == FINISH):
            pathStack = findSolutionStack(locX,locY-1,3) #Going down, came from up
            #maze.setItem(locY-1,locX,"@")
            if pathStack != None:
                item = pathStack.pop()
                pathStack.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == FINISH:
                    return [(locX,locY)] + pathStack
    
    #If the program hits here, then there is no path solution!
    return None

def checkAdjacentItems(locX, locY, item):
    """This returns a direction towards the adjecent square where an item is found. And it is only needed for the queue solution,
    so it assumes we're dealing with the queue's maze (maze2.)"""
    directions = []

    #Up
    if maze2.getItem(locY+1,locX) == item:
        directions.append((locX, locY+1))
    
    #Right
    if maze2.getItem(locY,locX+1) == item:
        directions.append((locX+1, locY))

    #Down
    if maze2.getItem(locY-1,locX) == item:
        directions.append((locX, locY-1))

    #Left
    if maze2.getItem(locY,locX-1) == item:
        directions.append((locX-1, locY))

    return directions

def findSolutionQueue(startX, startY):
    """This is my algorithm for solving the maze using a queue and returning the path solution (in the form of a list.)
    Three different traversals are defined below:
    1. The traversal of a new intersection
    2. The following of a path
    3. The backtracking from a dead-end to the last incomplete path that was passed
    These traversals are what the algorithm use until the end of the maze is found."""
    pathQueue = Queue()

    location = [startX,startY]

    #This denotes the coordinate of the beginning of the last path that was taken.
    lastPath = []

    while maze2.getItem(location[1],location[0]) != FINISH:
        #This checks to see if we are next to the goal yet and returns the coord if so
        finishDir = checkAdjacentItems(location[0],location[1],FINISH)

        #print "These are the finish directions"
        #print finishDir

        #If a coord for the finish was outputted, then we can update our location and move on to the completion of the loop.
        if finishDir != []:
            location[0] = finishDir[0][0]
            location[1] = finishDir[0][1]
            
        #If we are still in the process of assembling our Queue for the path solution
        else:
            newDirections = checkAdjacentItems(location[0],location[1]," ")

            #These ifs will determine what we will enqueue and what our next location will be
            #If this location is a new intersection, then we will place I's on the beginning of each path
            if len(newDirections) > 1:
                for direction in newDirections:
                    maze2.setItem(direction[1],direction[0], "I")
                    
                #On intersections, the next step will be towards the first path with an I.
                directions = checkAdjacentItems(location[0],location[1],"I")

                #Just enqueue the first path
                pathQueue.enqueue(newDirections[0])

                #Set our next location
                location[0] = newDirections[0][0]
                location[1] = newDirections[0][1]

                #This is meant to add all of the Incomplete item ("I") coords to the lastPath, so that we can keep track of them more or less.
                for i in xrange(len(newDirections)):
                    #It is imperitive that the newDirections list is added to the lastPath list in reverse order.
                    #That is because the last path coordinates added will be the ones we're adding on to (current path is at the back of the list.)
                    lastPath.append(newDirections.pop())
                    
            #This is just a common traversal for following a path
            elif len(newDirections) == 1:
                #Put it on the queue
                pathQueue.enqueue(newDirections[0])

                #Set a marker
                maze2.setItem(newDirections[0][1],newDirections[0][0],"X")

                #Set our next location
                location[0] = newDirections[0][0]
                location[1] = newDirections[0][1]
                
            #This is what we do to transition to an incomplete path once we've reach a dead-end.
            else:
                #Only the last path beginning is considered complete (accounts for sub-paths)
                completePath = lastPath.pop()
                
                #We will mark our current path as complete
                maze2.setItem(completePath[1],completePath[0],"C")

                #This will temporarily contain the items that we dequeue out of our original pathQueue
                #We do this so that we can grab the coords that are possibly in the path solution (the items before the last path intersection.)
                newQueue = Queue()

                #Here we're popping our lastPath stack and saving the coords.
                nextPath = lastPath.pop()

                finished = False
                #Then we will update our queue so that the next location will be at the next incomplete path.
                while not finished:
                    coord = pathQueue.dequeue()

                    newQueue.enqueue(coord)

                    incompletePaths = checkAdjacentItems(coord[0],coord[1],"I")

                    if incompletePaths != []:
                        for incPath in incompletePaths:
                            #Check to see if this path was the one we were searching for
                            if nextPath == incPath:
                                #pathQueue now in theory contains the items from the sub-path that led to a dead-end.
                                #So let's go ahead and set a different marker in each of them.
                                for i in xrange(len(pathQueue)):
                                    #bad location
                                    badLoc = pathQueue.dequeue()

                                    #maze2.setItem(badLoc[1],badLoc[0], "B")     #Set that item of the maze!

                                #Now we're going to put the possible path solution items back into the pathQueue
                                for i in xrange(len(newQueue)):
                                    pathQueue.enqueue(newQueue.dequeue())

                                #We gotta add our next coord to the path solution queue
                                pathQueue.enqueue(nextPath)

                                #And we also need the current location updated
                                location[0] = nextPath[0]
                                location[1] = nextPath[1]

                                #Then we can add nextPath back onto lastPath
                                lastPath.append(nextPath)
                                
                                finished = True
                    
                                break

    #This will convert the queue into list form
    pathSolution = []
    for i in xrange(len(pathQueue)):
        pathSolution.append(pathQueue.dequeue())
    
    return pathSolution

        

##def findPath(startX, startY):
##    """Finds the solution path through the maze starting at (startX, startY)."""
##    global maze
##    
##    locationStack = [(startX,startY)]
##
##    finished = True
##    while len(locationStack) != 0:
##        #Pop a location to work with
##        location = locationStack.pop()
##        #locationStack.append(location)
##        
##        #If the location is the end of the maze
##        if maze.getItem(location[1],location[0]) == "T":
##            return location
##        
##        #If the location hasn't already been marked by a path marker or the starting point
##        elif maze.getItem(location[1],location[0]) != "@":
##            #Place a marker at the location if it isn't the starting position
##            if maze.getItem(location[1],location[0]) != "P":
##                maze.setItem(location[1],location[0],"@")
##
##            #Check the adjacent elements on the grid for empty spaces
##            if maze.getItem(location[1],location[0]+1) == " " or maze.getItem(location[1],location[0]+1) == "T":
##                #Add the element to the stack
##                locationStack.append((location[0]+1,location[1]))
##
##            if maze.getItem(location[1],location[0]-1) == " " or maze.getItem(location[1],location[0]-1) == "T":
##                locationStack.append((location[0]-1,location[1]))
##
##            if maze.getItem(location[1]+1,location[0]) == " " or maze.getItem(location[1]+1,location[0]) == "T":
##                locationStack.append((location[0],location[1]+1))
##                
##            if maze.getItem(location[1]-1,location[0]) == " " or maze.getItem(location[1]-1,location[0]) == "T":
##                locationStack.append((location[0],location[1]-1))
##
##    return None
    
def updateMaze(solutionList, bMaze1):
    """Updates the maze with the solution stack!"""
    global maze, maze2

    if bMaze1 == True:
        for location in solutionList:
            maze.setItem(location[1],location[0], "#")
    else:
        for location in solutionList:
            maze2.setItem(location[1],location[0], "#")     
        
def saveMaze(bStack):
    """This is for writing our completed maze (that has the path solution marked on it) to a text file."""
    if bStack == True:
        f = open("completedSTACK"+file_Name,"w")
        f.write(str(maze))    #This should write the string representation of our grid to the file
    else:
        f = open("completedQUEUE"+file_Name,"w")
        f.write(str(maze2))
    
    f.close()        #This saves our changes to the file

def main():
    global file_Name
    
    finished = False
    while not finished:
        file_Name = raw_input("\nEnter a filename for the map text file: ")

        #Check to see if a fileName is even entered
        if file_Name != "":
            readGetGrid()

            #Check to see if the grid was successful in loading
            if maze != None:
                #Do the actions needed with the maze
                print maze  #grid has its own overloader for displaying the maze
                
                row, column = searchForStart()
                
                pathStack = findSolutionStack(column, row, 0)           #The stack is actually a list, but represents the stack

                #Take out the coordinates for the start and finish areas
                pathStack.pop()      #Last element (FINISH)
                pathStack.pop(0)     #First element (START)

                print "\nSTACK SOLUTION\n_____________\n"
                if pathStack != None:
                    print "\nThe end of the maze has been found!"
                    print "\nHere is the list of coordinates for the path solution stack:\n"
                    print pathStack
                    updateMaze(pathStack,True)
                    
                    saveMaze(True)    #This will save our completed maze to a separate file!

                else:
                    print "\nA solution for the maze wasn't found!"
            
                print maze  #grid has its own overloader for displaying the maze

                print "\nQUEUE SOLUTION\n_____________\n"
                pathQueue = findSolutionQueue(column, row)      #The returned item is actually just a list that represents the contents of the queue

                if len(pathQueue) != 0:
                    print "\nThe end of the maze has been found!"
                    print "\nHere is the list of coordinates for the path solution queue:\n"
                    print pathQueue
                    updateMaze(pathQueue,False)
                    
                    saveMaze(False)
                else:
                    print "\nA solution for the maze wasn't found!"
                    
                print maze2
                
        else:
            #Quit if the user doesn't enter a fileName
            finished = True

main()
