class Node:
    def __init__(self, val, prev=None, next=None):
        self.val=val
        self.prev=prev
        self.next=next
    
class MaxStack:

    def __init__(self):
        #put top node next to head, and least recent node next to tail
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.cur_max = float("-inf")
        #{1: [N(1)], 5: [N(5), N(5)]}
        self.node_map = defaultdict(list)

    def _remove(self, node):
        pre = node.prev
        pre.next = node.next
        node.next.prev = pre
        
    def push(self, x: int) -> None:
        newnode = Node(x)
        temp = self.head.next
        newnode.next, temp.prev = temp, newnode
        newnode.prev, self.head.next = self.head, newnode
        
        self.node_map[x].append(newnode)
        self.cur_max = max(self.cur_max, x)
        
    def pop(self) -> int:
        node = self.head.next
        v = node.val
        self._remove(node)
        self.node_map[v].pop()
        if not self.node_map[v]:
            del self.node_map[v]
            if self.cur_max == v:
                self.cur_max = max(self.node_map.keys()) if self.node_map else float("-inf")
        
        return node.val

    def top(self) -> int:
        return self.head.next.val

    def peekMax(self) -> int:
        return self.cur_max
        
    def popMax(self) -> int:
        max_node = self.node_map[self.cur_max].pop()
        v = max_node.val
        self._remove(max_node)
        if not self.node_map[v]:
            del self.node_map[v]
        
        #update cur_max
        self.cur_max = max(self.node_map.keys()) if self.node_map else float("-inf")
        
        return v
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()