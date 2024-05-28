from concurrent.futures import ThreadPoolExecutor

import pytest

from src.domain.ordered_dictionary import OrderedDictionary

DATA_SET_SIZE = 10000


def test_ordered_dictionary():
    ordered_obj = OrderedDictionary()
    assert ordered_obj == []
    ordered_obj.update("a")
    assert ordered_obj == ["a"]
    ordered_obj.update("b")
    assert ordered_obj == ["a", "b"]
    ordered_obj.update("a")
    assert ordered_obj == ["b", "a"]


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


@pytest.mark.timeout(2)
def test_ordered_dictionary_time_complexity_with_large_dataset_with_for_loop():
    ordered_obj = OrderedDictionary()
    for item in range(1, DATA_SET_SIZE + 1):
        ordered_obj.update(item)

    assert len(ordered_obj) == DATA_SET_SIZE


def test_ordered_dictionary_time_complexity_with_large_dataset_with_thread_pool():
    ordered_obj = OrderedDictionary()
    thread_count = 128

    def update_data(item):
        ordered_obj.update(item)

    with ThreadPoolExecutor(max_workers=thread_count) as executor:
        # updating the function with common data
        # executing the set_data with value range from 1 to 10,000
        results = executor.map(update_data, range(1, DATA_SET_SIZE + 1))

    assert len(ordered_obj) == DATA_SET_SIZE
