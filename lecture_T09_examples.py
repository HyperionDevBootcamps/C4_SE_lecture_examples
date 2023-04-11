#************* Example 1******************
#Exception handling for ValueErrors
while True:
    try:
        num = int(input("Please enter a number: "))
        break 

    except Exception:
        print("Oops! That was not a valid number. Try again")

if (num == 0):
    print("You've entered zero")
elif (num > 5):
    print("Your number is greater than 5")
elif (num < 5 ):
    print("Your number is smaller than 5")
else:
    print("Your number is 5")

#************Example 2*************
# Open a file and handle exception for file not found
file = None
try:
    file = open('days.txt', 'r')
    # Read over all lines in the text file
    read_lines = file.readlines()

    # Display content in text file
    print(read_lines)

    # Always close your file 
    file.close() 

except FileNotFoundError as error:
    print("The file that you are trying to open does not exist")
    print(error)

finally:
    if file is not None:
        file.close()

#*************Example 3**************
# Exception handling for invalid user entry
while True:
    try:
        user_input = int(input("Please enter a number: "))
        break 

    except ValueError:
        print("Oops! That was not a valid number. Try again")

# Create and write to a text file
with open("open_file.txt",'w') as file: 

    file.write(str(user_input))

#**********Example 4*************
# Write content to a text file using Python
user_input = input("Please enter your birth month: ")

# Create the file called "months" and write to it
with open("months.txt",'w') as file: 
    file.write("January \n")
    file.write("February \n")
    file.write("March \n")
    file.write("April \n")
    file.write("May \n")
    file.write("June \n")

    file.write(user_input)