def remove_person_with_id(people, id):
    people_copy = list(people)
    for person in people_copy:
        if person["id"] == id:
            people_copy.remove(person)
    return people_copy