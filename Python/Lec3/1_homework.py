# def input_of_an_array():
#     word = input("Enter a word: ")
    
#     lst = []
#     for letter in word:
#         lst.append(letter)

#     return lst

# def input_of_an_array_v2():
#     word = input("Enter a word: ")
#     return [letter for letter in word]

# def input_of_an_array_v3():
#     return list(input("Enter a word: "))


def input_array_of_numbers():
  input_string = ""
  lst = []
  while input_string != ".":
    input_string = int(input("Enter a number or type '.' to finish: "))
    if input_string != ".":
      lst.append(input_string)  



def input_array_of_numbers_v2():
    sequence = input("Enter a sequence of numbers separated by comma: ").strip()
    lst = sequence.split(",")
    return [int(num) for num in lst]


def star_rect():
    for row in range(10):
        # print 5 stars in a row
        for col in range(5):
            print("*", end="")
        # new line
        print("\n")

       


def mult_table():
   for row in range(1,11):
      for col in range(1,11):
         print(row * col, end="\t")
      print("\n")

mult_table()

def mult_table_lists():
    mult_table = []
    for row in range(1,11):
        mult_table_row = []
        for col in range(1,11):
            mult_table_row.append(row * col)
        mult_table.append(mult_table_row)
    return mult_table  

def print_2d_array(two_d_array):
    for row in two_d_array:
        for col in row:
            print(col, end="\t")
        print("\n")