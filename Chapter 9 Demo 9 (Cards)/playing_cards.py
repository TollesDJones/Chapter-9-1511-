# Playing Cards (2) D1
# Demonstrates combining objects & object communication
# A 'hand' object that contains 'card' objects

class Card:
    """ A playing card. """
    RANKS = ["A", "2", "3", "4", "5", "6", "7",
             "8", "9", "10", "J", "Q", "K"]
    SUITS = ["c", "d", "h", "s"]
    
    def __init__(self, rank, suit):
        self.rank = rank 
        self.suit = suit

    def __str__(self):
        rep = self.rank + self.suit
        return rep


class Hand:
    """ A hand of playing cards. """
    def __init__(self):
        self.cards = [] # initialize an empty list

    def __str__(self): # return value all cards in the hand (string)
        if self.cards:
           rep = ""
           for card in self.cards:
               rep += str(card) + "  "
        else:
            rep = "<empty>"
        return rep

    def clear(self): # remove all cards from hand
        self.cards = []

    def add(self, card): # add a card to the hand
        self.cards.append(card)

    def give(self, card, other_hand): # remove a specific card from this hand, place
        self.cards.remove(card)       # and place the card in another hand
        other_hand.add(card)


# main
card1 = Card(rank = "A", suit = "c")
print("Printing a Card object:")
print(card1)

card2 = Card(rank = "2", suit = "c")
card3 = Card(rank = "3", suit = "c")
card4 = Card(rank = "4", suit = "c")
card5 = Card(rank = "5", suit = "c")
print("\nPrinting the rest of the objects individually:")
print(card2)
print(card3)
print(card4)
print(card5)

my_hand = Hand()
print("\nPrinting my hand before I add any cards:")
print(my_hand)

my_hand.add(card1)
my_hand.add(card2)
my_hand.add(card3)
my_hand.add(card4)
my_hand.add(card5)
print("\nPrinting my hand after adding 5 cards:")
print(my_hand)

your_hand = Hand()
my_hand.give(card1, your_hand)
my_hand.give(card2, your_hand)
print("\nGave the first two cards from my hand to your hand.")
print("Your hand:")
print(your_hand)
print("My hand:")
print(my_hand)

my_hand.clear()
print("\nMy hand after clearing it:")
print(my_hand)



