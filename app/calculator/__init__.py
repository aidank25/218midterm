from app.logger import setup_logger
import logging
from app.calculation import Calculation
from app.history_manager import History
import os
from decimal import Decimal

class Calculator:
    """ manages repl and uses other all other classes to function"""
    history = History()

    def perform_operation(self, operation:str, a:Decimal ,b:Decimal)->Decimal:
        #TODO: set memento
        # set calculation
        calculation = Calculation(a,b,operation)
        # set history
        self.history.add_calculation(calculation)
        # log
        logging.info(f"calculator calculated {calculation}")
        # return result
        return calculation.result