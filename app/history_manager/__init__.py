import logging
from app.calculation import Calculation
from app.env_vars import EnvVars
import pandas as pd
from pandas import DataFrame
import os
from dotenv import load_dotenv

class History():
    directory: str
    file_name = "history.csv"
    max_entries: int
    calculations = []

    def __init__(self):
        envs = EnvVars()
        self.directory = envs.get_environment_variable("HIST_PATH")
        self.max_entries = int(envs.get_environment_variable("HIST_MAX"))
        pass
    
    def add_calculation(self, new_calculation: Calculation):
        """append a new calculation to calculations"""
        self.calculations.append(new_calculation)
        logging.info(f"added {new_calculation} to history")
        if(len(self.calculations) > self.max_entries):
            self.calculations.pop()
    
    def to_list(self):
        """converts list of calculation objects to list of lists"""
        listList = []
        for c in self.calculations:
            listList.append([c.operation, c.a, c.b, c.result])
        return listList
    
    def serialize(self):
        """convert list of calculation objects to csv and stores it to a file_path/file_ame.csv"""
        # TODO: use absolute path
        file_path = os.path.join(self.directory, self.file_name)
        # create the directory if it doesnt exist
        os.makedirs(self.directory, exist_ok=True)
        # store to csv file
        data_frame = pd.DataFrame(self.to_list(), columns=["operation","a","b","result"])
        data_frame.to_csv(file_path,index=False)
        logging.info(f"stored calculation history at {file_path}")
        