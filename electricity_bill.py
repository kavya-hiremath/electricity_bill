# Electricity Bill Calculator
RATE_PER_UNIT = 5  # ₹5 per unit

def calculate_bill(units):
    return units * RATE_PER_UNIT

try:
    units = float(input("Enter number of units consumed: "))
    bill_amount = calculate_bill(units)
    print(f"Electricity Bill")
    print(f"Units Consumed: {units}")
    print(f"Rate per Unit: ₹{RATE_PER_UNIT}")
    print(f"Total Bill: ₹{bill_amount}")
except ValueError:
    print("Please enter a valid number of units.")
