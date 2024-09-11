from src.raise_salaries import raise_salaries

"""
This function should take as its arguments:

A list of dictionaries representing a group of employees.
A number representing a percentage increase.
Each employee in the list will be represented as an dictionary with a name and 
a salary property.

It should return a new list of employees with their salary now increased by the given 
percentage increase. The new salaries should be rounded up to the nearest integer. 
None of the original employee dictionaries should be mutated.
"""

def test_returns_empty_list_given_empty_list():
    assert raise_salaries([], 10) == []

def test_returns_updated_salary_given_one_employee():
    test_employees =  [{"name": "Cat", "salary": 3000}]
    test_percentage = 10
    expected = [{"name": "Cat", "salary": 3300}]
    assert raise_salaries(test_employees, test_percentage) == expected

def test_returns_updated_salaries_given_multiple_employees():
    test_employees = [
        { "name": "Cat", "salary": 3000 },
        { "name": "Alex", "salary": 2000 },
        { "name": "Danika", "salary": 4500 },
    ]
    test_percentage = 10
    expected = [
        { "name": "Cat", "salary": 3300 },
        { "name": "Alex", "salary": 2200 }, 
        { "name": "Danika", "salary": 4950 }
    ]
    assert raise_salaries(test_employees, test_percentage) ==  expected

def test_input_is_unchanged():
    test_employees = [
        { "name": "Cat", "salary": 3000 },
        { "name": "Alex", "salary": 2000 },
        { "name": "Danika", "salary": 4500 },
    ]
    test_percentage = 10
    copy_test_employees = [
        { "name": "Cat", "salary": 3000 },
        { "name": "Alex", "salary": 2000 },
        { "name": "Danika", "salary": 4500 },
    ]
    raise_salaries(test_employees, test_percentage)
    assert test_employees == copy_test_employees