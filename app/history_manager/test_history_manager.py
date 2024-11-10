import pytest
from app.history_manager import History
from app.calculation import Calculation
import os



def test_add_calculation():
    """add calculation to empty history"""
    hist = History()
    calc = Calculation(2,5,"add")
    hist.add_calculation(calc)
    assert hist.calculations.pop() == calc

def test_max_entries():
    """add calculation to empty history"""
    hist = History()
    calc = Calculation(2,5,"add")
    for x in range(0,hist.max_entries+1):
        hist.add_calculation(calc)
    
    assert len(hist.calculations) == hist.max_entries

def test_to_list():
    """convert to list"""
    #build list of calculations
    hist = History()
    for x in range(0,hist.max_entries+1):
        hist.add_calculation(Calculation(2,x,"add"))
    assert hist.to_list()[0][0] == hist.calculations[0].operation
    assert hist.to_list()[0][1] == hist.calculations[0].a
    assert hist.to_list()[0][2] == hist.calculations[0].b
    assert hist.to_list()[0][3] == hist.calculations[0].result

def test_serialize():
    hist = History()
    for x in range(0,hist.max_entries+1):
        hist.add_calculation(Calculation(2,x,"add"))
    hist.serialize()
    assert os.path.isfile(f"{hist.directory}/{hist.file_name}")
    