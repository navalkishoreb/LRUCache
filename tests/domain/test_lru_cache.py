from src.domain.lru_cache import LRUCache


def test_cache():
    cache_obj = LRUCache(capacity=1)
    cache_obj.put("a", 1)
    value = cache_obj.get("a")
    assert value == 1


def test_cache_out_of_capacity():
    cache_obj = LRUCache(capacity=1)
    cache_obj.put("a", 1)
    cache_obj.put("b", 1)
    assert cache_obj == {"b": 1}


def test_cache_when_same_key_is_inserted():
    cache_obj = LRUCache(capacity=1)
    cache_obj.put("a", 1)
    cache_obj.put("a", 2)
    value = cache_obj.get("a")
    assert value == 2


def test_cache_get_call_when_cache_is_empty():
    cache_obj = LRUCache(capacity=1)
    value = cache_obj.get("a")
    assert value is None
