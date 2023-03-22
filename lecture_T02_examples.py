# name = "Peter"
# surname = "Parker"

# full_name = name + surname
# full_name = name + " " + surname

# print(full_name)

# age = 32

# print(full_name + age) # TypeError: can only concatenate str (not "int") to str

# -------------------------------------------------------------------------------
#Let's say you want the program to output a sentence containing the (full) name and age of someone

##For these example I'll update the variable called name to contain both the name and the surname
#name = "Peter Parker"

##One way of doing this would be to concatenate (join) the words of the sentence and the variables  (Method 1)
#print("My name is " + name + " and I'm " + str(age) + " years old") #Casting Integer to String.

##Another way - using the format() method (Method 2)
#print("My name is {} and I'm {} years old.".format(name, age)) 

##Or assign a variable to the statement and then print the variable called sentence
#sentence = "My name is {} and I'm {} years old.".format(name, age)
#print(sentence)

##Using the f-strings
# sentence = f"My name is {name} and I'm {age} years old."
# print(sentence)

# # String methods
#message = "PyThOn Is FuN"

# # display all letters in upper case
# new_message = message.upper()
# print(message)
# #or you could do it all inside the print function
#print("Python is fun".upper())

# # The split() method converts the string argument into a list of strings
# message_split = message.split()
# print(message_split)

# # The join() method concatenate a list elements form on string
# list_join = " ".join(message_split) 
# print(list_join) 

# The replace() method requires two arguments - first the character that you wish to replace
# and then the new character 

# message_replace = message.replace(" ", "*")
# print(message_replace)

# # Escape sequence
# # Tab space escape sequence
# string1 = "Coding\tis\tfun"
# print(string1)

# print("len(string1)= {:10}".format((len(string1)))) 


# String slicing 
# word = "Programming"
# word_slice1 = word[0:7]  #outputs: Program
# word_slice2 = word[:7]  #outputs: Program
# word_slice3 = word[8:]  #outputs: ing

# print(word_slice1)

# # Extended slicing
# # Syntax - [begin:end:step]

# word_slice4 = word[3::2]
# word_slice5 = word[-1::-1]

# print(word_slice5)


