# Request user to enter their test score
test_score = int(input("Please enter your test score: "))

# Declare boolean variable
Pass = False

# If-elif-else statement to clasify test scores
if (test_score <= 30):
    Pass
    print("Sorry, keep on trying")
elif (test_score <50):
    Pass 
    print("You qualify for a re-write")
elif (test_score <= 79):
    Pass = True
    print("Well done!")
else:
    print("You've passed with a distinction! Congratulations!")
    Pass = True
    

# If statement to display outcome
if Pass == True:
    print("Outcome: passed")
else:
    print("Outcome: Failed")

