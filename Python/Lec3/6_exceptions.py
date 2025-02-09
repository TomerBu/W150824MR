# # Basic try/except block
# try:
#     x = 1 / 0 # This will raise a ZeroDivisionError
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# # Catching multiple exceptions
# try:
#     num = int(input("Enter a number: ")) #value error if not a number
#     result = 10 / num # ZeroDivisionError if num is 0
# except ValueError:
#     print("You must enter a number.")
# except ZeroDivisionError:
#     print("You can't divide by zero!")

# # Catching multiple exceptions with a single block
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except (ValueError, ZeroDivisionError):
#     print("Invalid input.")


# try:
#     num = int(input("Enter a number: "))
# except ValueError as e:
#     print(f"That's not a number! ")
#     print(e) # prints the error message
    


# # Catching all exceptions:
# try:
#     num = int(input("Enter a number: "))
#     result = 10 / num
# except ValueError:
#     print("Value error - You must enter a number.")
# except ZeroDivisionError:
#     print("ZeroDivisionError - You can't divide by zero.")
# except Exception as e:
#     print("Something went wrong.")
#     print(e)
# finally:
#     print("This will always execute.") 



# Raising exceptions

def draw_square(length):
    if length <= 0:
        raise ValueError("Length must be greater than 0.")
    for _ in range(length):
        print("*" * length)

draw_square(-5)