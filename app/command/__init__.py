import logging
from abc import ABC, abstractmethod

class Command:
    """handle user inputted commands"""
    @abstractmethod
    def execute():# pragma: no cover
        pass

class Help(Command):
    def execute():
        pass
class History(Command):
    def execute():
        pass
class Clear(Command):
    def execute():
        pass
class Undo(Command):
    def execute():
        pass
class Redo(Command):
    def execute():
        pass
class Save(Command):
    def execute():
        pass
class Load(Command):
    def execute():
        pass
class Add(Command):
    def execute():
        pass
class Subtract(Command):
    def execute():
        pass
class Multiply(Command):
    def execute():
        pass
class Divide(Command):
    def execute():
        pass