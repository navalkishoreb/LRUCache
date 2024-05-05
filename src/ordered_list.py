from collections import deque


class OrderedList:

    def __init__(self):
        self.__order_list = deque()

    def update(self, key):
        try:
            # Cannot remove a key when not present
            # this operation is O(n)
            # as it search for the key in whole array
            self.__order_list.remove(key)
        except ValueError:
            pass
        #  this operation is O(1)
        #  appending to front or rear
        self.__order_list.appendleft(key)

    def __eq__(self, other):
        if isinstance(other, list):
            return list(self.__order_list) == other
        return False
