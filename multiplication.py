"""
COS101 Python Practical: Multiplication Table

Repeatedly asks the user for a number greater than 1.
Enter E to exit. For a valid number, displays its multiplication
table from 1 to 12 and the sum of the products.
"""

while True:
    user_input = input("Input any number greater than 1 or press E to exit: ").strip()

    if user_input.lower() == "e":
        print("Program ended.")
        break

    try:
        number = int(user_input)

        if number <= 1:
            print("Please enter a number greater than 1.")
            continue

        total = 0
        print(f"\nMultiplication table for {number}")

        for i in range(1, 13):
            product = number * i
            print(f"{number} x {i} = {product}")
            total += product

        print(f"Sum of the products = {total}\n")

    except ValueError:
        print("Invalid input. Enter a whole number or E to exit.")
