# Create a parent class called person
class Person:
    height = 170
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

# Create a child class called Father
class Father(Person):
    def __init__(self, name, surname = "Reeds"):
        super().__init__(name, surname)
        self.height = super().height - 10  # 170 - 10 = 160
    
    # Create a method to compare the height 
    # of the father and the son
    def __eq__(self, other):
        if self.height == other.height:
            return True
        else: 
            return False

# Create a child class of Father called Son
class Son(Father):

    def __init__(self, name):
        super().__init__(name)
        self.height = super().height + 10

    # Create a method to change the height of the son
    def set_height(self, new_height):
        self.height = new_height

# Create another child class of Father called daughter
class Daughter(Father):
    def __init__(self,name):
        super().__init__(name)

    # Create methods to change the surname of the daughter 
    def change_surname(self, new_surname):
        self.surname = new_surname


# Create the main method
def main():
    person1 = Person("Ben", "Speer")
    father1 = Father("Jimmy", "Reeds")
    son1 = Son("Marc")
    daughter1 = Daughter("Clare")

    # print("Person1 has length: ", person1.height)
    # print("Father1 has length: ", father1.height)
    # print("Son1 has length: ", son1.height)

    # print("The surname of Father1 is: ", father1.surname)
    # print("The surname of Son1 is: ", son1.surname)

    # print("Their height are the same: ", father1.__eq__(son1))

    #son1.height = father1.height
    # son1.set_height(father1.height)

    # print("Their height are the same: ", father1.__eq__(son1))

    print("The daughter's name is", daughter1.name)
    print("The daughter's surname is", daughter1.surname)

    daughter1.change_surname("Clarke")
    print("The daughter's new surname is ", daughter1.surname)

main()