from src.update_tasks import update_tasks

def test_returns_empty_dict_given_empty_dict():
    assert update_tasks({}, "read books") == {}

def test_updates_tasks_in_dict_with_new_task():
    # Arrange
    test_person = {"name": "Nara", "tasks": ["feed Scout", "Go to karate"]}
    test_task = "read books"
    expected = {"name": "Nara", "tasks": ["feed Scout", "Go to karate", "read books"]}
    # Act
    result = update_tasks(test_person, test_task)
    # Assert
    assert result == expected

def test_updates_tasks_in_dict_with_multiple_new_tasks():
    # Arrange
    test_person = {
        "name": "Nara",
        "tasks": ["feed Scout", "Go to karate"]
    }
    test_tasks = ("read books", "tidy room")
    expected = {
        "name": "Nara",
        "tasks": ["feed Scout", "Go to karate", "read books", "tidy room"]
    }
    # Act
    result = update_tasks(test_person, *test_tasks)
    # Assert
    assert result == expected

def test_input_dict_is_unchanged():
    # Arrange
    test_person = {
        "name": "Nara",
        "tasks": ["feed Scout", "Go to karate"]
    }
    test_tasks = ("read books", "tidy room")
    test_copy_person = {
        "name": "Nara",
        "tasks": ["feed Scout", "Go to karate"]
    }
    # Act
    update_tasks(test_person, *test_tasks)
    # Assert
    assert test_person == test_copy_person