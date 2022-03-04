class Node:
    def __init__(self):
        #val is a bag of words 
        self.keyset = set()
        self.pre = None
        self.next = None
    
    def add_key(self, key):
        self.keyset.add(key)
        
    def remove_key(self, key):
        self.keyset.remove(key)
        
    def get_key(self):
        if self.keyset:
            result = self.keyset.pop()
            self.add_key(result)
            return result
        else:
            return None
    
    def is_empty(self):
        return len(self.keyset)==0
    
class AllOne:

    def __init__(self):
        #{1: N(["a", "b"]), 3:N(["abc", "def"])}
        self.node_freq = defaultdict(Node)
        #{"a":1, "b":1,"abc":3, "def":3}
        self.key_count = defaultdict(int)
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.pre = self.head
        # self.node_freq[0] = self.head
    
    def _insert_after(self, node):
        newnode = Node()
        temp = node.next
        newnode.next, temp.pre = temp, newnode
        newnode.pre, node.next = node, newnode
        return newnode
    
    def _insert_before(self, node):
        return self._insert_after(node.pre)
    
    def _insert(self, key):
        if 1 not in self.node_freq:
            newnode = self._insert_after(self.head)
            newnode.add_key(key)
            self.node_freq[1] = newnode
        else:
            node = self.node_freq[1]
            node.add_key(key)
            self.node_freq[1] = node
        self.key_count[key] = 1
    
    def _remove(self, node):
        prev = node.pre
        n = node.next
        prev.next = n
        n.pre = prev
    
    def _update(self, key, operation):
        count = self.key_count[key]
        newCount = count+1 if operation=='inc' else count-1
        # this is the node before update
        prevNode = self.node_freq[count]
        prevNode.remove_key(key)
        
        if newCount not in self.node_freq:
            self.node_freq[newCount] = self._insert_after(prevNode) if operation=='inc' else self._insert_before(prevNode)
            self.node_freq[newCount].add_key(key)
        else:
            node = self.node_freq[newCount]
            node.add_key(key)
            self.node_freq[newCount] = node
        
        if prevNode.is_empty():
            self._remove(prevNode)
            del self.node_freq[count]
        else:
            self.node_freq[count] = prevNode
                
        self.key_count[key] = newCount

    def inc(self, key: str) -> None:
        if key not in self.key_count:
            self._insert(key)
        else:
            self._update(key, 'inc')

    def dec(self, key: str) -> None:
        # remove the key from key_count if its frequency is 0
        count = self.key_count[key]
        newCount = count-1
        if newCount==0:
            del self.key_count[key]
            prevNode = self.node_freq[count]
            prevNode.remove_key(key)
            if prevNode.is_empty():
                self._remove(prevNode)
                del self.node_freq[count]
        else:
            self._update(key, 'dec')

    def getMaxKey(self) -> str:
        if not self.key_count:
            return ""
        return self.tail.pre.get_key()

    def getMinKey(self) -> str:
        if not self.key_count:
            return ""
        return self.head.next.get_key()