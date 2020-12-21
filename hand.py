from trick import Trick
from deck import Deck


class Hand:
    def __init__(self):
        self.team1Tricks = 0
        self.team2Tricks = 0
        self.dealer = 0
        self.leader = 0
        self.caller = 0
        self.trump = 0
        self.currentTrick = Trick()
        self.pastTricks = []

    def playTrick(self):
        """
        Plays trick
        """