# Main Coup game class and cards


class Card:
    def __init__(self, art, steal, block_steal, block_kill, kill, tax, swap, inquisitor):
        self.art = art
        self.steal = steal
        self.block_steal = block_steal
        self.block_kill = block_kill
        self.kill = kill
        self.tax = tax
        self.swap = swap
        self.inquisitor = inquisitor


class Coup:
    def __init__(self, players, inquisitor: bool, ambassador: bool, contessa: bool, timer):
        self.players = players
        self.timer = timer
        self.cards = [0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4, 4]
        # checking custom game rules
        if inquisitor is True:
            self.inquisitor = Card(1, False, True, False, False, False, False, True)
            self.cards.append(5)
            self.cards.append(5)
            self.cards.append(5)
        if ambassador is True:
            self.ambassador = Card(1, False, False, True, False, False, True, False)
        else:
            self.ambassador = Card(1, False, True, False, False, False, True, False)
        if contessa is True:
            self.contessa = Card(1, False, True, True, False, False, False, False)
        else:
            self.contessa = Card(1, False, False, True, False, False, False, False)

        self.captain = Card(1, True, True, False, False, False, False, False)
        self.assassian = Card(1, False, False, False, True, False, False, False)
        self.duke = Card(1, False, False, False, False, True, False, False)
