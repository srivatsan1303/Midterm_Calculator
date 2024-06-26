import sys
from app.commands import Command
import logging
from app.history import CalculationHistory

class SumOperation(Command):
    def execute(self, *args, **kwargs):
        """Prompts the user for two numbers, performs addition, and prints the result."""
        try:
            operand_one = float(input("Enter the first number: "))
            operand_two = float(input("Enter the second number: "))
            result = operand_one + operand_two
            print(f"Result of Addition: {result}")
            history_instance = CalculationHistory()
            data = ['add', operand_one, operand_two]
            old_data = history_instance.fetch_as_list()  # Updated data structure to include the operation name and result.
            old_data.append(data)
            history_instance.log_data(old_data)
            logging.info(f'Addition operation done successfully')
        except ValueError:
            print("Please enter valid numbers.")
            logging.info(f'Addition operation failed')


