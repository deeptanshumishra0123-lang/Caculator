🧮 Simple Python Calculator
This is a basic command-line calculator program written in Python. It allows users to perform fundamental arithmetic operations: addition, subtraction, multiplication, and division.

🚀 Getting Started
Prerequisites
You need to have Python 3 installed on your system to run this script.

Running the Calculator
Save the Code: Save the provided code into a file named temp.py.

Run from Terminal: Open your terminal or command prompt, navigate to the directory where you saved temp.py, and run the following command:

Bash
python temp.py
💻 Usage
Upon running the script, you will be greeted with a menu:

Welcome to the Simple Python Calculator!
Select operation:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Exit
------------------------------
Enter choice (1/2/3/4/5): 
Select an Operation: Enter the corresponding number (1, 2, 3, or 4) for the operation you want to perform.

Enter Numbers: You will be prompted to enter the first and second numbers.

View Result: The result of the operation will be displayed.

Continue or Exit: The calculator will loop, allowing you to perform more calculations. Enter 5 to exit the program.

Key Features
Addition (add): Calculates the sum of two numbers.

Subtraction (subtract): Calculates the difference between two numbers.

Multiplication (multiply): Calculates the product of two numbers.

Division (divide): Calculates the quotient of two numbers. Includes error handling for division by zero.

⚙️ Code Structure
The calculator is organized into several simple functions for clarity and modularity:

Function	Description
add(x, y)	Returns the sum of x and y.
subtract(x, y)	Returns the difference of x and y.
multiply(x, y)	Returns the product of x and y.
divide(x, y)	Returns the quotient of x and y, or an error message if y is 0.
calculator()	The main function that handles the user interface, input, operation selection, and output loop.
The script uses the standard Python entry point if __name__ == "__main__": to ensure the calculator() function is called when the file is executed directly.



