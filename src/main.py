# imported necessary modules for main programme.
import game_functions, blackjack as bj


# define game properties 
game = False
player_chips = bj.Chips()

# define player and dealer hands
player_hand = bj.Hand()
dealer_hand = bj.Hand()

# create and shuffle deck
deck = bj.Deck()
deck.shuffle_deck()


# main program loop
if __name__ == "__main__":
     # welcome player to the game
     start_game = input('Welcome to Blackjack! Please press y (to play) or n (to exit): ').lower()
    # check if player wants to play
     if start_game == 'y':
          game = True
          while game:

               # player turn loop
               while player_chips.total > 0:
                    game_functions.take_bet(player_chips)
                    # deal cards to player and dealer -> two cards each
                    print('\n')
                    print('Dealing cards to player .... ')
                    player_hand.add_to_hand(deck.deal())
                    player_hand.add_to_hand(deck.deal())
                    print('\n')
                    print('Dealing cards to dealer .... ')
                    dealer_hand.add_to_hand(deck.deal())
                    dealer_hand.add_to_hand(deck.deal())

                    print('\n')
                    game_functions.display_hands(player_hand, dealer_hand, True)
                    print('\n')

                    # ask player if they want to hit
                    try:
                         player_hit = input('Hit or Stand (h/s): ').lower()
                    except:
                         print('Please enter h (hit) or s (stand): ')

                    # if the player chooses to hit
                    if player_hit == 'h':
                         game_functions.hit(deck, player_hand)
                    # if player chooses not to hit     
                    elif player_hit == 's':
                         game_functions.stand()
                    
                    # check if player hand is bust
                    if game_functions.check_for_bust(player_hand):
                         # if hand is bust loose the bet
                         player_chips.loose_bet()
                         game_functions.display_hands(player_hand, dealer_hand, False)
                         print('\n')
                         print(f'Dealer Wins! You LOST! Remaining Chips: {player_chips.total}')
                         if player_chips.total > 0: 
                              game_functions.new_round(deck, player_hand, dealer_hand)
                              print('\n')
    
                    else:
                         # increase dealer hand till > 17
                         game_functions.dealer(deck, dealer_hand)

                    # check the players hand value against the dealers hand value
                    if game_functions.compare_hands(dealer_hand, player_hand, player_chips):
                         game_functions.display_hands(player_hand, dealer_hand, False)
                         print('\n')
                         print(f'Player Wins! Dealer LOST! Remaining Chips: {player_chips.total}')
                         if player_chips.total > 0: 
                              game_functions.new_round(deck, player_hand, dealer_hand)
                              print('\n')

                           
     else:
          game = False
     




               
               




