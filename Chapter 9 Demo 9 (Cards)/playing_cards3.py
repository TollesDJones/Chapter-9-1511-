# Playing Cards 3.0 (4) D2
# Demonstrates inheritance - overriding methods - Polymorphism

"""
Overriding - Allows you to redefine how inherited methods work
we can create a new method to change the functionality or
we can incorporate the the existing functionality

Polymorphism - The word polymorphism means having many forms.
In programming, polymorphism means the same function name
(but different signatures) being used for different types.
the __str__ methods below are an example of this.

"""

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


class Unprintable_Card(Card):
    """ A Card that won't reveal its rank or suit when printed.
    it 'extends' the Card class by inheriting all the methods of 'Card'
    it overrides the base class's string method """
    def __str__(self):
        return "<unprintable>"


class Positionable_Card(Card):
    """ A Card that can be face up or face down.
     this class also extends the card class and
     overrides both the init and string methods """

    def __init__(self, rank, suit, face_up=True):
        """ New init method incorporates the the old one
        by calling the the use of the 'Super()' method """
        super().__init__(rank, suit) # indicates a call to the base class' init method
        self.is_face_up = face_up    # to provide the rank/ suit, while adding the new 'face_up' attribute

    def __str__(self):
        if self.is_face_up:
            rep = super().__str__() # incorporates base class string method
        else:
            rep = "XX" # extends base class functionality
        return rep

    def flip(self): # new ability for positionable cards
        self.is_face_up = not self.is_face_up # Not used to reverse the current value of attribute


#main
# Creates 3 card objects, one of each class type
card1 = Card("A", "c")
card2 = Unprintable_Card("A", "d")
card3 = Positionable_Card("A", "h")

print("Printing a Card object:")
print(card1)

print("\nPrinting an Unprintable_Card object:")
print(card2)

print("\nPrinting a Positionable_Card object:")
print(card3)
print("Flipping the Positionable_Card object.")
card3.flip()
print("Printing the Positionable_Card object:")
print(card3)
print("Flipping the Positionable_Card object back.")
card3.flip()
print("Printing the Positionable_Card object:")
print(card3)


