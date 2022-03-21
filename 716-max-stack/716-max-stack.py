class Node:
    def __init__(self, val, pre=None, next=None):
        self.val = val
        self.pre = pre
        self.next = next
        
class MaxStack:

    def __init__(self):
        # add from head, so that elements are also popped from head node
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        self.nodeMap = defaultdict(list)
        self.max = float("-inf")
        
    def push(self, x: int) -> None:
        node = Node(x)
        nxt = self.head.next
        node.next, nxt.pre = nxt, node
        node.pre, self.head.next = self.head, node
        
        self.nodeMap[x].append(node)
        self.max = max(self.max, x)
    
    def _remove(self, node):
        prev = node.pre
        prev.next = node.next
        node.next.pre = prev
        
        nodeVal = node.val
        self.nodeMap[nodeVal].pop()
        if not self.nodeMap[nodeVal]:
            del self.nodeMap[nodeVal]
            if self.max==nodeVal:
                self.max = max(self.nodeMap.keys()) if self.nodeMap else float("-inf")

    def pop(self) -> int:
        node = self.head.next
        self._remove(node)
        return node.val

    def top(self) -> int:
        return self.head.next.val
        
    def peekMax(self) -> int:
        return self.max

    def popMax(self) -> int:
        maxNode = self.nodeMap[self.max][-1]
        self._remove(maxNode)
        
        self.max = max(self.nodeMap.keys()) if self.nodeMap else float("-inf")
        
        return maxNode.val
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()