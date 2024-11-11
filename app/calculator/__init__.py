from app.logger import setup_logger
import logging
from app.calculation import Calculation
from app.history_manager import History
import os
from decimal import Decimal

class Calculator:
    """ manages repl and uses other all other classes to function"""
    history = History()
    command_list = [
        "help",
        "history",
        "clear",
        "undo",
        "redo",
        "save",
        "load",
        "add",
        "subtract",
        "multiply",
        "divide"
    ]

    def __init__(self):
        #TODO: configure settings from env vars
        pass

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
    
    def list_commands(self)->None:
        for command in self.command_list:
            print(command)
    def show_history(self)->None:
        command_list = self.history.to_list()
        for command in command_list:
            print(f"{command[0]} {command[1]} {command[2]}")
    def undo(self):
        print("undo")
    def redo(self):
        print("redo")
    
def calculator_repl():
    try:
        # start calculator
        setup_logger()
        calculator = Calculator()
        logging.info("started calculator")
        print("Calculator started. Type 'help' for commands.\n")
        # map commands to functions
        """command line interface for calculator"""
        command_map = {
            "help": calculator.list_commands,
            "history": calculator.show_history,
            "clear": calculator.history.clear,
            "undo": calculator.undo,
            "redo": calculator.redo,
            "save": calculator.history.save_history,
            "load": calculator.history.load_history,
        }
        
        while True:
            print("Type in a command: ", end="")
            # get input
            split_input = []
            split_input = input().lower().strip().split()
            command = split_input[0]
            logging.info(f"user typed in command {command}")
            
            # non calculation commands
            if command == "exit":
                logging.info("Exiting program.")
                calculator.history.save_history()
                exit(0)
            try:
                command_map[command]()
                continue
            except:
                pass
            # calculation commands
            try:
                a = split_input[1]
                b = split_input[2]
            except IndexError:
                print("Operation Failed: missing operand(s)")
                logging.info("Operation Failed: missing operand(s)")
                continue
            try:
                

                print(calculator.perform_operation(command, a, b))
                continue
            except Exception as e:
                logging.error(f"failed to execute calculation {e}")
    except Exception as e:
        print(f"Fatal error:{e} \nQuitting.")
        logging.error(f"Fatal error:{e} in REPL")