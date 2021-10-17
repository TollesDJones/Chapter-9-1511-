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

class Senior(Person):
    """This class creates a joseph object """ # Method description
    def __init__(self,fname, lname, age, employed: bool = False, wage="$0"):
        super().__init__(fname, lname)
        self.age = age
        self.employed = employed
        self.wage = wage

    def displayStatus(self):
        print("Here are my stats: ",
        self.age,"Age",
        self.wage, "Wage",
        self.employed, "Employed")

    def hobbies(self):
        print("Play CS:GO")

    def job(self):
        print("Make Money by working at Cold Stone", )


class Junior(Senior):
    """This class creates a 'Nick' object """
    def __init__(self, fname: str, lname: str, age: str, employed: bool, wage="$0", allowance="$0"):
        Person.__init__(self, fname, lname)
        Senior.__init__(self, age, employed, wage)
        self.allowance = allowance

    def hobbies(self):
        print("Play Rust")

    def job(self):
        print("I'm not working, I get an allowance of ", self.allowance)

    def chores(self):
        print("I did the dishes")
        choresComplete = True
        return choresComplete


def playGame(someObject):
    someObject.play()

# main

# Create an instance of a Senior Object
person0= Senior("Donte", "Jones", "18", True, "$6.25")
person0.displayStatus()
person0.printname()

person2= Junior("Tony", "Stark", 38, True, "$1B")
person2.displayStatus()

#person3 = Junior(employed=False, name="Nick", age="17")
# person2.displayStatus()
# person3.displayStatus()


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