#******************* LIST METHODS *******************

#list_1D = [1,2,3,4,5,6,7,8,9,2]

# indexing
#print(list_1D[3])

# len()
#print(len(list_1D))

# append()
# list_1D.append(10)
# print(list_1D)

# extend()
# list_1D.extend([20,14,17])
# print(list_1D)

# insert()
# list_1D.insert(2,16)
# print(list_1D)

# clear()
# list_1D.clear()
# print(list_1D)

# pop()
# popped_num = list_1D.pop()
# print(popped_num)
# print(list_1D)

# count()
#print(list_1D.count(8))


#********************* 2D Lists ******************
#          c0 1 2   c0 1 2
#list_2D = [[1,5,7], [2,4,6], [6,3,9]]
#              r0      r1       r1

# indexing
#print(list_2D[0][1])

# len()
#print(len(list_2D))

# insert()
# list_2D.insert(1,[10,5,8])
# print(list_2D)

#******************* LIST COMPREHENSION ***********************

# Example 1: Simple list comprehension

# Creating a list of numbers in a range without list comprehension
# list1 = []
# for num in range(0,7):
#     list1.append(num)
# print(list1)

# Alternately, use list comprehension
# list2 = [num for num in range(0,7)]
# print(list2)


# Example 2: Conditional statement within comprehension logic

# Create a list of even numbers from 95 to 126.

# list1 = []
# for num in range(95,126):
#     if num % 2 == 0:
#         list1.append(num)

# print(list1)

# list2 = [num for num in range(95,126) if num % 2 == 0]

# print(list2)

# Example 3: Creating a 1D list from a 2D list

# with list comprehension
# data = [[1,2,3], 
#     [4,5,6],   
#     [7,8,9]]

# new_data = [col_data for row in data for col_data in row]
# print(new_data)

# without list comprehension
# list_data = []
# for row in data:
#     for col_data in row:
#         list_data.append(col_data)
# print(list_data)


# Example 4: Filtering iterable using list comprehension 

# students = [['John',17], ['Mary', 18], ['Alice', 21], ['Peter', 23], ['Nick', 20 ]]

# Create list of student older than 18

# new_list =[]
# for student in students:
#     if student[1] > 18:
#         new_list.append(student[0])

# print(new_list)

# with list comprehension

# student_above_18 = [student[0] for student in students if student[1] > 18]

# print(student_above_18)


# Example 5: 2D Grid


# list = [[1,2,3],[4,5,6], [7,8,9]]
# # without list comprehension
# for row in list:
#     for col in row:
#         print(col, end=" ")
#     print()

# # display a grid using list comprehension
# list_x = [["x" for col in row] for row in list]

# print(list_x)



#**************** Fun example*****************
message = input("Enter a message: ")

mes_list = message.split()

new = []
for item in mes_list:
    if item == ':)':
        item = '🙂'
    new.append(item)

print(" ".join(new))







    
    

