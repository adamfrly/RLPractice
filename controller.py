from table import Table
from player import Player


class Controller:
    def GameSetup(self):
        print("Starting Euchre! \n There are four players, for now all of them are computers.")

        Player1 = Player()
        Player2 = Player()
        Player3 = Player()
        Player4 = Player()

        table = Table(Player1, Player2, Player3, Player4)
    
    def playGame(self, tble):
        print("Starting the game now.")

        round = 1

        while not tble.gameover:
            print(f"Starting Round: {round}")
            print(f"Current Score: Team 1 has {Table.team1score} points and Team 2 has {Table.team2score} points.")

            tble.deal()
            tble.chooseTrump()
            tble.playHand()

            round += 1
            tble.shiftDeal()

