"""

Authors:
Jake Waffle, Mark Kelly
Created on:
4/11/12
Title of program:
Question1.py
Significant Constants:
none
User Input:
uNumber asks for a number to be aproximated.
And also tells the user to enter a positive number if a negative one is entered.

                        Functions
Main:
    The main function asks for user input and checks to see if a number or nothing is
entered and prints the aproximated answer.

Newton:
    the newton function uses a aproximation algorithum to aproximate the exact square
roots of numbers.


"""

def newton(uNumber):
    '''This returns the result of the newton approximation for square roots on the parameter
    uNumber.'''
    while True:
        z = 1
        for i in xrange(16):
            z=(z+uNumber/z)/2
        return z
            
def main():
    '''We enter an interactive loop that either quits or prints the square roots of
    the numbers that are entered by the user.'''
    done = False
    while done == False:
        uNumber = raw_input('Enter number,or just push enter to quit: ')
        if uNumber == "":
            done = True
        else:
            #We don't want to deal with imaginary numbers
            if uNumber >= 0:
                uNumber = newton(float(uNumber))
                print 'The square root of your number is: ', uNumber
            else:
                uNumber = raw_input('You did not enter a positive number: ')
                uNumber = float(uNumber)    
main()
