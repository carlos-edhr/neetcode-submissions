class _Node:
    def __init__(self, key: int = 0, val: int = 0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache: Dict[int, _Node] = {}
        self._head = _Node()
        self._tail = _Node()
        self._head.next = self._tail
        self._tail.prev = self._head
    
    def _remove(self, node: _Node) -> None:
        # Unlink node from wherever it is in O(1)
        node.prev.next = node.next
        node.next.prev = node.prev
    
    def _add_to_head(self, node: _Node) -> None:
        # Insert node right after the head => most recently used
        node.next = self._head.next
        node.prev = self._head
        self._head.next.prev = node
        self._head.next = node


    def get(self, key: int) -> int:
        if key not in self._cache:
            return -1
        node = self._cache[key]
        #unlink from current position
        self._remove(node)
        #... and promote to most recent
        self._add_to_head(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            #drop the stale node
            self._remove(self._cache[key])
        node = _Node(key, value)
        self._cache[key] = node
        self._add_to_head(node)
        if len(self._cache) > self._capacity:
            # least recently used
            lru = self._tail.prev
            self._remove(lru)
            #keep map and list in sync
            del self._cache[lru.key]

        

        
