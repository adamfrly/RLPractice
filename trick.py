# Should be explicit with typing at some point

class Trick:
    def __init__(self, trumpSuit, players):
        self.trumpSuit = trumpSuit
        self.leadSuit = 0
        self.playCount = 0
        self.currentWinner = 0
        self.players = players
        self.moves = []

    def leadMove(self, move):
        self.leadSuit = move.suit
        self.moves.append(move)
        self.currentWinner = self.players.isDealer.index(True)

    # This should be run once for every non-lead move
    def addMove(self, move):
        self.moves.append(move)
        if self.isBetterCard(self.moves[self.currentWinner], move):
            self.currentWinner = self.moves.index(move)

    # Three cases: Same suit, other trump current not, current trump other not.
    # If the current card
    def isBetterCard(self, currentBest, challenger):
        if currentBest.suit == challenger.suit:
            if currentBest.value > challenger.value:
                return False
            elif currentBest.value < challenger.value:
                return True
            else:
                print("Somehow you're comparing two cards of the same suit and value doofus.")
        elif currentBest.suit != self.trumpSuit and challenger.suit == self.trumpSuit:
            return True
        elif currentBest.suit == self.trumpSuit and challenger.suit != self.trumpSuit:
            return False
        else:
            print("You doofus, how could you have possibly ever gotten here?!?!")
        return False # Idk why I chose to default to a False response, I just did
    # def checkTrump():
    #
    # def checkOnSuit():
    #
    # def winner():

