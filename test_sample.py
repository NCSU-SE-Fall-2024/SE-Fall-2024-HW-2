import pytest
from hw2_debugging import merge_sort

def test_one():
    arr = [4,78,31,2,5,9]
    assert merge_sort(arr) == [2,4,5,9,31,78]

def test_two():
    arr = [4]
    assert merge_sort(arr) == [4]

def test_three():
    arr = [21,7,43,3,71]
    assert merge_sort(arr) == [3,7,21,43,71]
