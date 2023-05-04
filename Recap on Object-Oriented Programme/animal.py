class Animal:
    animal_type = "animal"

    def display_type(self):
        print("This is an animal.")


class Mammal(Animal):

    def __init__(self):
        self.animal_type = "Mammal"
    
    def display_type(self):
        print(f"This is a {self.animal_type}.")

    def make_sound(self):
        print(f"{self.animal_type} has made a sound")


class Fish(Animal):

    def __init__(self):
        self.animal_type = "Fish"

    def display_type(self):
        print(f"This is a {self.animal_type}.")

    def blow_bubbles(self):
        print("OOOooo  OOOooo  OOOooo")


my_animal = Fish()

my_animal.display_type()