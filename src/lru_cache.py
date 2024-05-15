from threading import RLock
from typing import Optional, Any, Hashable

from src.ordered_dictionary import OrderedDictionary


class CacheOverFlow(Exception):
    pass


class LRUCache:

    def __init__(self, capacity: int, data: dict = None):
        self.__capacity = capacity
        self.__data = data or dict()
        self.__order = OrderedDictionary()
        self.lock = RLock()

    def get(self, key: Hashable) -> Optional[Any]:
        if key not in self.__data:
            return None
        value = self.__data[key]
        self.__order.update(key=key)
        return value

    def get_and_increment(self, key: Hashable, update_by: int = 1):
        with self.lock:
            value = int(self.get(key=key))
            value += update_by
            self.put(key=key, value=value)

    def __is_cache_out_of_capacity__(self) -> bool:
        return len(self.__data) >= self.__capacity

    def __does_key_exists__(self, key: Hashable) -> bool:
        return key in self.__data

    def __does_key_not_exists__(self, key: Hashable) -> bool:
        return not self.__does_key_exists__(key=key)

    def put(self, key: Hashable, value: Any) -> None:
        with self.lock:
            self.__put__(key=key, value=value)
        # return self.__put__(key=key, value=value)

    def __put__(self, key: Hashable, value: Any) -> None:
        if self.__is_cache_out_of_capacity__() and self.__does_key_not_exists__(key=key):
            self.__evict__()
        self.__data[key] = value
        self.__order.update(key)

    def __evict__(self):
        last_element = self.__order.remove_last_element()
        if last_element in self.__data:
            del self.__data[last_element]

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.__data == other
        else:
            return False

    def __len__(self):
        return len(self.__data)

    def get_data(self):
        return self.__data
