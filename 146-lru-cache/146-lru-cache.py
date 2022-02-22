class Node:
    def __init__(self, key, val, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
        
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.key_map = defaultdict(Node)
    
    def _add(self, node):
        prev_node = self.head.next
        self.head.next = node
        node.pre = self.head
        node.next = prev_node
        prev_node.pre = node
    
    def _update(self, node:Node, val:int):
        node.val = val
        node.next.pre = node.pre
        node.pre.next = node.next
        self._add(node)
    
    def _remove(self):
        node = self.tail.pre
        self.tail.pre = node.pre
        node.pre.next = self.tail
        del self.key_map[node.key]
        
    def get(self, key: int) -> int:
        val = -1
        if key in self.key_map:
            curnode = self.key_map[key]
            val = curnode.val
            self._update(curnode, val)
        return val

    def put(self, key: int, value: int) -> None:
        # add the key into the map
        if key in self.key_map:
            node = self.key_map[key]
            self._update(node, value)
        else:
            node = Node(key=key, val=value)
            self.key_map[key] = node
            self._add(node)
            
        # if number of nodes exceed limit, remove the least recently used key
        if len(self.key_map) > self.capacity:
            self._remove()
             


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)