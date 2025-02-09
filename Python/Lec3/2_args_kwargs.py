def cool_print(*words):
    for word in words:
        print("❄️" + word + "❄️")   

cool_print("elsa", 'anna', 'olaf') # ❄️elsa❄️ ❄️anna❄️ ❄️olaf❄️


print()

def my_sum(*numbers):
    return sum(numbers)

def my_min(*numbers):
    return min(numbers)

def my_max(*numbers):
    return max(numbers)

def max_diff(*numbers):
    return max(numbers) - min(numbers)