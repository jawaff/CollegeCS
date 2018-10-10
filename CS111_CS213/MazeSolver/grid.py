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
        #supports two demensiional rows, columns
        return self._data[row][column]

    def setItem (self, rows, columns,item):
        #sets the items of the maze.
        self._data[rows][columns] = item

    def __str__(self):
        #returns a string representation of the text file
        results = ""
        print self.getHeight(), self.getWidth()
        for row in xrange(self.getHeight()):
            rowString = self._data[row]
            for col in xrange(self.getWidth()):
                results += str(rowString[col])
                
            results += "\n"
        return results
