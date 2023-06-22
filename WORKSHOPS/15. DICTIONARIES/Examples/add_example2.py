# **************Create a dictionary using data from a text file************

# open a file to read data from
with open("students.txt", "r") as file:
    # create a list consisting of all the student information
    file_data = file.read().split('\n')
       
# Hint: Check the contents of the list
#print(file_data)

all_data =[]
# iteratate through the list 
for each_element in file_data:
    # create a new list
    criteria_list = each_element.split(";")
    # create empty dictionary
    student_data_dict = {}
    
    # Hint: Check you new list
    #print(criteria_list)

    # add elements to the empty dictionary
    student_data_dict["name"] = criteria_list[0] #John
    student_data_dict["surname"] = criteria_list[1]
    student_data_dict["age"] = criteria_list[2]
    student_data_dict["degree"] = criteria_list[3]

    all_data.append(student_data_dict)

    # Hint: Check the dictionary items
    #print(student_data_dict)

#print(all_data)

for data in all_data:
    print(data["name"])