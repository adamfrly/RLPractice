class Trick:
    def __init__(self, trumpSuit, players):
        self.trumpSuit = trumpSuit
        self.leadSuit = 0
        self.playCount = 0
        self.currentWinner = 0
        self.players = players


    # def leadMove():
    #
    # def addMove():

    # Three cases: Same suit, other trump current not, current trump other not.
    def isBetterCard(self, currentCard, otherCard):
        if currentCard.suit == otherCard.suit:
            if currentCard.value > otherCard.value:
                return False
            elif currentCard.value < otherCard.value:
                return True
            else:
                print("Somehow you're comparing two cards of the same suit and value doofus.")
        elif currentCard.suit != self.trumpSuit and otherCard.suit == self.trumpSuit:
            return True
        elif currentCard.suit == self.trumpSuit and otherCard.suit != self.trumpSuit:
            return False
        else:
            print("You doofus, how could you have possibly ever gotten here?!?!")
        return False # Idk why I chose to default to a False response, I just did
    # def checkTrump():
    #
    # def checkOnSuit():
    #
    # def winner():

