from deck import Deck
from player import Player

class Table:

    gameover = False

    def __init__(self, player1, player2, player3, player4):
        self.players = [player1, player2, player3, player4]
        self.team1Score = 0
        self.team2Score = 0
        self.deck = Deck()

    # def playHand():
    #     return blah
    
    def deal(self):
        self.deck.shuffle()
        for i in range(20):
            self.players[i % 4].cards.append(self.deck.getTopCard())
        self.kitty = self.deck
    # def chooseTrump():

    # def shiftDeal():

one = Player()
two = Player()
three = Player()
four = Player()

table = Table(one, two, three, four)
table.deal()
print(one.cards)
print(two.cards)
print(three.cards)
print(four.cards)
print(table.kitty)
