"""
Created on Mar 29, 2012
Authors:
Jake Waffle Mark Kelly
Created on:
4/11/12
Title of program:
Question2.py
Significant Constants:
none
User Input:
uNumber asks for a number to be aproximated.

                        Functions

Main:
    The main function asks for user input and checks to see if a number or nothing is
entered and prints the aproximated answer.

newton:
    the newton function uses a aproximation algorithum to aproximate the exact square
roots of numbers.
"""
def newton(uNumber, approx):
    '''This is a recursive function that returns a step of the newton approximation.'''
    approx = (approx + uNumber / approx) / 2
    temp = approx **2
    #Checking to see if the approximation is goooooood
    if temp <= uNumber:
        return approx
    else:
        return newton(uNumber, approx)
    
def main():
    '''We enter an interactive loop that either quits or prints the square roots of
    the numbers that are entered by the user.'''    
    done = False
    #Interactive LOOOOOP
    while done == False:
        uNumber = raw_input('Enter number,or just push enter to quit: ')
        #QUIT
        if uNumber == "":
            done = True
        #SQUARE ROOT DISPLAY
        else:
            uNumber = float(uNumber)
            approx = 1
            approx = newton(uNumber, approx)
            print 'The square root of your number is: ', approx
main()
