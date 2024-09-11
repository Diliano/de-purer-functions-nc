from src.remove_last_num import remove_last_num

"""
This function should take a list of numbers as its only argument.

This function should return a new list of numbers with the last element removed.
"""

def test_removes_last_number():
    assert remove_last_num([1, 2, 3, 4]) == [1, 2, 3]

def test_input_is_unchanged():
    test_input = [1, 2, 3, 4]
    test_input_copy = [1, 2, 3, 4]
    remove_last_num(test_input)
    assert test_input == test_input_copy
