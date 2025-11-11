# basic_operations.py
# This program performs basic math operations

# Ask for user input
a = float(input("Enter the first number: "))
b = float(input("Enter the second number: "))

# Perform operations
sum_result = a + b
difference = a - b
product = a * b
quotient = a / b if b != 0 else "Undefined (cannot divide by zero)"

# Display results
print("\nResults:")
print(f"Sum: {sum_result}")
print(f"Difference: {difference}")
print(f"Product: {product}")
print(f"Quotient: {quotient}")
