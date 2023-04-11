#***********Example 1*************
# A while loop to print numbers from zero to 10
# Declare a counter/control variable
num = 0

while num <= 10:
    print(num)
    # Increase control variable
    num += 1


#************Example 2*****************
# A program to print all numbers from zero to 19.
# If the number is 20 the loop will break and the 
# sum of the numbers will be displayed

# Declare control variables
num = 0
sum = 0

# A while loop to print all numbers less than 20 
while num < 20:
    print(num)
    
    # Increase control variable
    sum = sum + num   # sum += num
    num = num + 1     # num += 1
    

    if num == 20:
        print(sum)
        break


