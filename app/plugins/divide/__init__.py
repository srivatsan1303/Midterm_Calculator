import sys
from app.commands import Command

class DivideOperation(Command):
    def execute(self, *args, **kwargs):
        """Prompts the user for two numbers, performs division, and prints the result."""
        try:
            operand_one = float(input("Enter the first number: "))
            operand_two = float(input("Enter the second number: "))
            if operand_two == 0:
                print("Error: Division by zero is not allowed.")
                return
            result = operand_one / operand_two
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")


