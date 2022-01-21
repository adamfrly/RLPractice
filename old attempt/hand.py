# from trick import Trick
from deck import Deck
from dataclasses import dataclass, field
from card import Card
# Should be explicit with typing at some point


@dataclass
class Hand:
    kitty: Deck
    flipped: Card = field(init=False)
    # currentTrick: Trick = field(init=False)
    # pastTricks: list[Trick] = field(init=False)
    team1Tricks: int = field(init=False, default=0)
    team2Tricks: int = field(init=False, default=0)
    dealer: int = field(init=False, default=0)
    leader: int = field(init=False, default=0)
    caller: int = field(init=False, default=0)
    trump: int = field(init=False, default=0)

    def __post_init__(self):
        self.flipped = self.kitty.getTopCard()

    def playTrick(self):
        """
        Plays trick
        """
