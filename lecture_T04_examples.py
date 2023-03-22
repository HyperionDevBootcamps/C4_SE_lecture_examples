# Request user to enter their test score and semester average
semester_average = int(input("Please enter your average mark for the semester: "))
exam_score = int(input("Please enter your exam score: "))

# Declare boolean variable
Pass = True

# If-elif-else statement to clasify exam score and semester average
if (exam_score < 40) and (semester_average < 50):
    Pass = False
    print("Sorry, keep on trying")
elif (exam_score < 50 and exam_score >= 40 ) and (semester_average >= 50) :
    Pass = False
    print("You qualify for a re-write")
elif (exam_score >= 50 and exam_score <= 79) and (semester_average >= 50):
    Pass 
    print("Well done!")
else:
    print("You've passed with a distinction! Congratulations!")
    Pass 
    

# If statement to display outcome
if Pass == True:
    print("Outcome: Passed")
else:
    print("Outcome: Failed")

# There is a logical error - See if you can correct it :)