from copy import deepcopy

def update_tasks(person, *tasks):
    if not person:
        return {}
    
    copy_person = deepcopy(person)
    
    for task in tasks:
        copy_person["tasks"].append(task)
    return copy_person