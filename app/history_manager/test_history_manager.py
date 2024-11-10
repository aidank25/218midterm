import pytest
from app.history_manager import History
from app.calculation import Calculation
import os
from app.logger import setup_logger


def test_add_calculation():
    """add calculation to empty history"""
    hist = History()
    calc = Calculation(2,5,"add")
    hist.add_calculation(calc)
    assert hist.calculations.pop() == calc

def test_max_entries():
    """overwrite oldest calculation"""
    hist = History()
    calc = Calculation(2,5,"add")
    for x in range(0,hist.max_entries+1):
        hist.add_calculation(calc)
    
    assert len(hist.calculations) == hist.max_entries

def test_to_list():
    """convert to calculation objects to lists"""
    #build list of calculations
    hist = History()
    for x in range(0,hist.max_entries+1):
        hist.add_calculation(Calculation(2,x,"add"))
    assert hist.to_list()[0][0] == hist.calculations[0].operation
    assert hist.to_list()[0][1] == hist.calculations[0].a
    assert hist.to_list()[0][2] == hist.calculations[0].b
    assert hist.to_list()[0][3] == hist.calculations[0].result

def test_save_history():
    """does hist"""
    hist = History()
    for x in range(0,hist.max_entries+1):
        hist.add_calculation(Calculation(2,x,"add"))
    hist.save_history()
    assert os.path.isfile(f"{hist.directory}/{hist.file_name}")

def test_load_history():
    setup_logger()
    num_calculations = 3
    hist1 = History()
    for x in range(num_calculations):
        hist1.add_calculation(Calculation(2,x,"add"))
    hist1.save_history()
    
    hist2 = History()
    hist2.load_history()
    for x in range(num_calculations):
        assert hist1.calculations[x] == hist2.calculations[x]


    