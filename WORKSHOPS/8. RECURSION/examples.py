# Count backward to zero using recursion
def count_backwards(start_point):
    if start_point == 0:
        print(start_point) # Base case
        
    else:
        print(start_point)
        count_backwards(start_point-1)
        
# count_backwards(5)


# Determine the sum of a list of numbers recursively
# [2,3,4] 2 + 3 + 4
# [5,6,8] 5 + 6 + 8

def sum_values(num_list):
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + sum_values(num_list[1:])
                # 2  + (sum_values([3,4]) = 7)
                     # 3 + (sum_values([4]) = 4)
                          #    4 
       
    
# print(sum_values([2,3,4]))
    

# Determine value of a number to the power of a given number 2^3 (2x2x2)
def power(num, exponent):
    if exponent == 1:
        return num
    else:
        return num * power(num, exponent-1)
    
# print(power(5, 0))



# Reverse a string value recursively  sit    tis
def reverse_string(data):
    if len(data) == 1:
        return data
    else:
        return reverse_string(data[1:]) + data[0]
                #   t + i + s
                   #    t + i
                      #     t
                      
# print(reverse_string("sit"))                      

def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num-1)
    
# print(factorial(5))