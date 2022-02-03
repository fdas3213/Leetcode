class Node:
    def __init__(self, key=0, val=0, pre=None, next=None):
        self.key = key
        self.val = val
        self.pre = pre
        self.next = next
    
class LRUCache:

    def __init__(self, capacity: int):
        self.kv_pair = {}
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.capacity = capacity
    
    def add_node_to_tail(self, node: Node) -> None:
        #first move pre and next pointer of the node
        if node.next:
            next_node = node.next
            node.pre.next = next_node
            next_node.pre = node.pre
        
        #then move the node to the front of the tail node
        prev = self.tail.pre
        prev.next = node
        node.pre = prev
        node.next = self.tail
        self.tail.pre = node
        
        
    def get(self, key: int) -> int:
        if key not in self.kv_pair:
            return -1
        node = self.kv_pair[key]
        self.add_node_to_tail(node)
        return node.val
        

    def put(self, key: int, value: int) -> None:
        #This essentially works like a Queue, where we add from tail, and pop from head
            
        #if key does not already exist, we create a new key
        if key not in self.kv_pair:
            node = Node(key, value)
        else:
            node = self.kv_pair[key]
            node.val = value

        self.add_node_to_tail(node)
        
        #add the new node/newly updated node to the dictionary
        self.kv_pair[key] = node

        #when the LRU cache is at full capacity, we evict the key next to head
        if len(self.kv_pair)>self.capacity:
            n = self.head.next
            key_to_evict = n.key
            self.head.next = n.next
            n.next.pre = self.head
            del self.kv_pair[key_to_evict]

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)