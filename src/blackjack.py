# import necessary modules
import random

# global variables define tuple and key dictionary for card suit and number.

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
suits = ('Spades', 'Hearts', 'Diamonds', 'Clubs')
values = {'Ace':11, 'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10}

# define card class attributes

class Card:
    
    # initialize class objectss
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
        
    # return card objects in string format
    def __str__(self):
        return self.rank + ' of ' + self.suit
    

class Deck:

    # add cards to the deck -> creating the deck format 
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    
    # return the deck attributes in string format (testing only!)
    def __str__(self):
        actual_deck = ' '
        for card in self.deck:
            actual_deck += '\n' + card.__str__()
        
        return 'This deck has: ' + actual_deck
    
    # shuffle the deck
    def shuffle_deck(self):
        return random.shuffle(self.deck)

    # deal a card to a hand -> removing a card from the deck
    def deal(self):
        single_card = self.deck.pop(0)
        return single_card
    
class Hand:

    # create a list to store player cards in hand
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
    
    # add a card to a players hand
    def add_to_hand(self, card):
        self.cards.append(card)
        self.value += values[card.rank]

        # log another ace into a seprate list
        if card.rank == 'Ace':
            self.aces += 1

    # check to see if ace value must be 1 or 11.
    def check_for_aces(self):
        while self.value > 21 and self.aces:
            self.value += 11
            self.aces += 1 


class Chips:

    # create chip attributes
    def __init__(self):
        self.total = 100
        self.bet = 0

    # add original bet to total.
    def win_bet(self):
        self.total += self.bet
    
    # subtract original bet from total
    def loose_bet(self):
        self.total -= self.bet


