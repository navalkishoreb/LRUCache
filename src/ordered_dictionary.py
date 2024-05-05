from collections import OrderedDict


class OrderedDictionary:

    def __init__(self):
        # 'Dictionary that remembers insertion order'
        self.order_dict = OrderedDict()

    def update(self, key):
        self.order_dict[key] = key
        self.order_dict.move_to_end(key=key, last=False)

    def last_element(self):
        key, value = self.order_dict.popitem()
        self.order_dict[key] = value
        return key

    def remove_last_element(self):
        if not self.order_dict:
            return None
        key, value = self.order_dict.popitem()
        return key

    def __eq__(self, other):
        if isinstance(other, list):
            return list(self.order_dict) == other
        return False
