import sys
from app.commands import Command

class SumOperation(Command):
    def execute(self, *args, **kwargs):
        """Prompts the user for two numbers, performs addition, and prints the result."""
        try:
            operand_one = float(input("Enter the first number: "))
            operand_two = float(input("Enter the second number: "))
            result = operand_one + operand_two
            print(f"Result: {result}")
        except ValueError:
            print("Please enter valid numbers.")


