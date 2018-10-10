class Player(object):

    def __init__(self):
        """The player's constructor does nothing!"""
        #Initializes the player's hand
        self._cards = []
    def __str__(self):
        """The player's textual display is managed here."""
        result = ", ".join(map(str, self._cards))
        result += "\n  " + str(self.getPoints()) + " points"
        return result

    def __len__(self):
        """Returns the length of the player's hand."""
        return len(self._cards)

    def hit(self, card):
        """Add a card to the player's hand"""
        self._cards.append(card)

    def returnCards(self):
        """This is for putting the cards back into the deck inbetween games."""
        cards = []
        for i in xrange(len(self._cards)):
            cards.append(self._cards.pop(-1))
        return cards
    
    def getPoints(self):
        """Returns the points of the player's hand."""
        count = 0
        for card in self._cards:
            if card.rank > 9:
                count += 10
            elif card.rank == 1:
                count += 11
            else:
                count += card.rank
        for card in self._cards:
            if count <= 21:
                break
            elif card.rank == 1:
                count -= 10
        return count

    def hasBlackjack(self):
        return len(self._cards) == 2 and self.getPoints() == 21
        
        
class Dealer(Player):
    def __init__(self):
        """The dealer's constructor"""
        Player.__init__(self)
        self._showOneCard = True
        
    def __str__(self):
        """The textual display of the Dealer is managed here."""
        return Player.__str__(self)

    def giveCard(self, card):
        """Add a card to the dealer's hand"""
        self._cards.append(card)
        self._showOneCard = True

    def hit(self, deck):
        """Add a card to the dealer's hand"""
        self._showOneCard = False
        #I will use this list to return all the fileNames of the cards being dealt to the dealer
        cards = []
        while self.getPoints() < 17:
            card = deck.deal()
            self._cards.append(card)
            cards.append(card)
        return cards
