#*************Example 4******************
# Write contents to a file using with/as block
with open('output.txt','w') as file:

    file.write("Mankind knew, that they cannot change society.\n")
    file.write("So instead of reflecting on themselves. \n")
    file.write("They blamed the beast")

# The .write() method, will write any data we provide 
# within the parentheses to our file
# and since we are using a with/as block
# we don't need to close the file with .close()
