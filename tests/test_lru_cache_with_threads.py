from concurrent.futures import ThreadPoolExecutor, as_completed
from threading import Thread

from src.lru_cache import LRUCache


def test_lru_cache_with_capacity_limit_with_two_threads():
    cache_obj = LRUCache(capacity=1)

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


def test_lru_cache_given_capacity_limit_with_two_threads_and_large_number_of_put_operation():
    capacity = 1
    thread_count = 2
    data_set_size = 10000
    cache_obj = LRUCache(capacity=capacity)

    def set_data(key):
        cache_obj.put(key=key, value=key)
        return key

    results = []
    with ThreadPoolExecutor(thread_name_prefix="thread", max_workers=thread_count) as executor:
        # updating the function with common data
        # executing the set_data with value range from 1 to 10,000
        futures = []
        for i in range(1, data_set_size + 1):
            future = executor.submit(set_data, i)
            futures.append(future)

        for future in as_completed(futures):
            try:
                result = future.result()
            except Exception:
                result = False
            results.append(result)
    current_cache_size = len(cache_obj)
    # print(results)
    assert current_cache_size == capacity, f"Cache size should at {capacity} but found {current_cache_size}"
    successful = len([result for result in results if result])
    # print(f"{successful} were successful out of {limit}")
    assert successful == data_set_size, f"Only {successful} put calls were successful out of {data_set_size}"
