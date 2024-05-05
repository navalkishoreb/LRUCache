from typing import Optional, Any, Hashable


class LRUCache:

    def __init__(self):
        self.__data = dict()

    def get(self, key: Hashable) -> Optional[Any]:
        value = self.__data[key]
        return value

    def put(self, key: Hashable, value: Any) -> None:
        self.__data[key] = value
