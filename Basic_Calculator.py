# Simple Calculator in Python

# Function for addition
def add(x, y):
    return x + y

# Function for subtraction
def subtract(x, y):
    return x - y

# Function for multiplication
def multiply(x, y):
    return x * y

# Function for division
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y

# Function to display the menu
def menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

# Main function
def calculator():
    while True:
        menu()
        try:
            choice = input("Enter choice (1/2/3/4/5): ")

            # Exit condition
            if choice == '5':
                print("Exiting the calculator. Goodbye!")
                break

            # Input validation
            if choice in ['1', '2', '3', '4']:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    print(f"{num1} / {num2} = {divide(num1, num2)}")
            else:
                print("Invalid Input! Please select a valid operation.")
        except ValueError:
            print("Invalid input! Please enter numeric values.")

# Run the calculator
if __name__ == "__main__":
    calculator()
