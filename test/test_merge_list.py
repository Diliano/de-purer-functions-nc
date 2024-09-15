from src.merge_list import merge_list

def test_returns_empty_list_given_empty_list():
    assert merge_list([]) == []

def test_handles_two_lists_of_same_length_adding_to_flattened_list_in_alternating_order():
    # Arrange
    test_lists = [[1,2], ['a', 'b']]
    expected = [1, "a", 2, "b"]
    # Act
    result = merge_list(test_lists)
    # Assert
    assert result == expected

def test_handles_more_than_two_lists_of_same_length():
    # Arrange
    test_lists = [[1,2], ['a', 'b'], [3, 4]]
    expected = [1, "a", 3, 2, "b", 4]
    # Act
    result = merge_list(test_lists)
    # Assert
    assert result == expected

def test_handles_lists_of_diff_length_by_adding_none_for_missing_vals():
    # Arrange
    test_lists = [[1, 2, 3], ['a', 'b', 'c', 'd']]
    expected = [1, 'a', 2, 'b', 3, 'c', None, 'd']
    # Act
    result = merge_list(test_lists)
    # Assert
    assert result == expected