#**************Example 1**************
print("Example 1:")
# A function to calculate a times table
# Request user to specify the times table they want to display
num = int(input("Which times table would you like to display? :"))

# A function to calculate the product of two numbers
def times_table(x,y = num):
   total = x * y 
   return total

# A for loop to display the ?(num) times table
for i in range(1,11):
    result = times_table(i)
    print(f"{i} x {num} = {result}")

#****************Example 2**************
print("Example 2:")
# User input in a function
def greet():
    title = input("Enter your title:")
    user_name = input("Enter your name: ")
    user_surname = input("Enter your surname: ")
    print(f"Good day, {title} {user_name[0]} {user_surname}")

# Call the function
greet()