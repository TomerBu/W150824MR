def stats(*numbers):
    return sum(numbers), max(numbers), min(numbers), len(numbers), sum(numbers) / len(numbers)


def gas_prices():
    return (7.1, 7.2, 8.0)

benzin, diesel, octan = gas_prices()


def card_suits():
    return ("❤️", "♦️", "♠️", "♣️")

result = stats(100, 20, 30, 40, 50)

print("sum", result[0])
print("max", result[1])
print("min", result[2])
print("count", result[3])
print("average", result[4])


m_tuple = (1, 2, True, 4, 5)
print(m_tuple)
print(m_tuple[0])


tuple_from_list = tuple([1, 2, 3, 4, 5])

m_tuple_with_single_element = (1,)
m_tuple_with_single_element = (1) # this is not a tuple

# We cannot change the value of a tuple
m_tuple[0] = 100 # this will throw an error


tuple_1 = (1, 2, 3)
tuple_2 = (4, 5, 6)

tuple_3 = tuple_1 + tuple_2 # (1, 2, 3, 4, 5, 6)


# tuple unpacking
tuple_demo = ("John", "Doe", 30)

first_name, last_name, age = tuple_demo
print(first_name, last_name, age)



data = ('John', 'Doe', 30)

first_name, last_name, age = data

my_dict = {
    "name": "moe" ,
    "age": 30
}

