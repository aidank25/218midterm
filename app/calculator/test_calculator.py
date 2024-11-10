from app.calculator import Calculator, calculator_repl
import pytest
import sys
from io import StringIO

def test_perform_operation():
    calculator = Calculator()
    assert calculator.perform_operation("subtract", 3, 2) == 1

def test_repl_start(capsys):
    calculator_repl()
    captured = capsys.readouterr()
    assert "Calculator started. Type 'help' for commands.\n" in captured.out

def test_help(monkeypatch,capsys):
    monkeypatch.setattr(sys, "stdin", StringIO("help\n"))
    calculator_repl()
    captured = capsys.readouterr()
    help_str = "help\nhistory\nclear\nundo\nredo\nsave\nload\nadd\nsubtract\nmultiply\ndivide"
    assert help_str in captured.out

    