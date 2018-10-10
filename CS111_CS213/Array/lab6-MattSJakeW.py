"""
Lab 5; CS 213
Authors:            Jacob Waffle,
                    Matt Steele
                    
Date:               10/5/2012

File:               arrays.py

Some code used from chapter 13 of Fundamentals of Python, by Kenneth Lambert

An Array is a restricted list whose clients can use
only [], len, iter, and str.

To instantiate, use

<variable> = array(<capacity>, <optional fill value>)

The fill value is None by default.


Significant Constants:

        ACTIONS:                List of Menu actions stored in a tuple
        DEFAULT_CAPACITY:       The initial size of the instantiated array
        
Inputs:
        name                    Name of the new array
        sizeArray               Size of new array
        defaultValues           Default fill value for the array's empty cells
        action                  User input selection for the menu
        quit                    Input for checking for program termination
        nameArray               Input that specifies the current working array
        indx                    Input for tracking the index of a item to be removed from an array
        
Outputs:
        
        Print statements explaining what is happening with respect to their selected actions.
        
        These print statements include error messages for when incorrect input is given, success 
        messages for when an action was successful and other print statements for the contents of
        the ArrayPool and the selected modified array.


"""

class Array(object):
    """Represents an array."""
    def __init__(self, capacity, fillValue = None):
        """Capacity is the static size of the array.
        fillValue is placed at each position."""
        
        self._items = list() 
        self._fillValue = fillValue
        self._DEFAULT_CAPACITY = capacity
        self._logicalSize = 0 #as required by exercise 1
        
        
        for count in xrange(capacity):
            self._items.append(self._fillValue)
          

    def __len__(self):
        """-> The capacity of the array."""
        return len(self._items)

    def __str__(self):
        """-> The string representation of the array."""
        return str(self._items)

    def __iter__(self):
        """Supports traversal with a for loop."""
        return iter(self._items)

    def __getitem__(self, index):
        """Subscript operator for access at index."""
        #Check to see whether or not the index is within the array's element range.
        if index >= 0 and index < len(self):
            return self._items[index]

        return None

    def __setitem__(self, index, newItem):
        """Subscript operator for replacement at index."""
        #Check to see whether or not the index is within the array's element range.
        if index >= 0 and index < len(self):
            #If the element has nothing in it
            if self._items[index] == self._fillValue:
                self._logicalSize += 1
                
            #If we are going to replace an element with fillValue
            if self._items[index] != self._fillValue and newItem == self._fillValue:
                self._logicalSize -= 1
            
            self._items[index] = newItem

    def _size(self):
        """Returns the logical size of the array."""
        return self._logicalSize
    
    def _grow(self):
        """Increase the physical size of the array. elements will be the number of elements to grow the list by."""  
        limit = 0
        #Iterating through the list to find the number of elements
        for i in xrange(len(self)):
            if self._items[i] != self._fillValue:
                #There's an element at index i, so update the limit
                limit = i
                
        #Only grow the array if the limit+1 and the physical size is the same.
        if limit+1 == len(self):
            temp = Array(len(self)*2)
            
            #Copy existing elements to the new Array
            for i in xrange(len(self)):
                temp[i] = self._items[i]
                
            #Initialize the new elements to the fillValue
            for j in xrange(len(self), len(self)*2):
                temp[j] = self._fillValue
            self._items = temp

              
    def _shrink(self):
        #Decrease the physical size of the array. It will 
        limit = 0

        #Iterating through the list to find the number of elements
        for i in xrange(len(self)):
            if self._items[i] != self._fillValue:
                #There's an element at index i, so update the limit
                limit = i
                print limit, "test limit"

        if (limit <= len(self)/4) and (len(self) > limit) and (len(self) > self._DEFAULT_CAPACITY):
            #The newSize will never be smaller than the limit! So all previously active elements will always
            #be transfered to the new Array
            newSize = max(limit, len(self)/2)
            newSize = max(newSize, self._DEFAULT_CAPACITY)
            temp = Array(newSize, self._fillValue)
            for i in xrange(limit):
                temp[i] = self._items[i]
                #temp[i] = a[i]  changed from this after eclipse run
            self._items = temp

    def _remove(self, targetIndex):
        """Remove an item from the list at position targetIndex"""
        if 0 <= targetIndex and targetIndex < len(self):
            limit = 0
            for i in xrange(len(self)):
                if self._items[i] != self._fillValue:
                    #There's an element at index i, so update the limit
                    limit = i
                    
            #Move items in the list to their future positions
            for i in xrange(targetIndex, limit):
                self._items[i] = self._items[i+1]
            
            
            #Only update the logicalSize if the value being removed was not a None value.
            if self._items[targetIndex] != self._fillValue:
                self._logicalSize -= 1
            
            #The vacated element will be set to the fillValue
            self._items[limit] = self._fillValue  
            
            #Shrink the physical size if need be
            self._shrink()
    
    def _insert(self, item, targetIndex):
        '''insert an item into the list at position targetIndex'''
        
        if 0 <= targetIndex and targetIndex < len(self):
            #Increase the physical size if necessary
            self._grow()
    
            limit = 0
            for i in xrange(len(self)):
                if self._items[i] != self._fillValue:
                    #There's an element at index i, so update the limit
                    limit = i
                           
            #Move the items down, to free up the space at position index of the _items
            for i in xrange(limit+1, targetIndex, -1):
                self._items[i] = self._items[i-1]
            
            #Only update the logical Size if we are updating a None value with a non-None value.
            if self._items[targetIndex] == self._fillValue and item != self._fillValue:
                self._logicalSize += 1

            #Copy the item into the list at position targetIndex
            self._items[targetIndex] = item
            
    
    def __eq__(self, other):
        if (len(self) == len(other)):
            #compare the contents
            equal = True
            for i in xrange(len(self)):
                if (self._items[i] != other._items[i]):
                    equal = False
                    
            return equal


ArrayPool = {}
arrayInstance = None
arrayName = None

def doAction(action):
    """This executes the action represented by the parameter."""
    global ArrayPool, arrayInstance, arrayName
    if action == 1:
        #Add Array
        proceed = True
        #Ask the user for the name of the Array to be created
        name = raw_input("\nEnter the name of the Array you'd like to create: ")
        sizeArray = raw_input("\nPlease enter the physical size of the array: ")
        defaultValues = raw_input("\nEnter a default value for the Array's elements(or leave it blank to set them as None): ")
    
        #Check the input's validity
        if not name.isalpha() or not sizeArray.isdigit():
            proceed = False
            print "\nI'm sorry, but I don't like that input."
        
        newArray = None
        #Execute stuff!
        if proceed:
            if defaultValues != "":    
                newArray = Array(int(sizeArray), defaultValues)
            else:
                newArray = Array(int(sizeArray))

            #Throw that thing into the dictionary
            ArrayPool[name.lower()] = newArray

            print ""
            print name.lower(), "has been added to the array pool!"
        
    elif action == 2:
        #Choose Array
        print ""
        print "%-10s%-10s" % ("Name", "Contents")        
        #Print a list of all the Arrays (name and contents) that are being stored in the dictionary
        for (key, value) in ArrayPool.items():
            print "%-10s%-10s" % (key, value)
        
        #Ask the user for a name of the Array that s/he would like to select
        nameArray = raw_input("\nEnter the name of the array you'd like to use: ")
        
        if nameArray.isalpha() and nameArray.lower() in ArrayPool.keys():
            #Update the pointer instance respectively
            arrayInstance = ArrayPool[nameArray.lower()]
            arrayName = nameArray.lower()
            
            print ""
            print nameArray, "is ready to be used by other actions now!"
            
        else:
            print "\nI'm sorry, but I don't like that input."            
       
    elif action == 3:
        #Can't use an array that doesn't exist
        if arrayInstance != None:
            #Add an element to Array
            #Ask the user the index and item to be added
            indx = raw_input("\nEnter the index you'd like to insert into: ")
            item = raw_input("\nEnter the element you'd like to insert into the chosen Array: ")

            if indx.isdigit() and (item.isalpha() or item.isdigit()):
                #The inputs pass my inspection and are worthy of being added to the Array
                #Call insert with the user's input as arguments with the pointer instance                            
                arrayInstance._insert(item, int(indx))
                
                print ""
                print arrayInstance
                
            else:
                print "\nI'm sorry, but I don't like that input."     
                
        else:
            print "\nChoose an array first!"                              

    elif action == 4:
        #Can't use an array that doesn't exist
        if arrayInstance != None:
            #Remove an element from the Array   
            #Ask the user the index
            indx = raw_input("\nEnter the index of the item you'd like to remove: ")
            
            if indx.isdigit():
                #Call the remove method for the pointer instance            
                arrayInstance._remove(int(indx))
                
                print ""
                print arrayInstance
                
            else:
                print "\nI'm sorry, but I don't like that input."   
                
        else:
            print "\nChoose an array first!"                              
           
    elif action == 5:
        if arrayInstance != None:
            #We're going to compare the arrayInstance with one chosen by the user from the ArrayPool.            
            print "\nYour current array"
            print "\nName:", arrayName
            print "\nOther arrays in the array pool"         
            #Print a list of the Arrays in the ArrayPool                  
            for key in ArrayPool.keys():
                if key != arrayName:
                    print "\nName:", key
                      
            nameArray = raw_input("\nEnter the name of the array you'd like to compare to your current array: ")
            
            if nameArray.isalpha() and nameArray.lower() in ArrayPool.keys():
                if arrayInstance == ArrayPool[nameArray.lower()]:
                    print "\nThe arrays are the same!"
                else:
                    print "\nThe arrays are not the same!"
            else:
                print "\nI'm sorry, but I don't like that input."    
                
        else:
            print "\nChoose an array first!"                
                    
    elif action == 6:
        #Print the logicalSize (number of active elements inside the array.)
        if arrayInstance != None:
            print ""
            print "The contents of", arrayName, "are", arrayInstance
            print "The logical size of", arrayName, "is", arrayInstance._size()
            
        else:
            print "\nChoose an array first!"
        
#Defines a list of the user's available actions
ACTIONS = ("1. Add Array", "2. Choose an Array","3. Add an element to Array", "4. Remove an element from the Array", "5. Compare two arrays for equality", "6. Print information on the current array")

def main():

    finished = False
    #Main loope
    while not finished:
        print ""
        
        #Prints all of the actions available to the user
        
        for str in ACTIONS:
            print str
            
        #Take in input regarding the user's next action
        action = raw_input("\nEnter the number that represents your intended action from the list above: ")
        
        #Execute the action
        doAction(int(action))
           
        #Check quit
        quit = raw_input("\nType 'Q' if you'd like to quit! ")
        if quit.upper() == "Q":
            finished = True
        
main()
