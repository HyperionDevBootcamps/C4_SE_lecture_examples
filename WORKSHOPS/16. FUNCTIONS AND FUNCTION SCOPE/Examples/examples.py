# -------------------- Example 1 -----------------------

# Define a function to open a file, read its contents and display it.

# def read_file(file_name) :
#     # add file extension
#     file = file_name + ".txt"
#     # open file
#     with open(file, 'r') as f:
#         # read contents 
#         contents = f.read() # return string
#     # display contents
#     print(contents)

# # function call
# read_file('days')
# read_file('months')

# -------------------- Example 2 -----------------------

# Define a function within a function
# def say() -> str:
#     #local variable
#     greeting = "Hello"

#     def display():
#         # greeting is defined outside the inner function 
#         print(greeting)

#     # call the inner function
#     display()

# # try to print greeting
# print(greeting)

# # call the outer function
# say()


# -------------------- Example 3 -----------------------

# Define a function to call another function

# def add(num1, num2, num3 ) -> int:
#     return num1 + num2 + num3

# def multiply(a, b) -> int:
#     return a * b

# def calculate(operation, *arg) -> str:
#     result = operation(*arg)
#     print("Result:", result)

# calculate(multiply, 3, 4)
# calculate(add, 1, 2, 3)


# ----------------- Example 4 ----------------------------------
# # Define a function to display arguments and keyword arguments

# def print_arguments(*args, **kwargs) -> str:
#     for arg in args:
#         print(arg)
#     for key, value in kwargs.items():
#         print(f"{key}: {value}")

# print_arguments("apple", "banana", "cherry", color="red", size="small")

