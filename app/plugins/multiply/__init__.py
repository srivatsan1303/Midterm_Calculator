import sys
from app.commands import Command
import logging
from app.history import CalculationHistory

class MultiplyOperation(Command):
    def execute(self, *args, **kwargs):
        """Prompts the user for two numbers, performs multiplication, and prints the result."""
        try:
            operand_one = float(input("Enter the first number: "))
            operand_two = float(input("Enter the second number: "))
            result = operand_one * operand_two
            print(f"Result of Multiplication: {result}")
            history_instance = CalculationHistory()
            data = ['multiply', operand_one, operand_two]
            old_data = history_instance.fetch_as_list()  # Updated data structure to include the operation name and result.
            old_data.append(data)
            history_instance.log_data(old_data)
            logging.info(f'Multiplication operation done successfully')
        except ValueError:
            print("Please enter valid numbers.")
            logging.info(f'Multiplication operation failed')



