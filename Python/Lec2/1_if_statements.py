# x = int(input("Enter a number"))
# y = int(input("Enter a number"))
# z = int(input("Enter a number"))

# lst = [x, y, z]

# smallest = lst[0]

# for num in lst:
#     if num < smallest:
#         smallest = num

# print(smallest)

# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)


x = 400 
y = 200 
z = 100
 
if x > y: 
    #swap the values
    x, y = y, x
if y > z:
    #swap the values
    y, z = z, y
if x > y: 
    #swap the values
    x, y = y, x