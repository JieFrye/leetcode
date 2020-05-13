# Use hash map to optimize search dic = {key: Node(key, value)}
# Use double linked list to optimize shift
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.dic = {} # key: Node(key, value)
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        if key in self.dic:
            node = self.dic[key]
            self.DLLremove(node) # shift DLL
            self.DLLadd(node)
            return node.value
        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dic:
        # if key exits, update value
            self.DLLremove(self.dic[key])
        node = Node(key, value)
        self.DLLadd(node) # update DLL
        self.dic[key] = node # update dic
        # check capacity before caching
        if len(self.dic) > self.capacity: # at capacity
            old = self.head.next
            self.DLLremove(old) # remove oldest in DLL
            del self.dic[old.key] # remove oldest in dic

    def DLLadd(self, node):
        a = self.tail.prev
        a.next = node
        node.prev = a
        node.next = self.tail
        self.tail.prev = node

    def DLLremove(self, node):
        a = node.prev
        b = node.next
        a.next = b
        b.prev = a

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
