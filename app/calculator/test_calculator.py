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
    help_str = "help\nhistory\nclear\nsave\nload\nadd\nsubtract\nmultiply\ndivide"
    assert help_str in captured.out

def test_exit(monkeypatch,capsys):
    monkeypatch.setattr(sys, "stdin", StringIO("exit\n"))
    with pytest.raises(SystemExit) as e:
        calculator_repl()
    assert e.value.code == 0

def test_calc_commands(monkeypatch,capsys):
    monkeypatch.setattr(sys, "stdin", StringIO("add 4 2\n"))
    calculator_repl()
    captured = capsys.readouterr()
    assert "result: 6" in captured.out