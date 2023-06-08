#*************Example 1******************
# Write contents to a file using with/as block
with open('output.txt','w') as file:

    file.write("Mankind knew, that they cannot change society.\n")
    file.write("So instead of reflecting on themselves. \n")
    file.write("They blamed the beast")

# The .write() method, will write any data we provide 
# within the parentheses to our file
# and since we are using a with/as block
# we don't need to close the file with .close()

#**************Example 2**************
# An alternative method to write contents to a file 
file_name = 'output.txt'

file = open(file_name,'w')

file.write("Mankind knew, that they cannot change society.\n")
file.write("So instead of reflecting on themselves. \n")
file.write("They blamed the beast")

file.close()

#***************Example 3*******************
# Using the 'a' access mode will prevent data to be over written
# Open the file again
file_name = 'output.txt'  # This is the original text file

file = open(file_name,'a+')

file.write("This is the new text")

lines = file.read()

print(lines)

file.close()

#Open and read the contents in the text file
file_name = 'output.txt'

file = open(file_name, 'r')

for lines in file:
    print(lines.replace('\n',''))

file.close()
