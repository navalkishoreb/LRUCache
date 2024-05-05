from typing import Optional, Any, Hashable

from src.ordered_list import OrderedList


class CacheOverFlow(Exception):
    pass


class LRUCache:

    def __init__(self, capacity: int):
        self.__data = dict()
        self.__capacity = capacity
        self.__order = OrderedList()

    def get(self, key: Hashable) -> Optional[Any]:
        value = self.__data[key]
        self.__order.update(key=key)
        return value

    def __is_cache_out_of_capacity__(self) -> bool:
        return len(self.__data) >= self.__capacity

    def __does_key_exists__(self, key: Hashable) -> bool:
        return key in self.__data

    def __does_key_not_exists__(self, key: Hashable) -> bool:
        return not self.__does_key_exists__(key=key)

    def put(self, key: Hashable, value: Any) -> None:
        if self.__is_cache_out_of_capacity__() and self.__does_key_not_exists__(key=key):
            self.__evict__()
        self.__data[key] = value
        self.__order.update(key)

    def __evict__(self):
        last_element = self.__order.last_element()
        del self.__data[last_element]
        self.__order.remove_last_element()

    def __eq__(self, other):
        if isinstance(other, dict):
            return self.__data == other
        else:
            return False
