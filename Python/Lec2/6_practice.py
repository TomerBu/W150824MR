from random import choice

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "pear", "pineapple", "strawberry", "watermelon"]

# random fruit:
random_word = choice(fruits)


apples = list("🍏"*len(random_word))
print(apples) #['🍏', '🍏', '🍏', '🍏', '🍏', '🍏', '🍏', '🍏', '🍏']

