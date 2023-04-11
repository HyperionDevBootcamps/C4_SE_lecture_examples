#***********Example 1************
# Method 1: Create a dictionary using {}
print("Example 1: Creating dictionaries \n")
print("Method 1: Using {}")
my_dictionary = {
    "name" : "Terry",
    "age" : 23,
    "is_funny" : False
}

print(my_dictionary)
print()
#Method 2: Create a dictionary using the dict() function
print("Method 2: Using the dict() function")
new_dictionary = dict(name ="Terry", age = 23, is_funny = False)

print(new_dictionary)  
print()
#*************Example 2**************
# Accessing values in a dictionary by calling the key
# print("Example 2: Accessing values in a dictionary")

new_dictionary = dict(name ="kitty", age = 0.5, kitten = True)

print(new_dictionary["name"])
print(new_dictionary["age"])
print(new_dictionary["kitten"])
print()

#*************Example 3*************
print("Example 3: Accessing all keys and values")

# Method 1: Accessing keys and values
# using the .keys() and .values() functions
# to display them in lists
print("-> Method 1: Access all keys and values in lists")
new_dictionary = dict(name ="kitty", age = 0.5, kitten = True)

# Convert dict_keys/ dict_values objects to lists 
x = list(new_dictionary.keys())
y = list(new_dictionary.values())

print(x)
print(y)

# Use a for loop to iterate over keys in x (renamed to keys_list)
print("These are all the keys: ")
for key in x:
    print(key)

# Use a for loop to iterate over keys in y (renamed to values_list)
print("These are all the values: ")
for value in y:
    print(value)


# Method 2: Accessing keys and values using for loops 
print("-> Method 2: Access all keys and values using for loops")
print("These are all the keys: ")
for keys in new_dictionary.keys():
    print(keys)

print("These are all the values: ")
for values in new_dictionary.values():
    print(values)

#**************Example 4**************
#Using the .item() method on dictionaries in a for loop
#to access all keys and values
print("Example 4: Accessing both keys & values")

for keys, values in new_dictionary.items():
    print(keys, " : ", values)

#************Example 5*************
# Use the .pop() method to remove a key value pair from a dictionary
# .pop("argument") where argument is the key
print("Example 5: Popping out of a dictionary")
value = new_dictionary.pop("name")
print(value)

# **********Addtional Example*************
# Changing the value of an element in the dictionary
new_dictionary["age"] = 1

print(new_dictionary)






 