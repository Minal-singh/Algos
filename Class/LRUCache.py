class Node:
    def __init__(self, key=-1, value=-1):
        self.key = key
        self.val = value
        self.next = None
        self.prev = None


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def _deletenode(self, node):
        pre = node.prev
        nxt = node.next
        pre.next = nxt
        nxt.prev = pre

    def _addafterhead(self, node):
        nxt = self.head.next
        self.head.next = node
        node.next = nxt
        nxt.prev = node
        node.prev = self.head

    def get(self, key: int) -> int:
        if key in self.cache:
            val = self.cache[key].val
            self._deletenode(self.cache[key])
            newnode = Node(key, val)
            self.cache[key] = newnode
            self._addafterhead(newnode)
            return val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._deletenode(self.cache[key])
            del self.cache[key]
        if self.capacity == len(self.cache):
            key_ = self.tail.prev.key
            self._deletenode(self.tail.prev)
            del self.cache[key_]
        newnode = Node(key, value)
        self.cache[key] = newnode
        self._addafterhead(newnode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
