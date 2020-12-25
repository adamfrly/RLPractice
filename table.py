# Should be explicit with typing at some point
from deck import Deck
from player import Player
from hand import Hand


class Table:

    gameover = False

    def __init__(self, player1, player2, player3, player4):
        self.players = [player1, player2, player3, player4]
        self.team1Score = 0
        self.team2Score = 0
        self.deck = Deck()
        self.kitty = None
        self.dealer = 0

    def deal(self):
        self.deck.shuffle()
        for i in range(20):
            self.players[i % 4].cards.append(self.deck.getTopCard())
        self.kitty = self.deck

    def shiftDeal(self):
        self.players[self.dealer].isDealer = False
        self.dealer = (self.dealer + 1) % 4
        self.players[self.dealer].isDealer = True

    # Needs to run through all suits, and all players, (right now it's broken).
    # def chooseTrump(self): # Returns the index of the person who called trump. If -1, then it's screw the dealer
    #     flipped = self.kitty.getTopCard()
    #     calledTrump = -1
    #     for player in self.players:
    #         calledTrump = self.players.index(player) if player.orderUp(flipped) else -1
    #         if calledTrump and self.dealer == self.players.index(player): # Dealer picked up
    #         elif calledTrump and (self.dealer + 2 % 4) == self.players.index(player): # Dealer's partner picked up
    #         elif

        # Get a player to choose Trump
        # Change card values to their trump values (Bowers)
        #     for player in self.players:
        #         for card in player.cards:
        #             if card.isLBower(trumpSuit=trump):
        #                 card.value = 15
        #                 card.suit = trump # This way the left bower will be recognized as the trump suit
        #             elif card.isRBower(trumpSuit=trump):
        #                 card.value = 16
        return trump

    # def playHand():
    #     return blah


one = Player()
two = Player()
three = Player()
four = Player()

table = Table(one, two, three, four)
table.deal()
print("Player one's hand: ", one.cards)
print("Player two's hand: ", two.cards)
print("Player three's hand: ", three.cards)
print("Player four's hand: ", four.cards)
print("The Kitty: ", table.kitty)

blah = Hand(table.kitty)

print("Kitty without top card: ", blah.kitty)
print("Flipped Card: ", blah.flipped)
