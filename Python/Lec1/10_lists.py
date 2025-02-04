from random import randint, choice

# print(choice(my_list))
# print(len(my_list)) # 5 (number of elements in the list)


my_list = ['a', 'b', 'c', 'd', 'e']

# insert: 
my_list.append('f') # add an element to the end of the list
my_list.insert(6, 'g') # insert an element at a specific index

# update:
my_list[0] = 'A' # update the element at index 0

# delete:
# delete by index:
del my_list[6] # delete the element at index 6

# delete by index:
my_list.pop(0)

# delete the last item:
my_list.pop()

# delete by value:
my_list.remove('c')

# print the list:
print(my_list)
print(my_list[0])
