"""
Program: student.py
Author(s):  Jacob Waffle
            Katy Phipps
            Casey Blamires

Class for students. Each object contains a student's name, and the number
of scores that they have associated with them. Methods include the ability
to mutate and access test scores

As of the Projects # 1 question in the textbook, this class also includes
comparison operations and an quality operator

1. Significant constants
    None

2. The inputs are
    There are no user-required inputs in this class. However, the mutator
    mehtods have necessary parameters (described at that method)

3. Computations:
    the average is the sum of all test scores / (divided by) the total number
    of test scores
    The only other computation here is the cmp() compare function, used to
    compare two averages from different objects

4. The outputs are
    Each accessor method has its own output. The __str__ string printing
    method prints out the student's name and all of their test scores
"""



class Student(object):
    """ Student Class - used to keep track of students and their test scores """
    
    def __init__ ( self , name , number ):
        """
        __init__ - Constructor
        This method is first called when the object goes into scope
        param:  name - the student's name
                number - total number of test scores that will be in this object
        return: void (nothing)
        """
        self._name = name
        self._scores = []   # creating an empty list for the test scores
        for count in xrange(number):
            self._scores.append ( 0 ) # all scores are initialized as 0 (zero)







    
    def getName ( self ):
        """
        getName - accessor method, returns the student's name
        param:  none
        return: string
        """
        return self._name






    
    def setScore ( self , i , score):
        """
        setScore - set the score for a specific test (user defined index)
        param:  i - the index of the score
                score - value (the test score) to put in
        return: none
        """
        self._scores[i-1] = score







    
    def getScore ( self, i ):
        """
        getScore - returns the test score specified
        param:  i - index of the test score
        return: string
        """
        return self._scores[i-1]







    
    def getAverage ( self ):
        """
        getAverage - get the average of test scores
        param:  none
        return: number (either int or double?)
        """
        total = 0

        # for item in list
        for element in self._scores:
            total += element
        return (total)/len(self._scores)







    
    def getHighScore(self):
        """
        getHighScore - get the best test score
        param:  none
        return: number (either int or double?)
        """
        return max(self._scores)








    
    def __str__ (self ) :
        """
        __str__ - printing method
        param:  none
        return: string
        """
        return "Name: " + self._name + "\nScores: " + \
               " ".join(map(str,self._scores))







    
    def __eq__ ( self , other ):
        """
        __eq__ - equality operator overload
        param:  other - the other object to which we are comparing
        return: boolean
        """
        if self._name == other._name:
            return True
        else:
            return False






    def __cmp__ ( self , other ):
        """
        __cmp__ - comparison operator overload
        param:  other - the other object
        return: less than, greater than, or equal to
        """
        return cmp( self.getAverage() , other.getAverage() )
