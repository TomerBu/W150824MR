# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# fruits2 = fruits[:]  # copy the list

# fruits2 = fruits.copy()
# fruits2.clear()
# print(fruits)
# fruits2 = fruits 
# fruits2.clear()
# print(fruits) 


# print(fruits[0])  # apple
# print(fruits[-1])  # mango


# print(fruits[1:3] )  #1(inclusive) to 3(exclusive)


# # start defaults to 0
# print(fruits[:3])

# # end defaults to len(list)
# print(fruits[2:])  # 2 to end


# # all the elements but the last #['apple', 'banana', 'cherry', 'kiwi']
# print(fruits[:-1])


# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# print(numbers[::-1]) # step -1


# phrase = "Monty Python!"
# print(phrase[:-1]) #Monty Python

# print(phrase[::-1]) #nohtyP ytnoM


# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

# # copy all the fruits but the banana
# fruits_copy = fruits[:1] + fruits[2:]

# # copy all the fruits but the banana
# fruits_copy = []
# for fruit in fruits:
#     if fruit != "banana":
#         fruits_copy.append(fruit)


# from random import randint
# random_numbers = [randint(1, 100), randint(1, 100), randint(1, 100), randint(1, 100)]


# even_numbers = [num for num in random_numbers if num % 2 == 0]



#in ניתן לבדוק האם מחרוזת מכילה מחרוזת נתונה באמצעות האופרטור 
#not in ניתן לבדוק האם מחרוזת מכילה מחרוזת נתונה באמצעות האופרטור 

# 
# print("a" in "apple")  # True
# print("b" in "apple")  # False

# print("banana" not in "apple pie")  # True


# # also works with lists:
# fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# print("apple" in ["apple", "banana", "cherry"])  # True
# print("apple" in fruits)  # True

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_copy = [fruit for fruit in fruits if "a" in fruit]
print(fruits_copy)  # ['apple', 'banana', 'mango']