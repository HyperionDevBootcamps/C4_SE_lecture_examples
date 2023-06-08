#************Example 1***************
# Changing every third character to uppercase
string = 'Learning python is fun'

#Create a new string
new_string = ""

# A for loop to change every third letter to an upper case letter
for i in range(len(string)):
    if i % 3 == 0:
        new_string = new_string + string[i].upper()
    else:
        new_string += string[i].lower()

print(new_string)

#***********Example 2*****************
string = "Learning python is fun"

#Create a list using the split method
list_string = string.split()

print(list_string)

#Add '!' to the end of the list
list_string.append("!")

print(list_string)

#Print every second character in the list
for i in range(len(list_string)):
    if i % 2 == 0:
        print(list_string[i])

#Now change the list back to a string
new_string = " ".join(list_string)

print(new_string)