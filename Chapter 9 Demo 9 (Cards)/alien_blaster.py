# Alien Blaster (1) D1
# Demonstrates object interaction


""" Objects send messages to each other through methods. """
class Player:
    """ A player in a shooter game. """
    def blast(self, enemy):
        print("The player blasts an enemy.\n")
        # The enemy variable refers to an object of type Alien
        enemy.die()

class Alien:
    """ An alien in a shooter game. """
    def die(self):
        print("The alien gasps and says, 'Oh, this is it.  This is the big one. \n" \
              "Yes, it's getting dark now.  Tell my 1.6 million larvae that I loved them... \n" \
              "Good-bye, cruel universe.'")

# main
print("\t\tDeath of an Alien\n")

# Creates a Player Object
hero = Player()

# Creates an Alien Object
invader = Alien()

# Hero object uses a Player class method to call an Alien object's 'Die' method
hero.blast(invader)


