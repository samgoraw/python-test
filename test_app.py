import pytest
from app import add_numbers,sub_numbers

def test_add_numbers():
    assert add_numbers(2,3) == 5
    assert add_numbers(-1,1) == 0
    assert add_numbers(2,8) == 10
    assert add_numbers(5,0) == 5

def test_sub_numbers():
    assert sub_numbers(3,3) == 0
    assert sub_numbers(1,1) == 0
    assert sub_numbers(8,2) == 6
    assert sub_numbers(9,9) == 18
