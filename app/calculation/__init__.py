#-------------------#
# Calculation Class #
#-------------------#
from decimal import Decimal
from app.operations import Addition, Subtraction, Multiplication, Division
import datetime
from dataclasses import dataclass, field
import logging

@dataclass
class Calculation:
    # fields
    a: Decimal
    b: Decimal
    operation: str

    result: Decimal = None
    timestamp: datetime.datetime = datetime.datetime.now()

    def __post_init__(self):
        """calculates the result of the calculation after initialization"""
        try:
            self.a = Decimal(self.a)
            self.b = Decimal(self.b)
        except:
            raise(TypeError("operands must be numbers"))
            logging.error("operands must be numbers")
        self.result = self.calculate()
    
    def __str__(self):
        """string representation of a calculation"""
        return f"{self.operation} {self.a}, {self.b} = {self.result}"

    def calculate(self)-> Decimal:
        operations_map = {"add": Addition(), 
                          "subtract": Subtraction(), 
                          "multiply": Multiplication(), 
                          "divide": Division()
        }
        try:
            self.result = operations_map.get(self.operation).execute(self.a, self.b)
            logging.info(f"successfully computed {self}")
            return self.result
        except (ValueError, ArithmeticError):
            raise(ValueError("value/arithmetic error occured"))
            logging.error("value/arithmetic error occurred")
    
        


        