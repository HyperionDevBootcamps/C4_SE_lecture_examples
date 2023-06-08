class Animal:
    animal_type = "animal"

    def display_type(self):
        print("This is an animal.")

    def make_sound(self):
        print(f"{self.animal_type} has made a sound")

    def blow_bubbles(self):
        print("OOOooo  OOOooo  OOOooo")


class Mammal(Animal):

    def __init__(self):
        self.animal_type = "Mammal"
    
    def display_type(self):
        print(f"This is a {self.animal_type}.")

    def make_sound(self):
        print(f"{self.animal_type} has made a sound")

    def blow_bubbles(self):
        pass


class Fish(Animal):

    def __init__(self):
        self.animal_type = "Fish"

    def display_type(self):
        print(f"This is a {self.animal_type}.")

    def blow_bubbles(self):
        print("OOOooo  OOOooo  OOOooo")

    def make_sound(self):
        pass
