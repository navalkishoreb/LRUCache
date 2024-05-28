import functools
from concurrent.futures import ThreadPoolExecutor

import pytest

from src.domain.lru_cache import LRUCache


def get_and_update(key, cache_obj):
    cache_obj.get_and_increment(key=key)


@pytest.fixture
def distinct_key_setup(data_set_size):
    range_obj = range(1, data_set_size + 1)
    cache_obj = LRUCache(capacity=data_set_size, data={key: 1 for key in range_obj})
    expected = {key: 2 for key in range_obj}
    test_function = functools.partial(get_and_update, cache_obj=cache_obj)
    return cache_obj, range_obj, test_function, expected


@pytest.fixture
def single_key_setup(data_set_size):
    single_key = "a"
    range_obj = [single_key for _ in range(1, data_set_size + 1)]
    cache_obj = LRUCache(capacity=1, data={single_key: 0})
    expected = data_set_size
    test_function = functools.partial(get_and_update, cache_obj=cache_obj)
    return cache_obj, single_key, range_obj, test_function, expected


def test_get_and_update_distinct_key_with_for_loop(distinct_key_setup):
    #  This is easier problem statement
    #  where we are updating individual key
    #  but we want to evaluate time taken
    #  finish this operation in sequential environment

    cache_obj, range_obj, test_function, expected = distinct_key_setup
    for key in range_obj:
        test_function(key=key)

    assert cache_obj.get_data() == expected


def test_get_and_update_distinct_key_with_thread_pool(worker_thread_count, distinct_key_setup):
    #  This is easier problem statement
    #  where we are updating individual key
    #  but we want to evaluate time taken
    #  in multi-threaded environment

    cache_obj, range_obj, test_function, expected = distinct_key_setup

    with ThreadPoolExecutor(max_workers=worker_thread_count) as executor:
        executor.map(test_function, range_obj)

    assert cache_obj.get_data() == expected


def test_get_and_update_same_key_with_for_loop(single_key_setup):
    #  This is easier problem statement
    #  where we are updating individual key
    #  but we want to evaluate time taken
    #  finish this operation in sequential environment

    cache_obj, single_key, range_obj, test_function, expected = single_key_setup
    for key in range_obj:
        test_function(key=key)

    assert cache_obj.get(single_key) == expected
    assert len(cache_obj) == 1


def test_get_and_update_same_key_with_thread_pool(single_key_setup, worker_thread_count):
    #  This is easier problem statement
    #  where we are updating individual key
    #  but we want to evaluate time taken
    #  finish this operation in sequential environment

    cache_obj, single_key, range_obj, test_function, expected = single_key_setup
    with ThreadPoolExecutor(max_workers=worker_thread_count) as executor:
        executor.map(test_function, range_obj)
    assert cache_obj.get(single_key) == expected
    assert len(cache_obj) == 1
