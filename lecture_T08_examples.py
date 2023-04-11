
#*************Example 1**************
#A for loop to display all number from 0 to 15
for i in range(0,16):
    print(i)
    
#*************Example 2**************
# We can also use for loops to print the characters of a string variable
# Declare the variable for the iterable_object
alphabet = "abcdefghiklmnopqrstuvwxyz"

for each_letter in alphabet:
    # the temporary variable "each_letter" updates for every iteration (repetition)
    print(each_letter)  


#*************Example 3*************
#A for loop to display all even numbers from 2 to 20
for i in range(2,21,2):  
    print(i)

#************Example 4****************
# A for loop to display display numbers from 0 to 20 in reverse
for i in range(20,-1,-1):  
    print(i)

#************Example 5*****************
# A program to display the 9 times table
for i in range(10):
    # A variable to store the product of the index_variable and 9
    multiply_by_9 = i * 9
    
    print (f"{i} * 9 = {multiply_by_9}")

     


