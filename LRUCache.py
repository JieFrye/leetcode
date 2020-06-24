import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # dict subclass that remembers the order entries were added
        self.dic = collections.OrderedDict()
        # if not allowed, use queue to keep track FIFO


    def get(self, key: int) -> int:
        if key not in self.dic:
            return -1
        # pop out the element, but put it back to update order
        v = self.dic.pop(key)
        self.dic[key] = v
        return v


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
            self.dic.pop(key)
        if len(self.dic) >= self.cap:
            # FIFO
            self.dic.popitem(last=False)
        self.dic[key] = value


cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
print(cache.get(1)) # returns 1
cache.put(3, 3) # evicts key 2
print(cache.get(2)) # returns -1 (not found)
cache.put(4, 4) # evicts key 1
print(cache.get(1)) # returns -1 (not found)
print(cache.get(3)) # returns 3
print(cache.get(4))  # returns 4

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
