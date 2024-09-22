from src.get_fragment import get_fragment
import pytest

def test_returns_empty_list_given_empty_list():
    assert get_fragment([]) == []

def test_returns_given_list_if_no_start_or_end_index_provided():
    assert get_fragment([1, 2, 3]) == [1, 2, 3]

def test_returns_fragment_starting_from_given_start_index():
    assert get_fragment([1, 2, 3, 4], 1) == [2, 3, 4]

def test_returns_fragment_ending_at_given_end_index_minus_1():
    assert get_fragment([1, 2, 3, 4], 0, 3) ==  [1, 2, 3]

def test_handles_given_start_and_end_index():
    assert get_fragment([1, 2, 3, 4], 1, 3) == [2, 3]

def test_handles_out_of_range_indexes():
    with pytest.raises(IndexError):
        get_fragment([1, 2, 3, 4], 0, 5) 
    with pytest.raises(IndexError):
        get_fragment([1, 2, 3, 4], 4) 