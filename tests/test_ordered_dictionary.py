import pytest

from src.ordered_dictionary import OrderedDictionary


def test_ordered_dictionary():
    ordered_obj = OrderedDictionary()
    ordered_obj.update("a")
    assert ordered_obj == ["a"]
    ordered_obj.update("b")
    assert ordered_obj == ["b", "a"]
    ordered_obj.update("a")
    assert ordered_obj == ["a", "b"]


def test_ordered_dictionary_last_element():
    ordered_obj = OrderedDictionary()
    ordered_obj.update("a")
    ordered_obj.update("b")
    value = ordered_obj.last_element()
    assert value == "a"


def test_ordered_dictionary_last_element_dictionary_is_empty():
    ordered_obj = OrderedDictionary()
    value = ordered_obj.last_element()
    assert value is None


def test_ordered_dictionary_remove_last_element():
    ordered_obj = OrderedDictionary()
    ordered_obj.update("a")
    ordered_obj.update("b")
    value = ordered_obj.remove_last_element()
    assert value == "a"
    assert ordered_obj == ["b"]


def test_ordered_dictionary_remove_last_element_when_empty():
    ordered_obj = OrderedDictionary()
    value = ordered_obj.remove_last_element()
    assert value is None
    assert ordered_obj == []


@pytest.mark.timeout(1)
def test_ordered_dictionary_time_complexity_with_large_dataset():
    ordered_obj = OrderedDictionary()
    for item in range(2100000):
        ordered_obj.update(item)
