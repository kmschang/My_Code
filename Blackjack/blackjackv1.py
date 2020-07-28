import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven','Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10,
          'Queen': 10, 'King': 10, 'Ace': 11}

class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:

    def __init__(self):

        self.deck = []

        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)

                self.deck.append(created_card)

    def shuffle(self):
        random.shuffle(self.deck)

    def deal_one(self):
        return self.deck.pop()



deck = Deck()
deck.shuffle()

firstcard = deck.deal_one()

print (firstcard)

secondcard = deck.deal_one()

print (secondcard)
