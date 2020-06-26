import random

class Deck():

    def __init__(self):
        self.deck = []

    def build(self):
        suits = ['Club', 'Spade', 'Heart', 'Diamond']
        values = ['J', 'Q', 'K', 'A'] + list(range(2, 11))
        for suit in suits:
            for num in values:
                self.deck.append(tuple([num,suit]))

    def show(self):
       print(self.deck)



deck = Deck()
deck.build()
deck.show()