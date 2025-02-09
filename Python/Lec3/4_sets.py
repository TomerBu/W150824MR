# # יש להגריל 3 מספרים שונים בין 1 ל10

# from random import randint

# def distinct_random_numbers_v1(n, start = 0, end = 10):
#     winners = []

#     while len(winners) < n: #o(n*n)
#         num = randint(start, end)
#         if num not in winners:
#             winners.append(num)
#     return winners

# def distinct_random_numbers(n, start = 0, end = 10):
#     winners = set()

#     while len(winners) < n: #o(n)
#         num = randint(start, end)
#         winners.add(num)
#     return winners

# creating sets:
s1 = {1, 1, 4, 4, 5} # {1, 4, 5}

# creating sets from list:
my_list = [1, 1, 4, 4, 5] # [1, 1, 4, 4, 5]
s2 = set(my_list) # {1, 4, 5}

# creating sets from string:
s3 = set('hello') # {'h', 'e', 'l', 'o'}

# create empty set:
s4 = set() # new empty set



s = {1, 2, 3, 4, 5}

s.add(6) # {1, 2, 3, 4, 5, 6}
s.add(6) # {1, 2, 3, 4, 5, 6} # no change
s.update({7, 8, 9}) # {1, 2, 3, 4, 5, 6, 7, 8, 9}

# cant remove element that not exists (error)

if 7 in s:
    s.remove(7) # KeyError: 7

s.discard(7) # {1, 2, 3, 4, 5, 6} # no error


batman = {'Christian Bale', 'Michael Keaton', 'Ben Affleck'}
american = {'Christian Bale', 'Ben Affleck', 'Tom Hanks'}

# union
union = batman.union(american) # {'Christian Bale', 'Michael Keaton', 'Ben Affleck', 'Tom Hanks'}
union = batman|american # {'Christian Bale', 'Michael Keaton', 'Ben Affleck', 'Tom Hanks'}

# intersection
intersection = batman.intersection(american) # {'Christian Bale', 'Ben Affleck'}
intersection = batman & american # {'Christian Bale', 'Ben Affleck'}

# difference
difference = batman.difference(american) # {'Michael Keaton'}
difference = batman - american # {'Michael Keaton'}

# symmetric difference
symmetric_difference = batman.symmetric_difference(american) # {'Michael Keaton', 'Tom Hanks'}
symmetric_difference = batman ^ american # {'Michael Keaton', 'Tom Hanks'}


# convert set to list
actors_list = list(batman ) # ['Christian Bale', 'Michael Keaton', 'Ben Affleck']
actors_list.append('Ben Affleck')


given_list = [2, 2, 4, 4, 3, 4, 7, 8, 10]
# convert list to set
as_set = set(given_list) # {2, 3, 4, 7, 8, 10}


# remove duplicates from list:
list(set(given_list)) # [2, 3, 4, 7, 8, 10]




# Display results
print("🔹 Common technologies:", common_features)
print("🔹 All technologies combined:", all_features)
print("🔹 Technologies only in Country A:", only_A)
print("🔹 Technologies only in Country B:", only_B)
print("🔹 Unique technologies (not shared):", unique_features)
print("🔹 Does A include all of B?", A_includes_B)
print("🔹 Does B include all of A?", B_includes_A)
