import random

"""Creates a 52 card deck, returns a list of strings"""
def create_deck():
    deck = []
    for l in range(4):
        for j in range(1, 14):
            if j == 1:
                deck.append("Ace")
            elif j < 11:
                deck.append(str(j))
            elif j == 11:
                deck.append("Jack")
            elif j == 12:
                deck.append("Queen")
            elif j == 13:
                deck.append("King")
    return deck
    
"""Input a deck of cards, output is a shuffled deck"""

def shuffle(deck):
    new_deck = []
    for i in range(51):
        num = 51 - i
        card = random.randint(0, num)
        new_deck.append(deck[card])
        deck.pop(card)
    return(new_deck)
    
def round(deck_1, money):
    player_cards = deck_1[0]
    

deck_1 = create_deck()
money = 1000
