from dataclasses import dataclass, field
from random import shuffle
from card import Card


def make_deck():
    return [Card(rank, suit) for suit in range(1, 5) for rank in range(9, 15)]


@dataclass
class Deck:
    cards: list[Card] = field(default_factory=make_deck)

    def shuffle(self):
        for i in range(0, 3):
            shuffle(self.cards)

    def getTopCard(self):
        return self.cards.pop()
