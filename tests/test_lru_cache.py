import pytest

from src.lru_cache import LRUCache, CacheOverFlow


def test_cache():
    cache_obj = LRUCache(capacity=1)
    cache_obj.put("a", 1)
    value = cache_obj.get("a")
    assert value == 1


def test_cache_out_of_capacity():
    with pytest.raises(CacheOverFlow):
        cache_obj = LRUCache(capacity=1)
        cache_obj.put("a", 1)
        cache_obj.put("b", 1)


def test_cache_when_same_key_is_inserted():
    cache_obj = LRUCache(capacity=1)
    cache_obj.put("a", 1)
    cache_obj.put("a", 2)
    value = cache_obj.get("a")
    assert value == 2
