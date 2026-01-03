print("Welcome to the tip calculator")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10%, 12% or 15%? "))
bill_including_tip = bill * (1 + tip/100)
people = int(input("How many people to split the bill? "))
split = round(bill_including_tip / people, 2)
print(f"Each person should pay: ${split}")

