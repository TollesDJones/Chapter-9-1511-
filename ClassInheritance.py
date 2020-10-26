#
#Demonstrate Class Inheritance
#Parameters, Arguments, Overloading, Polymorphism
#
#
class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Joseph:
    """This class creates a joseph object """ # Method description
    def __init__(self, age, name, employed: bool = False, wage="$0"):
        self.age = age
        self.employed = employed
        self.wage = wage
        self.name = name


    def display(self):
        print("This is from Class Joseph",
        self.age,
        self.wage,
        self.employed,
        self.name)

    def play(self):
        print("Play CS")

    def job(self):
        print("Make Money at my job", )


class Nick(Joseph):
    """This class creates a 'Nick' object """
    def __init__(self, age, employed, wage, name, allowance="$0"):
        super().__init__(age, employed, name, wage="0")
        self.allowance = allowance

    def display(self): # 'age' is a parameter of the display method
        print("This is from Class Nick", self.age)

    def play(self):
        print("Play Rust")

    def job(self):
        print("I'm not working, I get an allowance of ", self.allowance)


def playGame(someObject):
    someObject.play()

# main

donte = Person("Donte", "Jones")
donte.printname()

person2 = Joseph(age=18, name="Joseph", wage="$13", employed=True)
person3 = Nick(wage="13", employed=False, name="Nick", age="17")
person2.display()
person3.display()


#joseph1 = Joseph("18", True, "$13", "Joseph")  # Instantiates a Joseph Object Named 'joseph1'
#nick1 = Nick()      # Instantiates a Nick Object Named 'nick1'
#nick2 = Nick()      # Instantiates a second Nick Object Named 'nick2' with default parameters

#joseph1.display() # The string " 16" is an argument setting the 'age' parameter
                         # We pass this argument because the .display() method
                         # we defined in the Class has a parameter

#nick1.display()
#nick1.job()


#joseph1.job() # Be sure Joseph is passed as a class argument before using
#             # Demonstrates the 'nick' object inheriting a method
#             # from the Joseph class through
#
#
#
#
#playGame(nick1) # Demonstrates 'Polymorphism'
                     # The 'playGame' method takes any object passed
                     # as an argument and calls it's  .play()