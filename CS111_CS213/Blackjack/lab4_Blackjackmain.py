"""
Program: lab4-DouglasG_and_JakeW
Authors: Douglas Griffith and Jacob Waffle

1. Constants
    #Constants of the Card class
    RANKS,            #A tuple of the ranks possible for the cards
    SUITS,            #A tuple of the suits possible for the cards
    BACK_OF_CARD      #The filename connecting to the back image of the cards
    
2. Inputs
    #Of the Blackjack class
    The inputs are handled by the Button class in TKinter.
    The instances of the Button class include:
    _hitButton
    _passButton
    _newButton
    
3. Computations
    We mostly just are handling input (for a button/button trigger)
    and dealing with the logic of the Blackjack game.
    
4. Outputs
    The hit, pass and new game button.
    The card images/text of the player's hand.
    The card images/text of the dealer's hand.
    The text saying who one the game.
"""

from Tkinter import *

from lab4_deck import Deck, Card          #This is where our Deck and Card class is being held
from lab4_players import Player, Dealer        #This is where our Player and Dealer class is being held
#import pdb
        
class Blackjack(Frame):
    def __init__(self):
        #Initialize the inheritted class
        Frame.__init__(self)       
        
        self.master.title("BLACKJACK!")

        #Make the window shown!
        self.grid()

        #Initialize a dealer and player to be used for the game
        self._player = Player()
        self._dealer = Dealer()

        #Initialize a deck for the game to use
        self._deck = Deck()
        self._deck.shuffle()

        #denotes the end of the current game
        self._end = True    #This is initialized as True to disable the hit and pass buttons until the user presses the new game button.
              
        #Initialize storage for the Player's card image labels
        #(Instances of class Label will be used as elements)
        self._pCardImgLabels = []
        self._pCardNamLabels = []
        #Do the same for the Dealer's card image labels
        self._dCardImgLabels = []
        self._dCardNamLabels = []

        #Set face down cards on the window where the player's and dealer's cards will be placed.
        for i in xrange(2):
            #Load and place the player's cards in row 1, columns 0&1
            Lbls = self._loadCard(None, 1, i)   #Returns a list containing the imgLabel and the textLabel
            
            #Put the labels into the list of labels!
            self._pCardImgLabels.append(Lbls[0])
            self._pCardNamLabels.append(Lbls[1])
            
            #Load and place the dealer's cards in row 3, columns 0&1
            Lbls2 = self._loadCard(None, 3, i)  #Returns a list containing the imgLabel and the textLabel

            #Put the labels into the list of labels!
            self._dCardImgLabels.append(Lbls2[0])
            self._dCardNamLabels.append(Lbls2[1])

        #Initialize this so it can be just updated later
        self._endMsg = Label(self, text = "")
        self._endMsg.grid(row = 7, column = 1)
        
        #Button Setup
        self._hitButton = Button(self, text = "Hit", command = self._hit)
        self._hitButton.grid(row = 0, column = 0)
        self._passButton = Button(self, text = "Pass", command = self._pass)
        self._passButton.grid(row = 0, column = 1)
        self._newButton = Button(self, text = "New Game", command = self._new)
        self._newButton.grid(row = 0, column = 2)
        
    
    def _loadCard(self, card, r, c):
        """This method will load an image connected to "fileName" and place its label
        on the grid at row = r and column = c. And finally return the imageLabel for storage purposes.

        !!!Facedown cards are represented by card = None in some certain calls."""
        
        #Initialize image buffer to be used
        _image = None
        
        #initialize textLabel before updating it in the if/else
        _textLabel = None
        #Check if we aren't dealing with a faceDown card
        if card != None:
            #The text for the card is free to be visible
            _textLabel = Label(self, text = card)
            #load/get image
            _image = PhotoImage(file = card.fileName)
        else:
            #The text for the card is hidden because it is facedown, the label will be updated in _pass()
            _textLabel = Label(self, text = "")
            #load/get image
            _image = PhotoImage(file = Card.BACK_OF_CARD)


        #Make a label for the image
        _imageLabel = Label(self, image = _image)
            
        #Display the text on the window
        _textLabel.grid(row = r+1, column = c)

        #Put the image label on the window
        _imageLabel.grid(row = r, column = c)
        
        return [_imageLabel, _textLabel]

    def _updateCard(self, imgLyst, txtLyst, card, column):
        """This method will update the card at index column of labelLyst (labelLyst[column]).
        The first card at column x corresponds with index x of the labelLyst.
        !!!This function too will make use of card == None to represent faceDown cards."""
        #Initialize image buffer to be used
        _image = None
        
        #initialize textLabel before updating it in the if/else
        textLabel = None
        
        if card != None:
            #The text for the card is free to be visible
            txtLyst[column]["text"] = card
            
            #load/get image
            _image = PhotoImage(file = card.fileName)
            
        else:
            #The text for the card is hidden because it is facedown, the label will be updated in _pass()
            txtLyst[column]["text"] = "             "
            
            #load/get image
            _image = PhotoImage(file = Card.BACK_OF_CARD)

        #Update the image for a element of imgLyst
        imgLyst[column]["image"] = _image
    
    def _hit(self):
        """This represents the actions that will be triggered upon pressing _hitButton."""
        #If the game hasn't already been decided
        if self._end == False:
            #This is a similar to what is being done in the constructor for initializing the cards
            card = self._deck.deal()
            self._player.hit(card)

            #print "P", len(self._player)
            #If the player's hand consists of more cards than the amount of player card images on the screen
            if len(self._player) > len(self._pCardImgLabels):
                #Load new cards for the player and place them on the screen
                Lbls = self._loadCard(card, 1, len(self._player)-1)   #This returns a list containing an imgLabel and textLabel
                self._pCardImgLabels.append(Lbls[0])
                self._pCardNamLabels.append(Lbls[1])
            else:
                #Update the existing card
                self._updateCard(self._pCardImgLabels, self._pCardNamLabels, card, len(self._player)-1)
                
            if self._player.getPoints() > 21:
                #Display "you lose"
                self._endMsg["text"] = "PLAYER BROKE!!!!!!!!!!"
                self._end = True
                
            elif self._player.hasBlackjack():
                #Display "you win" with a text label!
                self._endMsg["text"] = "PLAYER WINS!!!!!!!!!!"
                self._end = True
            
    def _pass(self):
        """This represents the actions that will be triggered upon pressing _passButton.
        And pretty much just let's the dealer play and sees who wins. While ending the game in the process..."""
        #If the textLbl is None, then 
        if self._end == False:
            #This method is meant for ending the current game.
            self._end = True
            
            #Let the dealer finish its hand
            cards = self._dealer.hit(self._deck)
            
            #Check to see if cards isn't empty
            if cards != None:
                #The next dealer card to be placed is at column = 1
                count = 1
                #Load the card images for the dealer
                for card in cards:
                    #Check to see if this card position is already being used, dealer starts with one card!
                    if len(self._dCardImgLabels) > count:
                        #Update the card if it is already present
                        self._updateCard(self._dCardImgLabels, self._dCardNamLabels, card, count)
                    else:
                        #Create a new card and put it on the screen.
                        Lbls = self._loadCard(card, 3, count)   #Return a list containing an imgLabel and txtLabel
                        self._dCardImgLabels.append(Lbls[0])
                        self._dCardNamLabels.append(Lbls[1])
                    #Move on to the next position
                    count += 1

            #Gotta see if the dealer broke
            if self._dealer.getPoints() > 21:
                #Dealer Broke!
                self._endMsg["text"] = "DEALER BROKE!!!!!!!!!!"
                
            #Get the points for the dealer and player.
            #Then see who has more points and display the corresponding message
            elif self._player.getPoints() > self._dealer.getPoints():
                #Player wins!
                self._endMsg["text"] = "PLAYER WINS!!!!!!!!!!"
                
            elif self._player.getPoints() < self._dealer.getPoints():
                #Dealer wins!
                self._endMsg["text"] = "DEALER WINS!!!!!!!!!!"
            
            else:
                #Tie!!!!!!!!
                self._endMsg["text"] = "YOU TIED!!!!!!!!!!"

    def _new(self):
        """Sets up the game! Deals the cards to the player/dealer and updates the images on the window."""
        #If the player has cards in its hand from the last game
        #print "P", len(self._player)
        if len(self._player) > 0:
            #We gotta put the cards back in the deck
            cards = self._player.returnCards()
            self._deck.putInDeck(cards)
            #print len(self._player)

        #print "D", len(self._dealer)
        #If the dealer has cards in its hand from the last game
        if len(self._dealer) > 0:
            #We gotta put the cards back in the deck
            cards = self._dealer.returnCards()
            self._deck.putInDeck(cards)
            #print len(self._dealer)
            
        #Reset this, denotes the end of the current game
        self._end = False
        
        #Reset the endMsg
        self._endMsg["text"] = "                    "

        #Shuffle the deck before using it
        self._deck.shuffle()
        
        #Get the initial cards from the deck for the player and dealer!
        pCards = [self._deck.deal(), self._deck.deal()]
        dCards = [self._deck.deal()]

        #Give the player and dealer their initial cards.
        self._player.hit(pCards[0])
        self._player.hit(pCards[1])                 
        self._dealer.giveCard(dCards[0])
  
        #Put two image labels in the player and dealer's imgLabel lists
        for i in xrange(2):
            #Updating the player's card image at index i of the lists included.
            self._updateCard(self._pCardImgLabels, self._pCardNamLabels, pCards[i], i)

        #Updating the dealer's card image at index 0 and 1 of the lists included.
        self._updateCard(self._dCardImgLabels, self._dCardNamLabels, dCards[0], 0)
        self._updateCard(self._dCardImgLabels, self._dCardNamLabels, None, 1)

        #If there are more than two cards on the window from previous games
        if len(self._pCardImgLabels) > 2:
            #Flip those cards over
            for i in xrange(2,len(self._pCardImgLabels)):
                #Updating the player's card image at index i of the lists included.
                self._updateCard(self._pCardImgLabels, self._pCardNamLabels, None, i)

        #If there are more than two cards on the window from previous games
        if len(self._dCardImgLabels) > 2:
            #Flip those cards over
            for i in xrange(2,len(self._dCardImgLabels)):
                #Updating the player's card image at index i of the lists included.
                self._updateCard(self._dCardImgLabels, self._dCardNamLabels, None, i)

            
def main():
    #Initialize the game class -- its constructor will set up the GUI screen and initialize the neccessary stuff.
    game = Blackjack()
    game.mainloop()

main()
