#************Example 2***************
# You can also read the contents in a file using a for loop
# Call and open the external file like we've done before
# file_name = 'input.txt'
# file = open(file_name, 'r', encoding='utf-8')

# # A for loop to iterate over the lines in the file object
# for line in file:
#     print(line)
    
#  # Remember to close file
# file.close()

# Alternatively, you can open a file using a with/as block
with open('input.txt', 'r') as file:
    for line in file:
        print(line, end='')

# You do not need to close the file 
# because it has reached the end of block
