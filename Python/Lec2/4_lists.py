lst = [int(input("Enter a number: ")), int(input("Enter a number: ")), int(input("Enter a number: "))]  

# add
lst.append(500)
lst.insert(1, 200) # insert 200 at index 1

# remove
lst.pop() # remove the last element
lst.pop(1) # remove the element at index 1
lst.remove(200) # remove by value

# update a value:
lst[0] = 100

# read:
print(lst[0]) # 100
print(lst) 
 