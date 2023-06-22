#*******************Write data to a text file and create a dictionary*************
# access files
import os

# check if file exists in current directory
if not os.path.exists("course.txt"):
    # open or create file
    with open("course.txt", "w") as default_file:
        # write name;code in file
        default_file.write("name;code")
        
# open the course.txt file 
with open("course.txt", 'r') as user_file:
    # create list to store data in course.txt line by line
    course_data = user_file.read().split("\n")
    # print(course_data = ['name;code','Maths;WTW123']


# create an empty dictionary
name_code_dict = {}

# access elements inside the course_data list
for course in course_data:
    name, code = course.split(';') #[Math,WTW123]
    # name = 'Math'
    # code = 'WTW123'
    name_code_dict[name] = code
    #name_code_dict['Math'] = WTW123

# print(name_code_dict)

print(name_code_dict["History"])
