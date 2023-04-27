# this file contains necessary functions to create a game of blackjack
import blackjack as bj
# take a players initial bet amount
def take_bet(chips):
    print(f'Chips Available : {chips.total}')
    while True:
        try:
            player_bet = int(input('Enter your bet: '))
        except ValueError:
            player_bet = int(input('You entered an incorrect value please make sure you enter a number: '))
        else:
            if player_bet > chips.total:
                print('Insufficient funds! Enter an amount you have: ')
            else:
                chips.bet = player_bet
                break


# take a card from the deck and add it to the player hand
def hit(deck, hand):
    card = deck.deal()
    hand.add_to_hand(card)
    hand.check_for_aces()

# when a player chooses not to hit.
def stand():
    pass

# check if player hand is more than 21
def check_for_bust(hand):
    return hand.value > 21


# hit the dealer deck until the value is 17
def dealer(deck, dealer_hand):
    while dealer_hand.value < 17:
        hit(deck, dealer_hand)


# check if dealer is closer to 21
def compare_hands(dealer_hand, player_hand, chips):
    if dealer_hand.value > player_hand.value and dealer_hand.value <= 21:
        chips.loose_bet()
        return False
    elif player_hand.value > dealer_hand.value and player_hand.value <= 21:
        chips.win_bet()
        return True


# display the dealer and player hand
def display_hands(player_hand, dealer_hand, hide_dealer_card=True):
    print("\nDealer's Hand:")
    if hide_dealer_card:
        print(" <hidden card>")
        print(" ", dealer_hand.cards[1])
    else:
        for card in dealer_hand.cards:
            print(" ", card)

    print("\nPlayer's Hand:")
    for card in player_hand.cards:
        print(" ", card)

# reshuffle deck and remove cards from hand
def new_round(deck, player_hand, dealer_hand):
    deck = bj.Deck()
    deck.shuffle_deck()
    player_hand.cards.clear()
    dealer_hand.cards.clear()

    
    






