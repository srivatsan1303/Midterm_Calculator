import os
import logging
import pandas as pd

class CalculationHistory:
    def __init__(self):
        storage_path = os.getenv('CALCULATION_HISTORY_PATH')
        self.storage_path = storage_path
        self.record_number = 1
        if not os.path.exists(os.path.dirname(storage_path)):
            os.makedirs(os.path.dirname(storage_path))
            logging.info(f"Storage directory '{os.path.dirname(storage_path)}' created.")

        elif not os.access(os.path.dirname(storage_path), os.W_OK):
            logging.error(f"Storage directory '{os.path.dirname(storage_path)}' cannot be written to.")

    def log_data(self, entries):
        entries_mod = [entry[1:] if len(entry) == 4 else entry for entry in entries]
        entries_with_id = [[self.record_number + idx] + entry for idx, entry in enumerate(entries_mod)]
        self.record_number += len(entries)
        dataset = pd.DataFrame(entries_with_id, columns=['RecordID', 'Operation', 'Operand1', 'Operand2'])
        dataset.to_csv(self.storage_path, index=False)
    
    def fetch_as_list(self):
        loaded_data = pd.read_csv(self.storage_path)
        return loaded_data.values.tolist()
    
    def fetch_as_dataframe(self):
        return pd.read_csv(self.storage_path)
    
    def reset(self):
        empty_dataset = pd.DataFrame([], columns=['RecordID', 'Operation', 'Operand1', 'Operand2'])
        empty_dataset.to_csv(self.storage_path, index=False)
