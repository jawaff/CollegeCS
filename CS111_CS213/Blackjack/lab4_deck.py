from random import shuffle

class Card (object):
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
    BACK_OF_CARD = "DECK/b.gif"
    
    
    def __init__(self, rank, suit):
        """Sets up the variables that belong to each card."""
        self.rank = rank
        self.suit = suit
        self.fileName = "DECK/" + str(rank) + str(suit[0].lower()) + ".gif"

    def __str__(self):
        """For the text display of each card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = "Jack" 
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of  ' + self.suit.lower()
   

class Deck (object):
    def __init__(self):
        #Initialization of the list that will hold the cards
        self._cards = []
        #Putting all the cards into the list
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                #Get an instance of the Card class for the card's representation
                c = Card(rank,suit)
                #Put the instance in the list
                self._cards.append(c)
    def shuffle(self):
        """Shuffle the cards list."""    
        shuffle(self._cards)

    def putInDeck(self, cards):
        """This is for putting cards back into the deck."""
        self._cards += cards
    
    def deal(self):
        """Removes and returns the top card or None if the deck is empty"""
        if len(self) == 0:
            return None
        else:
            return self._cards.pop(0) 
            
    def __len__(self):
        """The len of the deck is equal to the len() of the Deck's cards"""
        return len(self._cards)
        
    def __str__(self):
        """The textual display of the Deck object"""
        result = ' '
        for c in self._cards:
            result = result + str(c) + '\n'
        return result
