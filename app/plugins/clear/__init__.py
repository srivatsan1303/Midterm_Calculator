import sys
from app.commands import Command
from app.history import CalculationHistory
import logging

class ResetHistoryCommand(Command):
    def execute(self):
        history_manager = CalculationHistory()
        history_manager.reset()
        logging.info('Operation history of calculator has been reset.')
