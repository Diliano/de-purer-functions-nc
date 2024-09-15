from src.clone_dictionary import clone_dictionary

def test_updates_empty_target_dict():
    # Arrange
    test_target_dict = {}
    test_source_dict = {"a": 1, "b": 2, "c": 3}
    expected = {"a": 1, "b": 2, "c": 3}
    # Act
    result = clone_dictionary(test_target_dict, test_source_dict)
    # Assert
    assert result == expected

def test_updates_target_dict_that_has_existing_key_value_pairs():
    # Arrange
    test_target_dict = {"a": 1}
    test_source_dict = {"b": 2, "c": 3}
    expected = {"a": 1, "b": 2, "c": 3}
    # Act
    result = clone_dictionary(test_target_dict, test_source_dict)
    # Assert
    assert result == expected

def test_updates_target_dict_that_has_same_key_as_source():
    # Arrange
    test_target_dict = {"a": "A"}
    test_source_dict = {"a": 1, "b": 2, "c": 3}
    expected = {"a": 1, "b": 2, "c": 3}
    # Act
    result = clone_dictionary(test_target_dict, test_source_dict)
    # Assert
    assert result == expected

def test_target_dict_is_mutated():
    # Arrange
    test_target_dict = {"a": 1}
    test_source_dict = {"b": 2, "c": 3}
    test_copy_target_dict = {"a": 1}
    # Act
    clone_dictionary(test_target_dict, test_source_dict)
    # Assert
    assert test_target_dict != test_copy_target_dict