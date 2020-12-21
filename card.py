class Card:

    _suits = {1: 'Spades', 2: 'Clubs', 3: 'Hearts', 4: 'Diamonds'}
    _values = {9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace', 15: 'LBower', 16: 'RBower'}

    def __init__(self, value, suit):
        self.suit = suit
        self.value = value
    
    def getSuit(self):
        return self.suit
    
    def getValue(self):
        return self.value
    
    def isLBower(self, trumpSuit):
        if trumpSuit == 1 and self.suit == 2 and self.value == 11:
            return True
        elif trumpSuit == 2 and self.suit == 1 and self.value == 11:
            return True
        elif trumpSuit == 3 and self.suit == 4 and self.value == 11:
            return True
        elif trumpSuit == 4 and self.suit == 3 and self.value == 11:
            return True
        return False

    def setTrumpValue(self, trumpSuit):
        if self.suit == trumpSuit and self.value == 11:
            self.value = 16
        elif self.isLBower(trumpSuit):
            self.value = 15
    
    def __eq__(self, other):
        return self.value == other.value and self.suit == other.suit
    
    def __str__(self):
        s = self._suits.get(self.suit)
        v = self._values.get(self.value)
        return f"{v} of {s}"

    def __repr__(self):
        return f"{self._values.get(self.value)} of {self._suits.get(self.suit)}"