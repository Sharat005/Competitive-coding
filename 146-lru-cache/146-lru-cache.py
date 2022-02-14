from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cacheKey = None
        self.cache = OrderedDict()
        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache.move_to_end(key)
        self.cache[key] = value
        if len(self.cache) > self.capacity:
            self.cache.popitem(last = False)
        # if key in self.cache:
        #     val = self.cache[key]
        #     del self.cache[key]
        #     self.cache[key] = val
        #     self.cache[key] = value
        # if len(self.cache) == self.capacity and key not in self.cache:
        #     self.cacheKey = next(iter(self.cache))
        #     print(self.cacheKey)
        #     del self.cache[self.cacheKey]
    


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)