from collections import OrderedDict


class OrderedDictionary:

    def __init__(self):
        # 'Dictionary that remembers insertion order'
        self.order_dict = OrderedDict()
        # self.lock = RLock()

    def update(self, key):
        return self.__update__(key=key)
        # with self.lock:
        #     self.__update__(key=key)

    def __update__(self, key):
        # Setting a new item creates a new link at the end of the linked list,
        # and the inherited dictionary is updated with the new key/value pair.
        if key in self.order_dict:
            self.order_dict.move_to_end(key=key)
        else:
            self.order_dict[key] = key

    def remove_last_element(self):
        return self.__remove_last_element__()
        # with self.lock:
        #     return self.__remove_last_element__()

    def __remove_last_element__(self):
        if not self.order_dict:
            return None
        # Pairs are returned in LIFO order if last is true or FIFO order if false.
        key, value = self.order_dict.popitem(last=False)
        return key

    def __eq__(self, other):
        if isinstance(other, list):
            return list(self.order_dict) == other
        return False

    def __repr__(self):
        return str(list(self.order_dict))

    def __len__(self):
        return len(self.order_dict)
