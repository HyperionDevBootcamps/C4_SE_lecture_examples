#*****************SPA MENU*********************
# This program will allow users to 
#   1. View available spa packages 
#       a. Select one of the spa packages to view the treatments included in the package
#   2. Show the packages they've viewed
#   3. Quit the program

# We will build the program from scratch :)
# First -  create a class for the spa packages
# Second - create functions to hide the complexities (abstraction)
# Third - build the functionality of the rest of program


# Create a class called packages
class Package():
    # class variables
    selected = False
    def __init__(self, type, treatments, meal, beverage, price):
        # instance variables
        self.type = type
        self.treatments = treatments
        self.meal = meal
        self.beverage = beverage
        self.price = price

    # class method
    def viewed(self):
        self.selected = True

#package1 = Package(["Full body massage","Facial"],"Pizza","Coffee")

# create an empty list (package objects to be added)
inventory = [] 
# create a function to initialise package objects and add them to the inventory list
def create_inventory(type,treatments, meal, beverage, price):
    # initialise a package object
    package = Package(type,treatments, meal, beverage, price)
    # add object to inventory list
    inventory.append(package)

#create_inventory("Half day",["Full body massage","Facial"],"Pizza","Coffee", 50)

# Create a function to display the type of packages and their prices
def package_options(inventory):
    # iterate over inventory and display the package type and price in an ordered list
    for num, item in enumerate(inventory, start = 1):
        print(num, item.type,"@ $", item.price)
        
#inventory = [package<object>___67375734, package<object>___76327658] 
# Create a function to display the treatments included in a selected package
def show_treatments(package_no):
    # iterate over treatments list and display items
    for treatment in inventory[package_no].treatments:
        print(treatment, end=";")

    # call the 'viewed' method to change the value of selected to True
    inventory[package_no].viewed()


def main():
    # Call the create_inventory function to add packages to the inventory list
    create_inventory("Half day", ["Full body massage", "facial", "manicure"], "Pasta", "Coffee", 50)
    create_inventory("Full day", ["Full body massage", "facial", "manicure", "pedicure", "back scrub"], "Pasta", "Coffee", 80)
    
   

    # A while loop to keep prompting the user to select an option until they choose to end the program
    while True:
        # create a variable to store the option selected by the user
        user_option = int(input('''Please select an option from the menu:
        1. View all available packages
        2. Show your viewed package(s)
        3. Exit\n'''))

       

        # if statement to determine output based on option selected by user
        if user_option == 1:
            # Display package options
            # Call the package_options functions
            package_options(inventory)
            print()
            # Prompt user to select a package number to view the treatments included
            package_no = int(input("Select an option to view the treatments: \n"))
            # Call the show_treatments function
            show_treatments(package_no - 1)  
            print() 

        elif user_option == 2:
            # Only display packages that have been viewed
            for package in inventory:
                if package.selected == True:
                    print(f" You have viewed the {package.type} spa package")
           
                  
        elif user_option == 3:
            print("Goodbye")
            exit()
        
        else:
            print("Please make a valid selection.")
  
main()
