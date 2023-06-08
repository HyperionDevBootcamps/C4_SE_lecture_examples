#*************Example 1****************
# Create an empty dictionary
my_dict = {}

# Add key values to the dictionary
my_dict[1] = "rugby"
my_dict[2] = "tennis"
my_dict[3] = "cricket"
my_dict[4] = "football"

print(my_dict)

# Changing a value
my_dict[1] = "basketball"

print(my_dict)

# Membership test
print(4 in my_dict)
print(5 in my_dict)

#****************Example 2*******************
# An example using lists and dictionaries to calculate the average grade of a student
# Create a list which contains the names of three subjects
subjects_list = ["English", "Mathematics", "History"]

# Create a dictionary which contains the grade achieved by a student for
# each subject in the list

grades = {"English" : "82",
         "Mathematics" : "78",
         "History" : "68"}

# Create an empty list for the grades 
grade_list = []

# A for loop to iterate over the items in the subjects_list, 
# extract values from the grade dictionary and add the values to a new list
for subject in subjects_list:
    grade_list.append(grades[subject])

# Loop over each grade in grade_list and casting it to an integer
int_grade_list = [int(grade) for grade in grade_list] #[82,78,68]

# Calculate the average
average = sum(int_grade_list)/len(grade_list)

print(int(average))

