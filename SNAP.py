# Michael Gennery
# Pack of Cards
# Snap
# August 2020

from Playing_Cards import *

import time

"""
This is a simple game where each player plays one card at a time and when two cards match, the first person to say SNAP wins
"""

# VARIABLES

snap_area = area() # Area for played cards to be placed
snap_deck = deck() # Deck for playing cards
computer = hand()  # Computer's hand
player = hand()    # Player's hand
player_card = ''
computer_card = ''
quit_prog = False
snap = False       # SNAP!!
option = ''
valid_input = False

print('SNAP')
print('____')

pause = input('\nPRESS RETURN TO START PLAYING')

snap_deck.shuffle()

player.deal(snap_deck, 26) # Deal half the cards to the player
computer.deal(snap_deck, 26) # and the other half to the computer

while not quit_prog:

    player.play_card(player.hand[-1],snap_area) # Player deals a card
    player_card = snap_area.area[-1]
    computer.play_card(computer.hand[-1],snap_area) # Computer deals a card
    computer_card = snap_area.area[-1]

    print('\n')
    print('PLAYER:\t\t',card_to_text(player_card)) # Print the last 2 cards to be dealt
    print('COMPUTER:\t',card_to_text(computer_card))

    time.sleep(2) # This gives the player time to say "SNAP"

    if player_card[0] == computer_card[0]:
        snap = True
        print('\n!!\tSNAP\t!!') # You need to say SNAP before the computer does!
        time.sleep(2)

        option = ''
        valid_input = False

        while not valid_input:
            option = input('\nDo you wish to play again? (Y/N) : ')
            option = option.lower()
            if option == 'y' or option == 'yes':
                option = 'y'
                valid_input = True
            elif option == 'n' or option == 'no':
                option = 'n'
                valid_input = True
                quit_prog = True
            else:
                print('You must reply Y - YES or N - NO!')

            if option == 'y':
                print('\nREDEALING!!')
                snap_area.return_all(snap_deck) # Return everything to the deck and deal again
                computer.return_all(snap_deck)
                player.return_all(snap_deck)
                snap_deck.shuffle()
                player.deal(snap_deck, 26) # Deal half the cards to the player
                computer.deal(snap_deck, 26) # and the other half to the computer

    if len(computer.hand) == 0 and len(player.hand) == 0: # If all the cards have been played, return everything to the deck and deal again
        print('\nREDEALING!!')
        snap_area.return_all(snap_deck)
        computer.return_all(snap_deck)
        player.return_all(snap_deck)
        snap_deck.shuffle()
        player.deal(snap_deck, 26) # Deal half the cards to the player
        computer.deal(snap_deck, 26) # and the other half to the computer

