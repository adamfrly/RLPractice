from dataclasses import dataclass
from typing import ClassVar
# Should be explicit with typing at some point


@dataclass
class Card:
    value: int
    suit: int
    _suits: ClassVar[dict] = {1: 'Spades', 2: 'Clubs', 3: 'Hearts', 4: 'Diamonds'}
    _values: ClassVar[dict] = {9: 'Nine', 10: 'Ten', 11: 'Jack', 12: 'Queen', 13: 'King', 14: 'Ace', 15: 'LBower', 16: 'RBower'}
    
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

    def isRBower(self, trumpSuit):
        return self.suit == trumpSuit and self.value == 11

    def setTrumpValue(self, trumpSuit):
        if self.isRBower(trumpSuit):
            self.value = 16
        elif self.isLBower(trumpSuit):
            self.value = 15