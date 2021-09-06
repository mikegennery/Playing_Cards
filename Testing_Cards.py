# Michael Gennery
# Pack of Cards - Testing Cards
# August 2020

from Playing_Cards import *

## Testing area

my_area = area() # Create a new area
my_area.game_name = 'Testing Cards'

my_deck = deck() # Create a deck

my_hand = hand() # Create a hand
my_hand.player_name = 'Michael Gennery'

print(my_area.game_name,' by ',my_hand.player_name)

print('\nBEFORE SHUFFLE:')

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

# Shuffle Cards

my_deck.shuffle()

print('\nAFTER SHUFFLE: ')

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Deal 6 Cards
print('\nDeal 6 Cards:')

my_hand.deal(my_deck,6)

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Return two cards to the deck

card1 = my_hand.hand[0]
card2 = my_hand.hand[1]

print('\nRETURN: ',card_to_text(card1))
print('RETURN: ',card_to_text(card2))

my_hand.return_to_deck(card1,my_deck)
my_hand.return_to_deck(card2,my_deck)

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# play 3 cards

card3 = my_hand.hand[0]
card4 = my_hand.hand[1]

print('\nPLAY: ',card_to_text(card3))
print('PLAY: ',card_to_text(card4))

my_hand.play_card(card3,my_area) # Play the 2 cards
my_hand.play_card(card4,my_area)

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Return all cards to deck

print('\nRETURN: ',card_to_text(my_hand.hand[0]))
print('RETURN: ',card_to_text(my_hand.hand[1]))
print('RETURN: ',card_to_text(card3))
print('RETURN: ',card_to_text(card4))

my_hand.return_to_deck(my_hand.hand[0],my_deck)
my_hand.return_to_deck(my_hand.hand[0],my_deck)
my_area.return_to_deck(card3,my_deck)
my_area.return_to_deck(card4,my_deck)


print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Deal 4 Cards

my_hand.deal(my_deck,4)
print('\nDeal 4 Cards\n')

print('\nAFTER DEAL:')

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Play 8 cards from deck
print('\nPlay 8 cards from deck\n')

my_deck.play_card(my_deck, my_area, 8)

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Pick up three cards
print('\nPick up three cards\n')

my_hand.pick_up_card(my_area, my_area.area[0])
my_hand.pick_up_card(my_area, my_area.area[0])
my_hand.pick_up_card(my_area, my_area.area[0])

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Return everything
print('\nReturn everything\n')

my_area.return_all(my_deck)
my_hand.return_all(my_deck)

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))

pause = input('\nPRESS ENTER TO CONTINUE\n')

# Shuffle Cards

my_deck.shuffle()

print('\nAFTER SHUFFLE: ')

print('\nAREA: ',my_area.area)
print('HAND: ',my_hand.hand)
print('DECK: ',my_deck.deck) # Print full deck
print('CARDS: ',len(my_deck.deck))


