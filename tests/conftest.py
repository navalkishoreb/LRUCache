import pytest

from src.lru_cache import LRUCache


@pytest.fixture
def data_set_size():
    return 10000


@pytest.fixture
def date_set_range(data_set_size):
    return range(1, data_set_size + 1)


@pytest.fixture
def worker_thread_count():
    return 128


@pytest.fixture
def capacity():
    return 1


@pytest.fixture
def cache_obj(capacity):
    return LRUCache(capacity=capacity)
