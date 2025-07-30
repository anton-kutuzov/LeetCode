from collections import deque


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.first = Node()
        self.last = Node()
        self.first.next = self.last
        self.last.prev = self.first
        self.cache = {}

    def get(self, key: int) -> int:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            self.add(node)
            return node.value
        return -1

    def remove(self, node: Node):
        prev, next = node.prev, node.next
        node.prev.next = next
        node.next.prev = prev

    def add(self, node: Node):
        prev, next = self.first, self.first.next
        node.prev = prev
        node.next = next
        self.first.next.prev = node
        self.first.next = node


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        node = Node(key, value)
        self.add(node)
        self.cache[key] = node

        if len(self.cache) > self.capacity:
            del self.cache[self.last.prev.key]
            self.remove(self.last.prev)


if __name__ == '__main__':
    lRUCache = LRUCache(2)
    lRUCache.put(1, 1)  # cache is {1=1}
    lRUCache.put(2, 2)  # cache is {1=1, 2=2}
    assert lRUCache.get(1) == 1
    lRUCache.put(3, 3)  # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
    assert lRUCache.get(2) == -1
    lRUCache.put(4, 4)  # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
    assert lRUCache.get(1) == -1
    assert lRUCache.get(3) == 3
    assert lRUCache.get(4) == 4

    lRUCache = LRUCache(2)
    assert lRUCache.get(2) == -1
    lRUCache.put(2, 6)
    assert lRUCache.get(1) == -1
    lRUCache.put(1, 5)
    lRUCache.put(1, 2)
    assert lRUCache.get(1) == 2
    assert lRUCache.get(2) == 6

    lRUCache = LRUCache(2)
    lRUCache.put(2, 1)
    lRUCache.put(1, 1)
    lRUCache.put(2, 3)
    lRUCache.put(4, 1)
    assert lRUCache.get(1) == -1
    assert lRUCache.get(2) == 3
