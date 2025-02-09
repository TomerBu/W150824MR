
# new dictionary:
dict1 = {}
dict2 = dict()
dict_3 = {
    "name": "moe" ,
    "age": 30
}
dict_4 = dict(name="moe", age=30)


batman_dict = {
    "Dark Knight": "Christian Bale",
    "Batman": "Michael Keaton",
    "Batman v Superman": "Ben Affleck"
}

# get value by key:
print(batman_dict["Dark Knight"]) # Christian Bale

#print(batman_dict["Darkest Knight"]) # Raise KeyError

# get value by key with get method: avoid KeyError
print(batman_dict.get("Darkest Knight")) # None


counter_dictionary = {
    "a": 3,
    "b": 1,
    "n": 2
}

#update a value:
counter_dictionary["a"] = 2

# add a value:
counter_dictionary["j"] = 1

# remove a value:
del counter_dictionary["j"]
ac = counter_dictionary.pop("a")
counter_dictionary.popitem() # remove last item
counter_dictionary.clear() # remove all items



harry_potter_books = {
    "Philosopher's Stone": 1997,
    "Chamber of Secrets": 1998,
    "Prisoner of Azkaban": 1999,
    "Goblet of Fire": 2000
}

for key in harry_potter_books.keys():
    print(key)

for value in harry_potter_books.values():
    print(value) # 1997, 1998, 1999, 2000

for key, value in harry_potter_books.items():
    print(key, value)



person_dict = {
    "name": "moe",
    "age": 30
}

# check if key exists:
if "name" in person_dict:
    print(person_dict["name"])

if "birthday" not in person_dict:
    print("birthday not exists")