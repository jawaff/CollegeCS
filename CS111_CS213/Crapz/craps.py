"""
Program: craps.py
Author(s):  Jacob Waffle
            Katy Phipps
            Casey Blamires

Game of craps class (called Player)
The player is who plays the game, with simple methods such as getting the number
of rolls so far, and playing a simple game

1. Significant constants
    None

2. The inputs are
    There are no user-required inputs in this class.

3. Computations:
    None. The only "computation" here is rolling a dice, which is implemented in
    the Die class

4. The outputs are
    Each method (with the exception of the constructor) returns something, be it a string
    or an integer, or a boolean
"""

"""
ORIGINAL COMMENTS FROM TEXTBOOK
File: craps.py

This module studies and plays the game of craps
"""

from die import Die

class Player (object ):

    def __init__ ( self ):
        """Has a pair of dice and an empty rolls list."""
        self._die1 = Die()
        self._die2 = Die()
        self._rolls = []

    def __str__ ( self ):
        """Returns the string rep of the history of rolls."""
        result = ""
        for ( v1,v2 ) in self._rolls:
            result = result + str((v1,v2)) + " " + \
                     str(v1+v2) + "\n"
        return result

    def getNumberOfRolls ( self ):
        """Returns the number of the rolls in one game."""
        return len(self._rolls)

    def play(self):
        """Plays a game, saves the rolls for that game,
        and returns True for a win and False for a loss."""
        self._rolls = []
        self._die1.roll()
        self._die2.roll()
        (v1,v2) = (self._die1.getValue() , self._die2.getValue() )
        self._rolls.append((v1,v2))
        initialSum = v1 + v2
        if initialSum in (2,3,12):
            return False
        elif initialSum in (7,11):
            return True
        while True:
            self._die1.roll()
            self._die2.roll()
            (v1,v2) = (self._die1.getValue() , self._die2.getValue() )
            self._rolls.append((v1,v2))
            sum = v1+v2
            if sum == 7:
                return False
            elif sum == initialSum:
                return True
        
