import sys
from app.commands import Command
from app.history import CalculationHistory
import logging

class RemoveHistoryCommand(Command):
    def execute(self):
        history_manager = CalculationHistory()
        history_data_frame = history_manager.fetch_as_dataframe()
        try:
            record_id_to_remove = int(input('Enter the ID of the record to delete: '))
            filtered_data_frame = history_data_frame[history_data_frame['RecordID'] != record_id_to_remove]
            history_manager.log_data(filtered_data_frame.values.tolist())
            logging.info(f'Operation history record with ID {record_id_to_remove} has been deleted.')
            print('Operation history of calculator after deletion:\n', history_manager.fetch_as_dataframe().to_string(index=False))
        except ValueError:
            print("Invalid input. Please enter a valid record ID.")
        except Exception as e:
            logging.error(f'An error occurred while deleting the record: {e}')
            print("An error occurred. Could not delete the record.")
