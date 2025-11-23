def add(x, y):
    """Adds two numbers."""
    return x + y

def subtract(x, y):
    """Subtracts two numbers."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers."""
    return x * y

def divide(x, y):
    """Divides two numbers. Handles division by zero."""
    if y == 0:
        return "Error! Cannot divide by zero."
    return x / y

def calculator():
    """Main calculator function."""
    print("Welcome to the Simple Python Calculator!")
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    print("-" * 30)

    while True:
        # Take input from the user
        choice = input("Enter choice (1/2/3/4/5): ")

        # Check if choice is one of the available options
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input. Please enter numbers only.")
                continue

            if choice == '1':
                print(f"{num1} + {num2} = {add(num1, num2)}")

            elif choice == '2':
                print(f"{num1} - {num2} = {subtract(num1, num2)}")

            elif choice == '3':
                print(f"{num1} * {num2} = {multiply(num1, num2)}")

            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")

            print("-" * 30)
            
        elif choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        
        else:
            print("Invalid Input. Please enter a valid option (1, 2, 3, 4, or 5).")

# Run the calculator
if __name__ == "__main__":
    calculator()


