from threading import Thread

from src.lru_cache import LRUCache


def test_lru_cache_with_capacity_limit_with_two_threads():
    cache_obj = LRUCache(capacity=1)
    thread1 = Thread(name="thread1", target=set_data, kwargs=dict(cache_obj=cache_obj, key="a", value=1))
    thread2 = Thread(name="thread2", target=set_data, kwargs=dict(cache_obj=cache_obj, key="b", value=2))

    def set_data(key):
        cache_obj.put(key=key, value=key)
        return True

    thread1 = Thread(name="thread1", target=set_data, kwargs=dict(key="a"))
    thread2 = Thread(name="thread2", target=set_data, kwargs=dict(key="b"))
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    assert len(cache_obj) == 1
