#**************Example 1************
# Declare a variable to store the file object
file_name = "input.txt"

# Declare a variable to call the open() function  
# on the file you wish to open - a file object will be returned
# Remember to include the access mode as an argument eg 'r'
# 'r' allows Python to read the contents of the file
file = open(file_name, 'r', encoding='utf-8')

# Read methods: .read(), readline(), readlines()
# To read the contents in the file use the .read() method
# Declare a variable to store all the contents from the text file 'input.txt'
lines = file.readlines()

# Display contents - call the print function on the 'lines' variable
print(lines)

# Remember to close your file
file.close()