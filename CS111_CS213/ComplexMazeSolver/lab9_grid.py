"""
Program: Lab8 Chapter 14
Authors: Jake Waffle, Chase McCubbins

1. Constants
    None
    
2. Inputs
    None
    
3. Computations
    -The construction of our grid using list comprehensions
    
    -Traversal and returning of a string representation of our Grid
    
4. Outputs
    -The string representation of the grid
"""

class Grid(object):
    def __init__(self, rows, columns, fillValue = None):
        self._data = [[fillValue for col in xrange(columns)] for row in xrange(rows)]

    def getHeight(self):
        #returns the number of rows
        return len(self._data)

    def getWidth(self):
        #returns the number of columns
        return len(self._data[0])

    def getItem(self, row, column):
        #gets the item from the grid at position (column,row) and returns it
        if row >= 0 and row < self.getHeight() and column >= 0 and column < self.getWidth():
            return self._data[row][column]
        else:
            "The item you were getting from the Grid is out of bounds!"
            return None

    def setItem (self, rows, columns,item):
        #sets the items of the maze.
        self._data[rows][columns] = item

    def __str__(self):
        #returns a string representation of the text file
        results = ""
        print ""                                #prints a single newline character
        results += str(self.getHeight()) + " " + str(self.getWidth()) + "\n"
        for row in xrange(self.getHeight()):
            rowString = self._data[row]
            for col in xrange(self.getWidth()):
                results += str(rowString[col])
                
            results += "\n"
        return results


class Queue(object):
    def __init__(self):
        self._data = []

    def enqueue(self, item):
        """Adds the item to the end of our queue."""
        self._data.append(item)

    def dequeue(self):
        """Pops off and returns an item from the front of the queue."""
        return self._data.pop(0)

    def __len__(self):
        """Returns the size of the queue (number of items.)"""
        return len(self._data)
    
    def __str__(self):
        """Returns the list object for the data, because it already has its own str() overloader."""
        tmpString = ""
        for i in self._data:
            tmpString += "(" + str(i[0]) + ", " + str(i[1]) + ")" + " "
            
        return tmpString
