from src.lru_cache import LRUCache


def test_cache():
    cache_obj = LRUCache()
    cache_obj.put("a", 1)
    value = cache_obj.get("a")
    assert value == 1
