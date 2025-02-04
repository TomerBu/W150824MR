"""
יש לקלוט סכום של חשבון במסעדה.
יש לקלוט אחוז טיפ שרוצים להשאיר.
יש לקלוט את כמות הסועדים.
הדפיסו כמה כל אחד צריך לשלם.
הדפיסו כמה הסכום כולל הטיפ.
הדפיסו את סכום הטיפ שיש להשאיר.
"""
# inputs:
bill = float(input("Enter the bill amount: "))
tip_percent = int(input("Enter the tip percentage: "))
diners = int(input("Enter the number of diners: "))

# calculations:
tip_amount = bill * tip_percent / 100
total = bill + tip_amount
total_per_person = total / diners

# outputs:
print(f"Each person should pay: {total_per_person:.2f}💲")
print(f"Total: {total}💲")
print(f"Tip: {tip_amount}💲")
