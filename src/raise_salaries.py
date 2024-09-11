from copy import deepcopy

def raise_salaries(employees, percentage):
    if not employees:
        return []
    
    employees_copy = deepcopy(employees)
    for employee in employees_copy:
        employee["salary"] += (employee["salary"] * (percentage / 100))
    return employees_copy