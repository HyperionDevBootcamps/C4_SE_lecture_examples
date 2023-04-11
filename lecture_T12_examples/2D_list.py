#*************Example 1****************
# 2D List Example
# Variables to store row and column sizes
number_of_rows = 3
number_of_columns = 2

# Create a 2x3 list, all elements are the value None
empty_grid = [[None]*number_of_columns for row in range(number_of_rows)]

print(empty_grid)

for row in empty_grid:
    for column in row:
        print(column)

#*************Example 2****************
# This is a 2D list
my_2d_list = [[1,2,3],[4,5,6],[7,8,9]]

# Print all the elements in the 2D list
for row in my_2d_list:
    #print(row)
    for col in row:
        print(col, end = " ")
    print()

