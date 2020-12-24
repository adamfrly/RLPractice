class Player:
    def __init__(self):
        self.cards = []
        self.isDealer = False

    def isLegalMove(self, currentTrick, attemptedPlay):
        if not currentTrick.checkOnSuit(attemptedPlay):
            for otherCard in self.cards:
                if (currentTrick.checkOnSuit(otherCard)) and (otherCard != attemptedPlay):
                    return False
        return True

    # This entire function is very arbitrary and can probably be refined (by looking into winning prob of each hand)
    def analyzeHand(self, trumpSuit):
        score = 0
        spade = 0
        club = 0
        heart = 0
        diamond = 0
        for card in self.cards:
            if card.suit == 1: spade = 1
            elif card.suit == 2: club = 1
            elif card.suit == 3: heart = 1
            elif card.suit == 4: diamond = 1
            else: print("Idk how you managed to get an invalid suit in here but you did")

            score += card.value - 9
            if card.suit == trumpSuit: score += 6
        numSuits = spade + club + heart + diamond
        score = 2*score/numSuits
        return score

    # Right now this handles ties by taking the first "worst" card it sees. Could break ties by number of suits
    def findWorstCard(self, trumpSuit):
        min = 25
        currentVal = 0
        worst = None
        for card in self.cards:
            currentVal = card.value
            if card.suit == trumpSuit:
                currentVal += 6
            if currentVal < min:
                min = currentVal
                worst = card
        return worst

# Class for a non-reinforcement learning based computer. These are needed to train the agent players
# class AutoPlayer(Player):

# Class for the reinforcement learning players. Will (hopefully) eventually be able to play against each other
# class AgentPlayer(Player):

