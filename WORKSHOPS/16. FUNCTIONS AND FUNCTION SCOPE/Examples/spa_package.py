# Create a program to determine the total cost of customized spa package.

# Clients can customize their spa package by choosing a treatment, a meal and a beverage.
# Create 3 dictionaries, one for each type of option:

# Treatment dictionary
treatment_dict = {1:"Full body massage", 2: "Facial", 3: "Manicure"}
# Meal dictionary
meal_dict = {1: "Pasta", 2: "Pizza"}
# Beverage dictionary
beverage_dict = {1: "Coffee", 2: "Tea"}

# Create a function to determine and return the price of the treatment chosen by a client
def treatment(user_treatment) -> int:
    if user_treatment == 1:
        return 30
    elif user_treatment == 2:
        return 20
    elif user_treatment == 3:
        return 10
    else:
        print("Invalid option. Please selection option 1,2 or 3")


# Create a function to determine and return the price of the meal chosen by a client
def meal(user_meal) -> int:
    if user_meal == 1:
        return 15
    elif user_meal == 2:
        return 12
    else:
        print("Invalid option. Please selection option 1 or 2")


# Create a function to determine and return the price of the beverage chosen by a client
def beverage(user_beverage) -> int: # option 1: coffee, option 2: tea
    if user_beverage == 1:
        return 5 #$
    elif user_beverage == 2:
        return 3 #$
    else:
        print("Invalid option. Please selection option 1 or 2")

# Create a function to calculate the total cost of the spa package
def spa_package(treatment, meal, beverage) -> int:
    total = treatment(user_treatment) + meal(user_meal) + beverage(user_beverage)
    return total


# Create a function to display the options selected by a client and the total cost
def display(user_treatment, user_meal, user_beverage, spa_package) :
    print(f'''Your spa package include:
     Treatment: {treatment_dict[user_treatment]}
     Meal:{meal_dict[user_meal]}
     Beverage: {beverage_dict[user_beverage]}
     Total cost: $ {spa_package(treatment, meal, beverage)}''')


# Create variables to store user options
# For the type of treatment
while True:
    try:
        user_treatment = int(input('''Please select a treatment option: 
        1. Full body massage \n
        2. Facial \n
        3. Manicure \n'''))
        if user_treatment in range(1,4):
            break
        else:
            print("Invalid selection. Please select 1, 2 or 3")
    except ValueError:
        print("Invalid selection. Please try again")

# For the type of meal
user_meal = int(input('''Please select a meal option: 
1. Pasta \n
2. Pizza \n
'''))

# For the type of beverage
user_beverage = int(input('''Please select a beverage option:\n
1. Coffee 
2. Tea'''))

# Call the display function to print a summary of the customized spa package
display(user_treatment, user_meal, user_beverage, spa_package)
