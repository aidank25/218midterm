#-----------------#
# Operation Class #
#-----------------#

from abc import ABC, abstractmethod
from decimal import Decimal
from typing import Dict

class Operation(ABC):
    """abstract base class for operations"""

    @abstractmethod
    def execute(self, a: Decimal, b: Decimal)->Decimal: # pragma: no cover
        """abstract method for executing the operation"""
        pass

    def __str__(self) -> str:
        """returns operation name"""
        return self.__class__.__name__
    
class Addition(Operation):
    def execute(self, a, b):
        return a + b
    
class Subtraction(Operation):
    def execute(self, a, b):
        return a - b
    
class Multiplication(Operation):
    def execute(self, a, b):
        return a * b
    
class Division(Operation):
    def execute(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            raise ZeroDivisionError("Division by zero is not allowed")