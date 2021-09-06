# Michael Gennery
# Pack of Cards
# August 2021

import random

"""

These classes and functions facilitate the use of a deck of cards for creating card games.

A 52 deck of cards is created with a table with 2 character string variables using the following legend: -

    Cards

        A - Ace
        2 - Two
        3 - Three
        4 - Four
        5 - Five
        6 - Six
        7 - Seven
        8 - Eight
        9 - Nine
        T - Ten
        J - Jack
        Q - Queen
        K - King

    Suits

        H - Hearts
        D - Diamonds
        S - Spades
        C - Clubs

    e.g. 'AS' - Ace of Spades, 'KC' - King of Clubs, '3D' - Three of Diamonds, 'TH' - Ten of Hearts

Functions are also included for creating decks, shuffling decks, picking cards, playing cards and dealing hands

"""

def card_to_text(input_card):

    card_dict = {
        'A' : 'Ace',
        '2' : 'Two',
        '3' : 'Three',
        '4' : 'Four',
        '5' : 'Five',
        '6' : 'Six',
        '7' : 'Seven',
        '8' : 'Eight',
        '9' : 'Nine',
        'T' : 'Ten',
        'J' : 'Jack',
        'Q' : 'Queen',
        'K' : 'King'
        }

    card_suit = {
        'H' : 'Hearts',
        'D' : 'Diamonds',
        'S' : 'Spades',
        'C' : 'Clubs'
        }

    invalid_card = False
        
    if len(input_card) == 2: # Check length of card code
            
        if input_card[0] in card_dict: # Check card is valid
                
            output_card_code = input_card[0]                
            output_card = card_dict[output_card_code]
                
            if input_card[1] in card_suit: # Check suit is valid
                        
                    output_suit_code = input_card[1]                
                    output_suit = card_suit[output_suit_code]
                        
            else:
                invalid_card = True
        else:
            invalid_card = True
    else:
        invalid_card = True

    if invalid_card:
        return('Invalid Card')
    else:
        output_card_text = '{} of {}'.format(output_card,output_suit) 
        return(output_card_text) # Return card text if code valid


##


class area():

    # The area object is a shared place for players to put played cards
    # The face card is area[0]
    
    def __init__(self):
        self.area = []
        game_name = '' # The name of the game e.g. Poker, Blackjack, Rummey etc.

    def play_card(self, input_card, position):
        self.area.insert(position,input_card)       # Add card to the area in the correct position
        self.update_area(self.area)                 # Update the area

    def pick_up_card(self, input_card): # Pick up card from area
        self.area.remove(input_card)
        self.update_area(self.area)                         # Update the area

    def return_to_deck(self, input_card, input_deck):       # Return cards to deck
        self.area.remove(input_card)                        # Remove Card from area
        input_deck.replace_card(input_card)                 # Place it back into the deck
        self.update_area(self.area)                         # Update the area

    def return_all(self, input_deck):
        while len(self.area) > 0:
            self.return_to_deck(self.area[0], input_deck)     # Place next card back into the deck
        self.update_area(self.area)                         # Update the area
        
    def update_area(self, input_area):  # Update the area when cards are played or removed
        self.area = input_area


##


class deck(area):

    def __init__(self):
        self.deck = ['AH','2H','3H','4H','5H','6H','7H','8H','9H','TH','JH','QH','KH',
                     'AD','2D','3D','4D','5D','6D','7D','8D','9D','TD','JD','QD','KD',
                     'AS','2S','3S','4S','5S','6S','7S','8S','9S','TS','JS','QS','KS',
                     'AC','2C','3C','4C','5C','6C','7C','8C','9C','TC','JC','QC','KC']
        
    def remove_card(self, card):
        self.deck.remove(card) # Remove card from deck
        self.update_deck(self.deck)
        
    def replace_card(self, card):
        self.deck.append(card) # Replace card in deck
        self.update_deck(self.deck)

    def shuffle(self): # Shuffle cards in the deck
        output_deck = []
        while len(output_deck) < 52:
            output_card = random.choice(self.deck)      # Select a card from random
            output_deck.append(output_card)             # Place it into a new deck
            self.remove_card(output_card)               # Remove from the original deck
        self.deck = output_deck                         # Update the original deck with the new, shuffled deck
        self.update_deck(self.deck)

    def play_card(self, input_deck, input_area, num_of_cards): # Play cards from the deck
        for card in range(0,num_of_cards):
            output_card = input_deck.deck[0]
            input_deck.remove_card(output_card)                          # Remove Card from deck
            input_area.play_card(output_card,0)                          # Place it into the area
        self.update_deck(self.deck)

    def update_deck(self, input_deck): # Update deck when shuffled or each card is added or replaced
        self.deck = input_deck


##

        
class hand(deck):

    def __init__(self):
        self.hand = []
        player_name = '' # The name of the player

    def deal(self, input_deck, num_of_cards):
        for card in range(0,num_of_cards):
            output_card = input_deck.deck[0]    # Take the next card from the top of the deck
            self.hand.append(output_card)       # Add it to the hand
            input_deck.remove_card(output_card) # Remove from the deck
        self.update_hand(self.hand)

    def pick_up_card(self, input_area, input_card): # Pick up a card from an area
        input_area.pick_up_card(input_card)         # Remove card from area
        self.hand.append(input_card)            # Add it to the hand
        self.update_hand(self.hand)             # Update the hand

    def return_to_deck(self, input_card, input_deck):
        self.hand.remove(input_card)            # Remove Card from hand
        input_deck.replace_card(input_card)     # Place it back into the deck
        self.update_hand(self.hand)             # Update the hand

    def return_all(self, input_deck):
        while len(self.hand) > 0:
            self.return_to_deck(self.hand[0], input_deck)   # Place next card back into the deck
        self.update_hand(self.hand)                         # Update the hand
        
    def play_card(self, input_card, output_area):
        self.hand.remove(input_card)              # Remove Card from hand
        output_area.play_card(input_card,0)       # Play the card into the area
        self.update_hand(self.hand)               # Update the hand
        
    def update_hand(self, input_hand): # Update hand when cards are dealt or replaced
        self.hand = input_hand


