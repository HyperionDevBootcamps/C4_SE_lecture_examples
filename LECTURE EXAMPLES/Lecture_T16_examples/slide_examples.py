#*************Abstraction***************
# # Abstraction is used to hide background details or 
# # any unnecessary implementation about the data 
# # so that users only see the required information
# def makeCupOfTea():
#     print("Boil water")
#     print("Add tea bag")
#     print("Add sugar")
#     print("Add milk")
#     print("Stir")

# makeCupOfTea()

#************** Calling functions**********
# def my_function1(input1):
#     return input1 
# def my_function2(input2,input1):
#     return input1 + input2
# def my_function3(input1, keyword_arg = 2):
#     return input1 + keyword_arg

# a = my_function1(1)
# b = my_function2(1,2)
# c = my_function3(1) 

# print(a)
# print(b)
# print(c)

#*************Built-in functions************
# print(len([1,2,4]))
# print("Hello World")
# num = input("Enter number: ")
# int("5")

#************Import modules*************
# my_num = 10.23578
# import math
# my_result = math.floor(my_num)
# print(my_result)

# from math import floor
# my_result = floor(my_num)
# print(my_result)

#************** Default values***********
# def multiply(num1,num2 = 5):
#     sum = num1 * num2
#     return sum

# answer1 = multiply(10) 
# answer2 = multiply(10,num2 = 6)

# print(answer1)  #prints 50
# print(answer2)  #prints 60

#*****************scope*********************
## Variable declared inside a function are not
## accessible outside the function

# def multiply(x,y):
#     product = x * y 
#     return product

# answer1 = multiply(2,3)

# print(f"{x} times {y} is {answer1}")

#************General Syntax of functions**********
# def my_function(parameter1, parameter2):
#     #statement
#     local_variable = parameter1 * parameter2
#     #expression
#     return local_variable

# # Calling functions
# # Declare a variable to store the return value
# answer = my_function(1, 9)

# # Print the output of the function for the 'answer' instance
# print(answer)
      
