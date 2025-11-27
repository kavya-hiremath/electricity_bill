import sys

RATE_PER_UNIT = 5  # ₹5 per unit

if len(sys.argv) != 2:
    print("Usage: python electricity_bill.py <units>")
    sys.exit(1)

try:
    units = float(sys.argv[1])
    bill_amount = units * RATE_PER_UNIT

    print("----- Electricity Bill -----")
    print(f"Units Consumed: {units}")
    print(f"Rate per Unit: ₹{RATE_PER_UNIT}")
    print(f"Total Bill: ₹{bill_amount}")

except ValueError:
    print("Please enter a valid numeric value.")
