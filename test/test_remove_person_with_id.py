from src.remove_person_with_id import remove_person_with_id

def test_returns_empty_list_given_empty_list():
    assert remove_person_with_id([], 2) == []

def test_returns_list_if_no_matching_id():
    test_list = [{ "id": 1, "name": 'Joe' }]
    test_id = 2
    assert remove_person_with_id(test_list, test_id) == [{ "id": 1, "name": 'Joe' }]

def test_returns_list_with_matching_id_removed():
    test_list = [
        { "id": 1, "name": 'Joe' },
        { "id": 2, "name": 'Mick' },
        { "id": 3, "name": 'Chon' },
        { "id": 4, "name": 'Cat' },
        { "id": 5, "name": 'Danika' },
        { "id": 6, "name": 'Kyle' },
        { "id": 7, "name": 'Paul' },
        { "id": 8, "name": 'Simon' },
    ]
    test_id = 4
    expected = [
        { "id": 1, "name": 'Joe' },
        { "id": 2, "name": 'Mick' },
        { "id": 3, "name": 'Chon' },
        { "id": 5, "name": 'Danika' },
        { "id": 6, "name": 'Kyle' },
        { "id": 7, "name": 'Paul'},
        { "id": 8, "name": 'Simon' }
    ]
    assert remove_person_with_id(test_list, test_id) == expected

def test_input_is_unchanged():
    test_list = [
        { "id": 1, "name": 'Joe' },
        { "id": 2, "name": 'Mick' },
        { "id": 3, "name": 'Chon' },
        { "id": 4, "name": 'Cat' },
        { "id": 5, "name": 'Danika' },
        { "id": 6, "name": 'Kyle' },
        { "id": 7, "name": 'Paul' },
        { "id": 8, "name": 'Simon' },
    ]
    copy_test_list = [
        { "id": 1, "name": 'Joe' },
        { "id": 2, "name": 'Mick' },
        { "id": 3, "name": 'Chon' },
        { "id": 4, "name": 'Cat' },
        { "id": 5, "name": 'Danika' },
        { "id": 6, "name": 'Kyle' },
        { "id": 7, "name": 'Paul' },
        { "id": 8, "name": 'Simon' },
    ]
    test_id = 4
    remove_person_with_id(test_list, test_id)
    assert test_list == copy_test_list