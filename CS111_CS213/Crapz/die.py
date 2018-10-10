"""
Program: die.py
Author(s):  Jacob Waffle
            Katy Phipps
            Casey Blamires

Die (plural: Dice) class. The die can be rolled and its value returned to the caller

1. Significant constants
    None

2. The inputs are
    There are no user-required inputs in this class. The class *does* require the randint
    function from `random`.

3. Computations:
    randint() is called in the <class>.roll() method, which only returns a random number

4. The outputs are
    Depending on the method called, values are returned to the caller. No printing occurs
    in this class
"""

"""
ORIGINAL COMMENTS FROM TEXTBOOK
File: die.py

"""
from random import randint

class Die(object):
    """This class represents a six-sided die."""
    def __init__(self):
        """The initial face of the die."""
        self._value = 1
        
    def roll(self):
        """Resets the die's value to a random number between 1 and 6."""
        self._value = randint(1, 6)

    def getValue(self):
        return self._value

    def __str__(self):
        return str(self._value)
