# Individual player class


class Player:
    def __init__(self, card1, card2):
        self.cards = [card1, card2]
        self.health = 2

    # testing functions (temporary)
    def print(self):
        print(self.cards[0].name)
