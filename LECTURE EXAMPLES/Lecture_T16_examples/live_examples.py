print("Example 1: Print the 5 times table")
# Display the 5 times table
print("1 x 5 = 5")
print("2 x 5 = 10")
print("3 x 5 = 15")
print("4 x 5 = 20")
print("5 x 5 = 25")
print("6 x 5 = 30")
print("7 x 5 = 35")
print("8 x 5 = 40")
print("9 x 5 = 45")
print("10 x 5 = 50")

# How could we use a function to simplify this code?
print("Example 2: Print the 5 times table using a function")
def times_table():
    print("1 x 5 = 5")
    print("2 x 5 = 10")
    print("3 x 5 = 15")
    print("4 x 5 = 20")
    print("5 x 5 = 25")
    print("6 x 5 = 30")
    print("7 x 5 = 35")
    print("8 x 5 = 40")
    print("9 x 5 = 45")
    print("10 x 5 = 50")

times_table()

# Defining a method containing all the print statement
# is one way of simplifying the code to display the 5 times table

# But, we can actually define a function to determine the product
# of a number and 5:
print("Example 3: Using a function and a for loop")
def multiple(x, num1=5):
    answer = x * num1
    return answer
# Then, use a for loop to display the 5 times table
for i in range(1,11):
    # Call the multiple function and save it in a variable
    value = multiple(i)
    print(f"{i} x 5 = {value}")

# Or, even beter - we could include the for loop in the function

print("Example 4: Using a for loop inside a function")
# Define a function with its parameter set to a default value (num=5)
# This will allow you to change the value if you want to display the times
# table of another value eg. the 9 times table
def mult_tables(num=5):
    for i in range(1,11):
        multiple = i * num
        print(f"{i} * {num} = {multiple}")

# Call the mult_tables function 
mult_tables(5)

# Check out some other solutions proposed by students during the lecture!

## Student suggestion 1:
# def times_table(multiplier):
#     for i in range(1,11):
#         result = (i)*multiplier
#         print (str(i)+" x " + str(multiplier)+" = "+ str(result))

# times_table(5)

# #Student suggestion 2:
# def times_table(x):
#     while x<=10:
#         sum = x*5
#         print(f"{x} x 5 = {sum}")
#         x = x+1
# times_table(1)






