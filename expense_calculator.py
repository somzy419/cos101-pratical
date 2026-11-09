"""
COS101 Python Practical: Expense Calculator

This is a recreated general-purpose version of the expense calculator.
It asks for expense names and amounts, then displays the total.
"""

expenses = []

print("EXPENSE CALCULATOR")
print("Enter each expense and its amount.")
print("Type 'done' as the expense name when you have finished.\n")

while True:
    name = input("Expense name (or 'done' to finish): ").strip()

    if name.lower() == "done":
        break

    if not name:
        print("Please enter an expense name.")
        continue

    try:
        amount = float(input(f"Amount for {name}: ₦"))

        if amount < 0:
            print("Amount cannot be negative.")
            continue

        expenses.append((name, amount))

    except ValueError:
        print("Please enter a valid number for the amount.")

print("\n----- EXPENSE SUMMARY -----")

if not expenses:
    print("No expenses were entered.")
else:
    total = 0

    for name, amount in expenses:
        print(f"{name}: ₦{amount:,.2f}")
        total += amount

    print("---------------------------")
    print(f"Total expenses: ₦{total:,.2f}")
