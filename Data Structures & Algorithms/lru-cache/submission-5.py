class Node:
    def __init__(self, key, value):
        self.key, self.value = key, value
        self.next = self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0, 0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
    def insert(self, node:Node):
        prev, nxt = self.right.prev, self.right
        node.next = nxt
        node.prev = prev
        prev.next = node
        nxt.prev = node
    def delete(self, node:Node):
        prev, nxt = node.prev, node.next
        prev.next = nxt
        nxt.prev = prev


        

    def get(self, key: int) -> int:
        if key in self.cache:
            self.delete(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.delete(self.cache[key])
        self.cache[key] = Node(key, value)
        self.insert(self.cache[key])

        if len(self.cache) > self.capacity:
            lru = self.left.next
            self.delete(lru)
            del self.cache[lru.key]
