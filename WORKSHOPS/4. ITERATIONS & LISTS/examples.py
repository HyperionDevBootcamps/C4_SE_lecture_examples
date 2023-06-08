#List methods
num_list1 = [1,2,3,4,5]

num_list2 = [7,8,9,10,11]

#Extend
num_list1.extend(num_list2)

#insert & pop
num_list1.insert(5,6)

num_list1.pop()
print(num_list1)

#len & sum
print(len(num_list1))
print(sum(num_list1))

#sorted
print(sorted([4,5,10,2,19]))

#list comprehension
list = [(x+1) for x in range(5) if x % 2 == 0]
print(list)

list1 = []
for x in range(0,5): # 0, 2, 4
    if x % 2 == 0: # 0 , 2,  4
        list1.append(x+1) # 0 + 1, 2 + 1, 4 + 1
print(list1) # [1, 3, 5]

#copy
import copy
x = [[1,4,7], [2,9,5]]

y = copy.deepcopy(x) # deep copy

# y = [[1,4,7], [2,9,5]]
y[0][0] = 10

print(y)
print(x)

#indexing
animals = ["cat", "dog", "horse", "rabbit", "bee"]

print(animals[1])
print(animals[1:3])

#enumerate
for animal in enumerate(animals,1):
    print(animal)