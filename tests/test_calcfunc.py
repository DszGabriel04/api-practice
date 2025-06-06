import pytest
from calcfunc import add, sub, mul, div

# test_calcfunc.py


def test_add_basic():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0
    assert add(0, 0) == 0

def test_add_edge_cases():
    assert add(-1000000, 1000000) == 0
    assert add(999999999, 1) == 1000000000

def test_sub_basic():
    assert sub(5, 3) == 2
    assert sub(0, 0) == 0
    assert sub(-2, -2) == 0

def test_sub_edge_cases():
    assert sub(-1000000, 1000000) == -2000000
    assert sub(1, 999999999) == -999999998

def test_mul_basic():
    assert mul(2, 3) == 6
    assert mul(-1, 1) == -1
    assert mul(0, 100) == 0

def test_mul_edge_cases():
    assert mul(-1000000, 0) == 0
    assert mul(99999, 99999) == 9999800001

def test_div_basic():
    assert div(6, 2) == 3
    assert div(-9, 3) == -3
    assert div(0, 1) == 0

def test_div_edge_cases():
    assert div(1000000, 1) == 1000000
    assert div(-1000000, -1) == 1000000
