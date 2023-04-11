#**************Additional example********
# This program writes user input to a text file
# Create and open text file
with open('user.txt','w') as file:
    #Request user input
    user_name = input("Please enter your name: ")
    user_surname = input("Please enter your surname: ")

    # Write user input to text file
    file.write(user_name +'\n')
    file.write(user_surname)
