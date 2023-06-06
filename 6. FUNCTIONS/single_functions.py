#**************User defined functions******************
#Example 1 : Create a function to greet the user

# You could do this without the use of functions:
# my_name = input("Please enter your name: ")
# name_length = len(my_name)
# print(f"Hello {my_name}! Your name is {name_length} characters long") 

# We can use a function to hide the details (this process is called abstraction)
# def greet():
#     my_name = input("Please enter your name: ")
#     name_length = len(my_name)
#     print(f"Hello {my_name}! Your name is {name_length} characters long")

# greet() # call the function


#Example 2 : Conversion calculator
# def ounces_to_grams(weight):
#     return weight * 28.3495

# # Argument
# weight_in_ounces = int(input("Enter the amount in ounce: "))

# # Call the function
# weight_in_grams = ounces_to_grams(weight_in_ounces)

# # Display answer
# print(f"{weight_in_grams} g")


#Example 3: Create a function to extract the largest numbers in a list 

# Take the following code:
# my_list = [5, 7, 34, 5, 3, 545]
# big_numbers = []
# for num in my_list:
#     if num > 10:
#         big_numbers.append(num)
# print(big_numbers)

#and convert the data-processing parts to a function called get_larger_numbers which can be called like:
#my_list = [3, 7, 34, 5, 9, 545]
# a_list = [4,6,19]

# def get_largest_numbers(list):
#     big_numbers = []
#     for num in list:
#         if num > 10:
#             big_numbers.append(num)
#     return big_numbers

# large_numbers = get_largest_numbers(a_list)
# print(large_numbers)


# Example 4: Converting a message to a morse encoded message
#If you would like to learn more about morse code, visit this link: https://en.wikipedia.org/wiki/Morse_code
# letter_to_morse = {
#     'a':'.-', 'b':'-...', 'c':'-.-.', 'd':'-..', 'e':'.', 'f':'..-.', 
#     'g':'--.', 'h':'....', 'i':'..', 'j':'.---', 'k':'-.-', 'l':'.-..', 'm':'--', 
#     'n':'-.', 'o':'---', 'p':'.--.', 'q':'--.-', 'r':'.-.', 's':'...', 't':'-',
#     'u':'..-', 'v':'...-', 'w':'.--', 'x':'-..-', 'y':'-.--', 'z':'--..',
#     '0':'-----', '1':'.----', '2':'..---', '3':'...--', '4':'....-',
#     '5':'.....', '6':'-....', '7':'--...', '8':'---..', '9':'----.', ' ':'/'
# }

# message = "SOS We have hit an iceberg and need help quickly"

# def encode(message): #parameter
#     morse = [] #list
#     morse_message = ""
#     for letter in message:
#         letter = letter.lower()
#         morse_letter = letter_to_morse[letter] #letter_to_morse["s"] = "..."
#         morse.append(morse_letter)

#     morse_message = " ".join(morse)
#     return morse_message
        
# incoming_message = "SOS We have hit an iceberg and need help quickly"

# print(f"Incoming message: {message}")
# print(f"Morse encoded: {encode(incoming_message)}") 


#*******************Built-in function**************** 
#Example: Create your own enumerate function

# list = ["cat", "dog", "horse"]

# #The built-in enumerate function in Python
# for element in enumerate(list):
#     print(element)

# #Let's create our own enumerate function:
# def enume(iterable, start=0):
#     n = start
#     for elem in iterable:
#         yield n, elem # yield suspends the function to go back where it started/ pause function
#         n += 1

# for element in enume(list, start=0):
#     print(element)
