#***************LIST METHOD***************
print("Example 1:")
num_list = [23, 16, 46, 1, 6, 74, 86, 31, 6, 4, 16]

# extend() method - takes a list as an argument

# insert() - takes an index,value argument

# remove() - takes a value as an argument

# pop() - takes an index number as an argument

# index() - takes a value as an argument

# count() - takes a value as an argument

# sort() - takes no arguments 

# reverse() - takes no arguments



#**************COPYING LIST*******************
print("Example 2:")
# Remember to import the copy module
import copy

a = [[1, 1, 1], [1, 1, 1]] #2D list

# Shallow copies - sublists in original list can be modified
# if the corresponding inner lists in shallow-copied lists are modified
b = copy.copy(a) # b = [[1, 1, 1], [1, 1, 1]]
c = a[:]        # c = [[1, 1, 1], [1, 1, 1]]

# change the value of one of the elements in a sublist
b[0][0] = 2  # b =[[2, 1, 1], [1, 1, 1]]  a =[[2, 1, 1], [1, 1, 1]]  c = [[2, 1, 1], [1, 1, 1]]
c[1][1] = 5     # c = [[2, 1, 1], [1, 5, 1]]   a = [[2, 1, 1], [1, 5, 1]] b = [[2, 1, 1], [1, 5, 1]] 

print("List a:")
print(a)
print("List b:")
print(b)
print("List c:")
print(c)

# Re-assign list a
a = [[1, 1, 1], [1, 1, 1]] #2D list

# deep copy - sublists in original list cannot be modified 
d = copy.deepcopy(a)  # d = [[1, 1, 1], [1, 1, 1]] 

d[1][2] = 6     # a = [[1, 1, 1], [1, 1, 6]] 

print("List a:")
print(a)
print("List d:")
print(d)

# **************LIST COMPREHENSION*********
# List comprehension can be used to construct lists in an elegant and concise way.
# It is a powerful tool that will apply some operation to every element in a List, 
# and then put the element into a new List.
# List comprehension consists of an expression followed by a 
# for statement inside square brackets.

print("\nExample 3:")

num_list = ['1', '5', '8', '14', '25', '31']
print(num_list)

# One way of casting the list elements and putting them in a new list:
new_list = []
for element in num_list:
    new_list.append(int(element))
print(new_list)

# Or you could use list comprehension
new_num_list_ints = [int(element) for element in num_list]
# We are looping over num_list, which is a List of strings
# For each element, we are casting it to an Integer and 
# putting it into a new List, new_num_list_ints.

print(new_num_list_ints) 

# You can do many operations with List comprehensions.
double_list = [ 2 * element for element in new_num_list_ints ]

print(double_list)

# ***USING LIST AND DICTIONARIES TO PERFOR A CALCULATION****
# An example using lists and dictionaries to calculate the average grade of a student
# Create a list which contains the names of three subjects
subjects_list = ["English", "Mathematics", "History"]

subjects_list.append("chemistry")

print(subjects_list)

grades = {"English" : "82",
         "Mathematics" : "78",
         "History" : "68"}

grades["chemistry"] = "50"

print(grades)

# Create an empty list for the grades 
grade_list = [  ]

for subject in subjects_list:
    grade_list.append(grades[subject])

int_grade_list = [int(grade) for grade in grade_list] 
# Expected outcome: int_grade_list = [82, 78, 68, 50]

# Calculate the average
average = sum(int_grade_list)/len(int_grade_list)

print(average)

