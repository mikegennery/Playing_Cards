# Michael Gennery
# Pack of Cards
# August 2020
# Pontoon

from Playing_Cards import *

"""
This is a game where the player must draw cards or twist and gain as high a score as they can without going over 21.
"""

print('PONTOON')
print('_______\n')

# Create class objects

pontoon_deck = deck()
player_hand = hand()

# Scores

score_dict = {
    'A' : 11, # Ace
    'K' : 10, # King
    'Q' : 10, # Queen
    'J' : 10, # Jack
    'T' : 10, # Ten
    '9' : 9,  # Nine
    '8' : 8,  # Eight
    '7' : 7,  # Seven
    '6' : 6,  # Six
    '5' : 5,  # Five
    '4' : 4,  # Four
    '3' : 3,  # Three
    '2' : 2,  # Two
    }

quit_flag = False
    
while not quit_flag:

    player_score = 0 # Reset score for a new game
    card_score = 0
    present_card = ''
    present_suit = ''
    game_over = False
    ace_flag = 0 # This is to enable the Ace card to score a 1 or an 11
    pontoon_deck.shuffle()
    
    while not game_over:

        player_hand.deal(pontoon_deck, 1) # Deal next card
        present_card = player_hand.hand[-1]

        print('\nPLAYER HAND: ')
        for card in player_hand.hand:
            print('\t',card_to_text(card))

        present_suit = present_card[0]
        
        if present_suit == 'A': # This is to enable the Ace card to score a 1 or an 11
            ace_flag += 1
            
        present_score = score_dict[present_suit]
        player_score += present_score # Update Player's score
        
        if player_score > 21 and ace_flag > 0: # This is to enable the Ace card to score a 1 or an 11
            ace_flag -= 1
            player_score -= 10

        print('\nSCORE: ',player_score)

        if player_score > 21: 
            print('\nYOU ARE BUST\nYOU LOSE!!')
            game_over = True
        else:
            option = ''
            valid_input = False

            while not valid_input:
                option = input('\n(S)tick or (T)wist)? (S/T) : ')

                if option == 'S' or option == 's': # STICK
                    option = 's'
                    valid_input = True
                    
                    print('Your Final score is ',player_score) # FINAL SCORE
                    if len(player_hand.hand) >= 5:
                        print('FIVE CARD TRICK!! WELL DONE')
                    if player_score == 21:
                        print('MAXIMUM SCORE!! WELL DONE')
                    game_over = True

                elif option == 'T' or option == 't': # TWIST - Let's twist again like we did last summer!!
                    option = 't'
                    valid_input = True
                    
                else:
                    print('You must reply S - Stick or T - Twist!')
            
    option = ''
    valid_input = False

    while not valid_input:
        option = input('\nDo you wish to play again? (Y/N) : ')
        if option == 'Y' or option == 'y' or option == 'YES' or option == 'yes':
            option = 'y'
            valid_input = True
            player_hand.return_all(pontoon_deck)
        elif option == 'N' or option == 'n' or option == 'NO' or option == 'no':
            option = 'n'
            valid_input = True
            quit_flag = True
        else:
            print('You must reply Y - YES or N - NO!')

