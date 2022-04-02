# Main Coup game class and cards
from random import choice
from Player import Player


class Card:
    def __init__(self, art, name, steal, block_steal, block_kill, kill, tax, swap, inquisitor):
        self.art = art
        self.name = name
        self.steal = steal
        self.block_steal = block_steal
        self.block_kill = block_kill
        self.kill = kill
        self.tax = tax
        self.swap = swap
        self.inquisitor = inquisitor


class Coup:
    def __init__(self, players, inquisitor: bool, ambassador: bool, contessa: bool, timer):
        self.player_num = players
        self.timer = timer
        self.turn = 1
        self.cards = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        # checking custom game rules
        if inquisitor is True:
            self.inquisitor = Card(1, "Inquisitor", False, True, False, False, False, False, True)
            self.cards.append(5)
            self.cards.append(5)
            self.cards.append(5)
        else:
            self.inquisitor = None
        if ambassador is True:
            self.ambassador = Card(1, "Ambassador", False, False, True, False, False, True, False)
        else:
            self.ambassador = Card(1, "Ambassador",False, True, False, False, False, True, False)
        if contessa is True:
            self.contessa = Card(1, "Contessa",False, True, True, False, False, False, False)
        else:
            self.contessa = Card(1, "Contessa",False, False, True, False, False, False, False)

        self.captain = Card(1, "Captain",True, True, False, False, False, False, False)
        self.assassian = Card(1, "Assassian", False, False, False, True, False, False, False)
        self.duke = Card(1, "Duke",False, False, False, False, True, False, False)

        self.card_map = {0: self.ambassador, 1: self.contessa, 2: self.captain, 3: self.assassian, 4: self.duke,
                         5: self.inquisitor}

        self.players = [Player(self.card_map[self.add_card()], self.card_map[self.add_card()])
                        for i in range(self.player_num)]

    def add_card(self):
        card = choice(self.cards)
        self.cards.remove(card)
        return card
