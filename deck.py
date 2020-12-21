from random import shuffle
from card import Card


class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in range(1, 5) for rank in range(9, 15)]

    def shuffle(self):
        for i in range(0, 3):
            shuffle(self.cards)

    def getTopCard(self):
        return self.cards.pop()

    # NEED AN REPR AND STR METHOD

