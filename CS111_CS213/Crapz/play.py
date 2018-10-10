""" functions to interact with the user to play the games"""
"""
Program: play.py
Author(s):  Jacob Waffle
            Katy Phipps
            Casey Blamires

This file contains two functions, one to play the game, and one to play multiple games

1. Significant constants
    None

2. The inputs are
    The program itself requires the Player class from craps.py. playManyGames() requires user
    input to determine how many games to play

3. Computations:
    In the playManyGames( ) function, computations include incrementing the wins and winRolls
    counters and the losses and lossRolls counters.
    Win roll percentage and loss roll percentage is calculated at the end of playManyGames() by taking
    the number of winning rolls/losing rolls and dividing it by the total wins/losses. Win
    percentage is calculated by diving the number of wins by the number of games played.

4. The outputs are
    Each function prints to the console. playOneGame() prints if you win or lose, and
    playManyGames() prints the winning, losing, and total win percentages.
"""
from craps import Player


def playOneGame():
    """Plays a single game and prints the results."""
    player = Player()
    youWin = player.play()
    print player
    if youWin:
        print "You win!"
    else:
        print "You lose!"   
        
        
def playManyGames():
    """Plays a number of games and prints statistics."""
    gewd = False
    #Filter input
    while not gewd:
        number = raw_input ( "Enter the number of games you'd like to play: " )
        #Check to see if the input is actually a character/string or negative number(zero is also included to prevent divide by zeros.)
        if number.isalpha() or number == '' or int(number) <= 0:
            print "Incorrect input detected!"
        #Numbers greater than or equal to zero zero
        else:
            #convert the string to an integer
            number = int(number)
            gewd = True
    wins = 0
    losses = 0
    winRolls = 0
    lossRolls = 0
    player = Player()
    for count in xrange(number):
        hasWon = player.play()
        rolls = player.getNumberOfRolls()
        if hasWon:
            wins += 1
            winRolls += rolls
            print wins, winRolls
        else:
            losses += 1
            lossRolls += rolls
            print losses, lossRolls
    #Avoid divide by zeros
    if wins > 0:
        print "The total number of wins is", wins
        print "The average number of rolls per win is %0.2f" % \
              (float(winRolls) / wins )
    else:
        print "There were no wins to report."
    #Avoid divide by zeros
    if losses > 0:
        print "The total number of losses is", losses
        print "The average number of rolls per loss is %0.2f" % \
              (float(lossRolls) / losses)
    else:
        print "There were no losses to report."
    
    print "The winning percentage is %0.3f" % \
          (float(wins) / number)
