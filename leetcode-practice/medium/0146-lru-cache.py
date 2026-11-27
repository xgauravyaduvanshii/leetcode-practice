from collections import OrderedDict


class LRUCache:
    # My thinking: keep the cache in an OrderedDict, most-recently-used at
    # the end. A get moves the key to the end; a put adds or updates it at
    # the end and pops the oldest (first) item when the capacity is passed.
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last=False)
