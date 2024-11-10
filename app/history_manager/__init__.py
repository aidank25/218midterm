import logging
from app.calculation import Calculation
from app.env_vars import EnvVars
import pandas as pd
from pandas import DataFrame
import os
from dotenv import load_dotenv

class History():
    file_path: str
    max_entries: int
    calculations = []

    def __init__(self):
        envs = EnvVars()
        self.file_path = envs.get_environment_variable("HIST_PATH")
        self.max_entries = int(envs.get_environment_variable("HIST_MAX"))
        pass
    
    def add_calculation(self, new_calculation: Calculation):
        """append a new calculation to calculations"""
        self.calculations.append(new_calculation)
        logging.info(f"added {new_calculation} to history")
        if(len(self.calculations) > self.max_entries):
            self.calculations.pop()
    
    def to_list(self):
        listList = []
        for c in self.calculations:
            listList.append([c.operation, c.a, c.b, c.result])
        return listList

    def to_csv(self):
        """convert list of calculation objects to csv"""
        data_frame = pd.DataFrame(self.to_list(), columns=["operation","a","b","result"])
        return data_frame.to_csv(self.file_path,index=False)
    
    
    def serialize(self):
        # TODO: use absolute path
        try:
            # create the directory if it doesnt exist
            os.makedirs(self.file_path, exist_ok=True)
            logging.info(f"created directory: {self.file_path}")
        except Exception as e:
            logging.error(f"directory: {file_path}, error: {e}")
    
# except Exception as e