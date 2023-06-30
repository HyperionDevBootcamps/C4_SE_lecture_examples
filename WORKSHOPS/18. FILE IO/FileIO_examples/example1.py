# Read contents from one file and print some of the contents to another file
input_file = open('fav_sport.txt', 'r')

# Create a list consisting of lines containg information of each line
lines_list = input_file.readlines()
print(lines_list)

# create an empty list
id_list = []
# iterate through the lines_list
for item in lines_list:
    item_list = item.split(" ")
    id_list.append(item_list[0])
    print(item_list[0])

print(id_list)

# create a file to write contents to
output_file = open('id.txt', 'w')

# iterate through list items 
for id_num in id_list:
    id_num += "\n"
    # write id number to text file
    output_file.write(id_num)

