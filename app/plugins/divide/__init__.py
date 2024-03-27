import sys
from app.commands import Command
import logging
from app.history import CalculationHistory

class DivideOperation(Command):
    def execute(self, *args, **kwargs):
        try:
            operand_one = float(input("Enter the first number: "))
            operand_two = float(input("Enter the second number: "))
            
            if operand_two == 0:
                raise ZeroDivisionError  # Explicitly raise ZeroDivisionError for division by zero

            result = operand_one / operand_two
            print(f"Result of Division: {result}")
            history_instance = CalculationHistory()
            data = ['divide', operand_one, operand_two, result]  # Include result in the data list
            old_data = history_instance.fetch_as_list()
            old_data.append(data)
            history_instance.log_data(old_data)
            logging.info('Division operation done successfully.')

        except ZeroDivisionError:
            print("Cannot divide by zero.")
            logging.error('Division operation failed due to division by zero.')

        except ValueError:
            print("Please enter valid numbers.")
            logging.info('Division operation failed due to invalid input.')


