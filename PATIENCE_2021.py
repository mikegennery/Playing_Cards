# Michael Gennery
# PATIENCE / SOLITAIRE
# July 2021

from Playing_Cards_2021 import *

"""
This is a game for one player aka. Solitaire, where the player needs to arrange cards in a certain order according to certain rules
"""

print('\nPATIENCE / SOLITAIRE')
print('____________________\n\n')

# Create class objects

# These are the starting areas for the cards to be played in. The face card will be rowx[0]

row6 = area()
row5 = area()
row4 = area()
row3 = area()
row2 = area()
row1 = area()

# These are the areas that the player will place the ordered cards into for each suit

hearts = area()
diamonds = area()
spades = area()
clubs = area()

# Main deck

main_deck = deck()
main_deck_card = '' # This indicates which is the current card in the deck
current_card = 0 # This indicates which card in the main deck is the current card
card_in_play = '' # This indicates which card is currently being played
card_dest = '' # This is the card the card_in_play will be placed on

# VARIABLES

quit_prog = False
game_over = False
locations = ['A','a','B','b','C','c','D','d','E','e','F','f','G','g','H','h','I','i','J','j','K','k','DEAL','deal','QUIT','quit','x','X']
move_s = '' # Source Location
move_d = '' # Destination Location
valid_input = False
deal_card = False


# These indicate which cards should be displayed

row6_show = 0 # These variables indicate which cards should be shown
row5_show = 0 # with the top card (0) as the default
row4_show = 0 # This value is increased as more cards are added to the row
row3_show = 0
row2_show = 0
row1_show = 0

show_card = 0


#
# Display card rows
#


def display_rows(row6,row5,row4,row3,row2,row1):
    
    print('\n\nA:\t', end = '')

    show_card = len(row6)

    for card in reversed(row6): # ROW 6

        show_card = show_card - 1

        if show_card <= row6_show: # This indicates which cards should be shown
            print(card_to_text(card),end = '') # Only display the face card
            if card[1] == 'H' or card[1] == 'D':
                print(' - RED ',end = '')
            else:
                print(' - BLACK ',end = '')
        else:
            print('CARD ',end ='') # Hide all other cards

        print(' / ',end = '')

    print('\n\nB:\t', end = '')

    show_card = len(row5)

    for card in reversed(row5): # ROW 5

        show_card = show_card - 1

        if show_card <= row5_show: # This indicates which cards should be shown
            print(card_to_text(card),end = '') # Only display the face card
            if card[1] == 'H' or card[1] == 'D':
                print(' - RED ',end = '')
            else:
                print(' - BLACK ',end = '')
        else:
            print('CARD ',end ='') # Hide all other cards

        print(' / ',end = '')
    
    print('\n\nC:\t', end = '')

    show_card = len(row4)
          
    for card in reversed(row4): # ROW 4

        show_card = show_card - 1

        if show_card <= row4_show: # This indicates which cards should be shown
            print(card_to_text(card),end = '') # Only display the face card
            if card[1] == 'H' or card[1] == 'D':
                print(' - RED ',end = '')
            else:
                print(' - BLACK ',end = '')
        else:
            print('CARD ',end ='') # Hide all other cards

        print(' / ',end = '')

    print('\n\nD:\t', end = '')

    show_card = len(row3)
          
    for card in reversed(row3): # ROW 3

        show_card = show_card - 1

        if show_card <= row3_show: # This indicates which cards should be shown
            print(card_to_text(card),end = '') # Only display the face card
            if card[1] == 'H' or card[1] == 'D':
                print(' - RED ',end = '')
            else:
                print(' - BLACK ',end = '')
        else:
            print('CARD ',end ='') # Hide all other cards

        print(' / ',end = '')

    print('\n\nE:\t', end = '')

    show_card = len(row2)
          
    for card in reversed(row2): # ROW 2

        show_card = show_card - 1

        if show_card <= row2_show: # This indicates which cards should be shown
            print(card_to_text(card),end = '') # Only display the face card
            if card[1] == 'H' or card[1] == 'D':
                print(' - RED ',end = '')
            else:
                print(' - BLACK ',end = '')
        else:
            print('CARD ',end ='') # Hide all other cards

        print(' / ',end = '')

    print('\n\nF:\t', end = '')

    show_card = len(row1)
          
    for card in reversed(row1): # ROW 1

        show_card = show_card - 1

        if show_card <= row1_show: # This indicates which cards should be shown
            print(card_to_text(card),end = '') # Only display the face card
            if card[1] == 'H' or card[1] == 'D':
                print(' - RED ',end = '')
            else:
                print(' - BLACK ',end = '')
        else:
            print('CARD ',end ='') # Hide all other cards

        print(' / ',end = '')


#
# Display sorted cards
#


def display_sorted_cards(hearts,diamonds,clubs,spades):

    print('\n\n')

    if len(hearts) == 0:
        print('G:\tHEARTS.........:')
    else:    
        print('G:\tHEARTS.........: ',card_to_text(hearts[0]))

    print('\n')
          
    if len(diamonds) == 0:
        print('H:\tDIAMONDS.......:')
    else:    
        print('H:\tDIAMONDS.......: ',card_to_text(diamonds[0]))

    print('\n')
          
    if len(clubs) == 0:
        print('I:\tCLUBS..........:')
    else:    
        print('I:\tCLUBS..........: ',card_to_text(clubs[0]))

    print('\n')
          
    if len(spades) == 0:
        print('J:\tSPADES.........:')
    else:
        print('J:\tSPADES.........: ',card_to_text(spades[0]))


#
# MAIN PROGRAM
#


while not quit_prog:
    
    # Prepare for new game

    main_deck.shuffle()

    main_deck.play_card(main_deck,row6,6)
    main_deck.play_card(main_deck,row5,5)
    main_deck.play_card(main_deck,row4,4)
    main_deck.play_card(main_deck,row3,3)
    main_deck.play_card(main_deck,row2,2)
    main_deck.play_card(main_deck,row1,1)

    # These indicate which cards should be displayed

    row6_show = 0 # These variables indicate which cards should be shown
    row5_show = 0 # with the top card (0) as the default
    row4_show = 0 # This value is increased as more cards are added to the row
    row3_show = 0
    row2_show = 0
    row1_show = 0

    show_card = 0

    game_over = False

    while not game_over:

        display_rows(row6.area,row5.area,row4.area,row3.area,row2.area,row1.area)

        display_sorted_cards(hearts.area,diamonds.area,clubs.area,spades.area)

        if current_card < 0:
            current_card = 0

        if len(main_deck.deck) > 0:
            main_deck_card = main_deck.deck[current_card]
            print('\n\nK:\tCURRENT_CARD...: ',card_to_text(main_deck_card), end = '')
            if main_deck_card[1] == 'H' or main_deck_card[1] == 'D':
                print(' - RED')
            else:
                print(' - BLACK')
        else:
            print('\n\nK:\tCURRENT_CARD...:')


        print('\n\nType DEAL for new card')
        print('Type QUIT to end program')

        print('\nEnter K for the source and destination to deal a new card!')

        valid_input = False        
        while not valid_input:
            move_s = input('\n\nENTER SOURCE LOCATION.......(A - K): ')
            move_s = move_s.upper()
            if move_s not in locations:
                print('Invalid location')
            else:
                valid_input = True
        
        if move_s == 'DEAL':
            deal_card = True
        else:
            deal_card = False

        if move_s == 'QUIT':
            quit_prog = True
            game_over = True
        
        valid_input = False
        while not valid_input and not deal_card and not quit_prog:
            move_d = input('\n\nENTER DESTINATION LOCATION..(A - J) (X for void): ')
            move_d = move_d.upper()
            if (move_d not in locations or move_d == move_s) and (move_s != 'K' and move_d != 'K'):
                print('Invalid location')
            elif move_d == 'K' and (move_s != 'K'):
                print('Invalid location')
            elif move_s == 'K' and (move_d == ''):
                print('Invalid location')
            else:
                valid_input = True

        if move_s == 'DEAL' or move_d == 'DEAL' or (move_s == 'K' and move_d == 'K'):
            deal_card = True
            print('\n')
            current_card += 3 # Move along three cards
            if current_card >= len(main_deck.deck):
                current_card = 0 # Go back to the beginning of the deck if you reach the end
        else:
            deal_card = False

        if move_d == 'QUIT':
            quit_prog = True
            game_over = True
        
        if not quit_prog and not game_over and not deal_card and move_d != 'X':

            ##
            ## Move from source
            ##

            valid_input = True # This is a flag to indicate if the move is valid

            if move_s == 'A':
                if len(row6.area) > 0: # This ensures you don't move from an empty area
                    card_in_play = row6.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')
                    
            elif move_s == 'B':
                if len(row5.area) > 0:
                    card_in_play = row5.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')

            elif move_s == 'C':
                if len(row4.area) > 0:
                    card_in_play = row4.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')

            elif move_s == 'D':
                if len(row3.area) > 0:
                    card_in_play = row3.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')

            elif move_s == 'E':
                if len(row2.area) > 0:
                    card_in_play = row2.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')

            elif move_s == 'F':
                if len(row1.area) > 0:
                    card_in_play = row1.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')

            elif move_s == 'G':
                if len(hearts.area) > 0:
                    card_in_play = hearts.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')
            
            elif move_s == 'H':
                if len(diamonds.area) > 0:
                    card_in_play = diamonds.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')
            
            elif move_s == 'I':
                if len(clubs.area) > 0:
                    card_in_play = clubs.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')
            
            elif move_s == 'J':
                if len(spades.area) > 0:
                    card_in_play = spades.area[0]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')

            elif move_s == 'K':
                if len(main_deck.deck) > 0:
                    card_in_play = main_deck.deck[current_card]
                else:
                    valid_input = False
                    print('\nInvalid move!\n')



            ##
            ## VALIDATION
            ##


            # Which card is the card_in_play going to be placed on?


            if valid_input: # Everything ok so far?
                
                if move_d == 'A':
                    try:
                        card_dest = row6.area[0]
                    except IndexError:
                        card_dest = '--'
                
                elif move_d == 'B':
                    try:
                        card_dest = row5.area[0]
                    except IndexError:
                        card_dest = '--'

                elif move_d == 'C':
                    try:
                        card_dest = row4.area[0]
                    except IndexError:
                        card_dest = '--'
    
                elif move_d == 'D':
                    try:
                        card_dest = row3.area[0]
                    except IndexError:
                        card_dest = '--'

                elif move_d == 'E':
                    try:
                        card_dest = row2.area[0]
                    except IndexError:
                        card_dest = '--'
    
                elif move_d == 'F':
                    try:
                        card_dest = row1.area[0]
                    except IndexError:
                        card_dest = '--'

                elif move_d == 'G':
                    try:
                        card_dest = hearts.area[0]
                    except IndexError:
                        card_dest = '-H'
                    
                elif move_d == 'H':
                    try:
                        card_dest = diamonds.area[0]
                    except IndexError:
                        card_dest = '-D'
    
                elif move_d == 'I':
                    try:
                        card_dest = clubs.area[0]
                    except IndexError:
                        card_dest = '-C'
                
                elif move_d == 'J':
                    try:
                        card_dest = spades.area[0]
                    except IndexError:
                        card_dest = '-S'


                # The rules for a valid destination depend on where the card_in_play is being moved to


                # These rules for for cards moved to and around the main playiing areas

                if move_d == 'A' or move_d == 'B' or move_d == 'C' or move_d == 'D' or move_d == 'E' or move_d == 'F':

                    # Make sure a red card is only placed onto a black card and vice versa

                    if (card_in_play[1] == 'H' or card_in_play[1] == 'D') and (card_dest[1] == 'H' or card_dest[1] == 'D'):
                        valid_input = False
                        print('\nInvalid move!\n')
                    elif (card_in_play[1] == 'S' or card_in_play[1] == 'C') and (card_dest[1] == 'S' or card_dest[1] == 'C'):
                        valid_input = False
                        print('\nInvalid move!\n')

                    else:
                        
                        if card_in_play[0] == 'A' and card_dest[0] == '2': 
                            valid_input is True
                        elif card_in_play[0] == '2' and card_dest[0] == '3':
                            valid_input is True
                        elif card_in_play[0] == '3' and card_dest[0] == '4':
                            valid_input is True
                        elif card_in_play[0] == '4' and card_dest[0] == '5':
                            valid_input is True
                        elif card_in_play[0] == '5' and card_dest[0] == '6':
                            valid_input is True
                        elif card_in_play[0] == '6' and card_dest[0] == '7':
                            valid_input is True
                        elif card_in_play[0] == '7' and card_dest[0] == '8':
                            valid_input is True
                        elif card_in_play[0] == '8' and card_dest[0] == '9':
                            valid_input is True
                        elif card_in_play[0] == '9' and card_dest[0] == 'T':
                            valid_input is True
                        elif card_in_play[0] == 'T' and card_dest[0] == 'J':
                            valid_input is True
                        elif card_in_play[0] == 'J' and card_dest[0] == 'Q':
                            valid_input is True
                        elif card_in_play[0] == 'Q' and card_dest[0] == 'K':
                            valid_input is True
                        elif card_in_play[0] == 'K' and card_dest[0] == '-': # The card_in_play must be a king if moved to an empty area
                            valid_input is True
                        else:
                            valid_input = False
                            print('\nInvalid move!\n')

                                   
                # These rules are for cards being placed with their suits

                
                if move_d == 'G' or move_d == 'H' or move_d == 'I' or move_d == 'J':
                    if card_in_play[1] == card_dest[1]:                     # Is this the correct suit?
                        
                        if card_in_play[0] == 'A' and card_dest[0] == '-':      # The card_in_play must be an ace if moved to an empty area
                            valid_input is True
                        elif card_in_play[0] == '2' and card_dest[0] == 'A':
                            valid_input is True
                        elif card_in_play[0] == '3' and card_dest[0] == '2':
                            valid_input is True
                        elif card_in_play[0] == '4' and card_dest[0] == '3':
                            valid_input is True
                        elif card_in_play[0] == '5' and card_dest[0] == '4':
                            valid_input is True
                        elif card_in_play[0] == '6' and card_dest[0] == '5':
                            valid_input is True
                        elif card_in_play[0] == '7' and card_dest[0] == '6':
                            valid_input is True
                        elif card_in_play[0] == '8' and card_dest[0] == '7':
                            valid_input is True
                        elif card_in_play[0] == '9' and card_dest[0] == '8':
                            valid_input is True
                        elif card_in_play[0] == 'T' and card_dest[0] == '9':
                            valid_input is True
                        elif card_in_play[0] == 'J' and card_dest[0] == 'T':
                            valid_input is True
                        elif card_in_play[0] == 'Q' and card_dest[0] == 'J':
                            valid_input is True
                        elif card_in_play[0] == 'K' and card_dest[0] == 'Q':
                            valid_input is True
                        else:
                            valid_input = False
                            print('\nInvalid move!\n')
                    else:
                        valid_input = False
                        print('\nInvalid move!\n')
                    
                if move_s != 'K' and move_d == 'K':
                    valid_input = False
                    print('\nInvalid move!\n')
                    

                ##
                ## Move from source
                ##

                # Cards are moved to position 0 to ensure they are always card on the top and visible


                if valid_input: # Everything ok so far? If it is a valid move then the card can be placed in the new location

                    if move_s == 'A':
                        row6.pick_up_card(card_in_play)

                    elif move_s == 'B':
                        row5.pick_up_card(card_in_play)
                        
                    elif move_s == 'C':
                        row4.pick_up_card(card_in_play)
                        
                    elif move_s == 'D':
                        row3.pick_up_card(card_in_play)
                        
                    elif move_s == 'E':
                        row2.pick_up_card(card_in_play)
                        
                    elif move_s == 'F':
                        row1.pick_up_card(card_in_play)
                        
                    elif move_s == 'G':
                        hearts.pick_up_card(card_in_play)
                        
                    elif move_s == 'H':
                        diamonds.pick_up_card(card_in_play)
                        
                    elif move_s == 'I':
                        clubs.pick_up_card(card_in_play)

                    elif move_s == 'J':
                        spades.pick_up_card(card_in_play)

                    elif move_s == 'K' and (move_d !='K' and move_d !=''):
                        main_deck.remove_card(card_in_play)
                        current_card -= 1


                ##
                ## Move to destination
                ##
    
                    if move_d == 'A':
                        row6.play_card(card_in_play,0)
    
                    elif move_d == 'B':
                        row5.play_card(card_in_play,0)
    
                    elif move_d == 'C':
                        row4.play_card(card_in_play,0)
        
                    elif move_d == 'D':
                        row3.play_card(card_in_play,0)
    
                    elif move_d == 'E':
                        row2.play_card(card_in_play,0)
            
                    elif move_d == 'F':
                        row1.play_card(card_in_play,0)
        
                    elif move_d == 'G':
                        hearts.play_card(card_in_play,0)
            
                    elif move_d == 'H':
                        diamonds.play_card(card_in_play,0)
        
                    elif move_d == 'I':
                        clubs.play_card(card_in_play,0)
                    
                    elif move_d == 'J':
                        spades.play_card(card_in_play,0)

                    ##
                    ## ADJUST DISPLAY
                    ##

                    if move_s == 'A' and row6_show > 0:
                        row6_show -= 1
                    if move_d == 'A':
                        row6_show += 1
        
                    if move_s == 'B' and row5_show > 0:
                        row5_show -= 1
                    if move_d == 'B':
                        row5_show += 1
                    
                    if move_s == 'C' and row4_show > 0:
                        row4_show -= 1
                    if move_d == 'C':
                        row4_show += 1
                    
                    if move_s == 'D' and row3_show > 0:
                        row3_show -= 1
                    if move_d == 'D':
                        row3_show += 1
                
                    if move_s == 'E' and row2_show > 0:
                        row2_show -= 1
                    if move_d == 'E':
                        row2_show += 1

                    if move_s == 'F' and row1_show > 0:
                        row1_show -= 1
                    if move_d == 'F':
                        row1_show += 1


                ##
                ## Have you won yet?
                ##


                if (len(hearts.area) > 0 and len(diamonds.area) > 0 and len(clubs.area) > 0 and len(spades.area) > 0):
                    if (hearts.area[0] == 'KH' and diamonds.area[0] == 'KD' and clubs.area[0] == 'KC' and spades.area[0] == 'KS'):

                        display_rows(row6.area,row5.area,row4.area,row3.area,row2.area,row1.area)
                        display_sorted_cards(hearts.area,diamonds.area,clubs.area,spades.area)
                        
                        print('\nCONGRATULATIONS!!! . . . You have won the game !!')

                        game_over = True


        ##
        ## Play again?
        ## 


    option = ''
    valid_input = False

    while not valid_input:
        option = input('\nDo you wish to play again? (Y/N) : ')
        if option == 'Y' or option == 'y' or option == 'YES' or option == 'yes':
            option = 'y'
            valid_input = True
            quit_prog = False
            
            # Return all the cards to the deck n preparation for the next game
            
            row6.return_all(main_deck)
            row5.return_all(main_deck)
            row4.return_all(main_deck)
            row3.return_all(main_deck)
            row2.return_all(main_deck)
            row1.return_all(main_deck)
            hearts.return_all(main_deck)
            spades.return_all(main_deck)
            clubs.return_all(main_deck)
            diamonds.return_all(main_deck)
            
        elif option == 'N' or option == 'n' or option == 'NO' or option == 'no':
            option = 'n'
            valid_input = True
            quit_prog = True
            
        else:
            print('You must reply Y - YES or N - NO!')
