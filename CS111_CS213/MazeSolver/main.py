from grid import Grid

maze = None

def readGetGrid(fileName):
    """This reads the map file and returns an assembled grid of the map"""
    #This says that we are going to be updating the maze globally (not locally like it would at default.)
    global maze
    
    #Try to open the maze's file, but return None if the file didn't load correctly.
    try:
        f = open(fileName, 'r')
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

    #Adding to the grid 
    for j in xrange(rows):
        line = lines[j]
        for i in xrange(columns):
            grid.setItem(j,i,line[i])

    #Updates the maze globally (since "global maze" at the top of this function)
    maze = grid

def searchForStart():
    """Returns the position of the start (P) within the grid."""
    for row in xrange(maze.getHeight()):
        for col in xrange(maze.getWidth()):
            if maze.getItem(row,col) == "P":
                return row, col
                
def findSolution(locX, locY, direction):
    """This recursively finds the path solution and the direction denotes the area that we came from.
    So Right, Left, Up, Down = 1, 2, 3, 4 and 0 = starting point"""
    #Base case
    if maze.getItem(locY,locX) == "T":
        return [(locX,locY)]
    else:
        #Depending on which path will lead to the exit, we will return one of four possible path steps.
        #But the path step that is returned is not decided until the exit has been found.
        
        #Right
        if direction != 1 and (maze.getItem(locY,locX+1) == " " or maze.getItem(locY,locX+1) == "T"):
            pathList = findSolution(locX+1,locY, 2) #Going to the right, came from the left
            #maze.setItem(locY,locX+1,"@")
            if pathList != None:
                item = pathList.pop()
                pathList.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == "T":
                    return [(locX,locY)] + pathList
            
        #Left
        if direction != 2 and (maze.getItem(locY,locX-1) == " " or maze.getItem(locY,locX-1) == "T"):
            pathList = findSolution(locX-1,locY, 1) #Going to the left, came from the right
            #maze.setItem(locY,locX-1,"@")
            if pathList != None:
                item = pathList.pop()
                pathList.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == "T":
                    return [(locX,locY)] + pathList
    
        #Up
        if direction != 3 and (maze.getItem(locY+1,locX) == " " or maze.getItem(locY+1,locX) == "T"):
            pathList = findSolution(locX,locY+1, 4) #Going up, came from down
            #maze.setItem(locY+1,locX,"@")
            if pathList != None:
                item = pathList.pop()
                pathList.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == "T":
                    return [(locX,locY)] + pathList
           
        #Down     
        if direction != 4 and (maze.getItem(locY-1,locX) == " " or maze.getItem(locY-1,locX) == "T"):
            pathList = findSolution(locX,locY-1,3) #Going down, came from up
            #maze.setItem(locY-1,locX,"@")
            if pathList != None:
                item = pathList.pop()
                pathList.append(item)
                
                #Check to see if this direction has the finish on the end of it
                if maze.getItem(item[1],item[0]) == "T":
                    return [(locX,locY)] + pathList
    
    #If the program hits here, then there is no path solution!
    return None
    

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
    
def updateMaze(solutionList):
    """Updates the maze with the solution stack!"""
    global maze
    
    for location in solutionList:
        maze.setItem(location[1],location[0], "@")

def main():
    finished = False
    while not finished:
        fileName = raw_input("\nEnter a filename for the map text file: ")

        #Check to see if a fileName is even entered
        if fileName != "":
            readGetGrid(fileName)

            #Check to see if the grid was successful in loading
            if maze != None:
                print maze  #grid has its own overloader for displaying the maze
            
            row, column = searchForStart()
            
            pathList = findSolution(column, row, 0)
    
            if pathList != None:
                print "\nThe end of the maze has been found!"
                updateMaze(pathList)

            else:
                print "\nA solution for the maze wasn't found!"
            
            #Check to see if the grid was successful in loading
            if maze != None:
                print maze  #grid has its own overloader for displaying the maze

            #Save the new maze to a text file
                
        else:
            #Quit if the user doesn't enter a fileName
            finished = True

main()
