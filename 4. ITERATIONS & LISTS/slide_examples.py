#*****************FOR LOOP***************************
# No need to do this
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")
print("")

#********************************************
# For loop to the rescue...
for iteration_var in range(10):
    print("")

#********************************************
string = "coffee"
for letter in string:
    print(letter)

for num in range(1,10,2):
    # Take note that the ending value 10
    # is exclusive.
    # similar to string slicing
    print(num)

#********************************************
for num in range(1,10,2):
    print(num) # output: 1, 3, 5, 7, 9

#********************************************
for num in range(10,1,-1):
    print(num) # output: 10, 9, 8, 7, 6, 5, 4, 3, 2

#********************************************
for i in range(1,10):
    for j in range(9,10):
        print(f"{i} x {j} = {i*j}")

#**************************WHILE LOOPS***********************************
# while loop example
option = input("Whould you like to add a chocolate to your cart? (y/n): ")
num_of_choc = 0

while option == "y":

    num_of_choc += 1 # num_of_choc = num_of_choc + 1
    print(f"You have {num_of_choc} chocolate(s) in your cart!")

    #option = input("Do you want to add another chocolate to you cart?(y/n): ")

    if num_of_choc < 10:
        option = input("Do you want to add another chocolate to you cart?(y/n)")

    else:
        print("You have added the maximum amount of chocolates allowed!")
        break # Remember to break the loop

#*************************************************************************
#infinte loop
while True:
    print("I am an infinte loop")
    print("And you can't stop me!")
    
    stop = input("Do you wish to stop me? (y/n)")

    if stop == "y":

        print("As you wish!")
        break

#*************************************************************************
#while loops
while True:
    print("I am a loop")

    question = input("Would you like the loop to continue? (y/n)")

    if question == "y": # rather use an if statement
        
        print("As you wish!")
        continue # skip the rest of the lines within the loop for the current iteration 

    else:
        
        print("I shall cease")
        break # exit the loop completely