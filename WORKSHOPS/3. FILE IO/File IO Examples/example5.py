#***************Example 5*******************
# Using the 'a' access mode will prevent data to be over written
# Open the file again
file_name = 'output.txt'  # This is the original text file

file = open(file_name,'a+')

file.write("\nThis is the new text")

# Important: return to the top of the file before reading
file.seek(5) 

lines = file.read()

print(lines)

file.close()
