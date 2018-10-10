"""
Program: main.py
Author(s):  Jacob Waffle
            Katy Phipps
            Casey Blamires

Main program to play craps. This has a user interface to allow the "player" (read: user) to play
one or many games, or exit the "casino" (terminating the program)

1. Significant constants
    PLAY - a boolean (defaulted to True), which controls the program loop. This is never changed; to end
            the loop, the player enters "3" to exit, or a nonsensical input (such as "4" or "sdfsdfsd")

2. The inputs are
    main() will make a sort of menu asking the player about playing the game. The program is designed
    to make sure the player doesn't enter any bad input, such as an unavailable option

3. Computations:
    checking the player's input from the menu.

4. The outputs are
    In the program loop, main() will print out a menu for the player to choose from. All other output
    occurs in either the Player class or the functions defined in play.py
"""
from die import Die
from craps import Player
from play import *




def main():
    # this is a loop variable to keep playing the game until the user decides to stop
    PLAY = True
    print "\n\nLet's Play Craps!"
    print "Please enter a selection:"
    # program loop to keep playing
    while PLAY:
        print "1. Play one game of craps"
        print "2. Play multiple games of craps"
        print "3. Leave the casino"

        """ I'm using raw_input here so the program won't flip out if the user
            enters a garbage string such as 'dfsdfsdfsdfsdfs' """
        selection = raw_input ( ">>> " )
        if selection == "1":
            playOneGame()
            print "\nPlease enter a selection:"        
        elif selection == "2":
            playManyGames()
            print "\nPlease enter a selection:"    
        elif selection == "3":
            print "\nHave a wonderful day!"
            PLAY = False
        else:
            print "\nPlease enter a number corresponding with your selection."

main() # run the program!
