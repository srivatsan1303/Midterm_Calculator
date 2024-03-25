import sys
from app.commands import Command
from app.history import CalculationHistory
import logging

class RetrieveHistoryCommand(Command):
    def execute(self):
        history_instance = CalculationHistory()
        operation_history = history_instance.fetch_as_dataframe().to_string(index=False)
        print('Operation history of calculator:\n', operation_history)
        logging.info('Operation history fetched: %s', operation_history)
