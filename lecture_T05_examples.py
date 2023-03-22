#************* Example 1******************
num = int(input("Please enter a number: "))

if (num == 0):
    print("You've entered zero")
elif (num > 5):
    print("Your number is greater than 5")
elif (num < 5 ):
    print("Your number is smaller than 5")
else:
    print("Your number is 5")

#*************Example 2*********************
# Request user to enter two integers 
num1 = int(input("Please enter an integer: "))
num2 = int(input("Please enter another integer: "))

# An if-elif-else statement to determine the relationship between two integers
if (num1 == num2):
    print("You have entered exactly the same integers")
elif (num1 > num2):
    print(f"{num1} is greater than {num2}")
else:
    print(f"{num1} is smaller than {num2}")

# #*************Example 3********************
# A program to validate a user's eligiblity to vote 
# depending on their nationality and age  

nationality = input("Please enter your nationality:")

if nationality == "South Africa" or "south africa"or "RSA" or "SA":
    year_born = int(input("Please enter the year you were born: "))
    
    # A variable to calculate the age of the user
    age = 2023 - year_born

    if age >= 18:
        print("You are eligible to vote")
    else:
        print("Sorry, you are too young to vote")

else:
    print("Sorry, you are not eligible to vote")

#***************Example 4********************

# Request user to enter their grade
grade = int(input("Please enter your grade: "))

# An if-else nested loop to determine the outcome of the grade 
if grade >= 50:
    
    if grade >= 80:
        print("Congratulations! You passed with a distinction!")
    else:
        print("Well done! You passed the test.")

else:
    print("Sorry, you failed the test. Keep on trying")

#***************Example 5********************
# Application of Boolean variables 
# Declare boolean variable and set default value to false
is_raining = True 

# If-else statement to determine whether to bring umbrella or not 
if is_raining == True:
    print("Bring your umbrella")
else:
    print("Leave your umbrella at home")