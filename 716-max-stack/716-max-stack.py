class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
    
    def __lt__(self, other):
        self.val < other.val

class MaxStack:

    def __init__(self):
        self.head = Node(float('-inf'))
        self.tail = Node(float('-inf'))
        self.head.next = self.tail
        self.tail.prev = self.head
        self.max_heap = []
        self.node_map = defaultdict(list)
        
    def push(self, x: int) -> None:
        node = Node(x)
        
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev.next = node
        self.tail.prev = node
        
        # the way to customize the heap order is to have each element on the heap to be a tuple, with the first tuple element being one that accepts normal Python comparisons.
        heappush(self.max_heap, (-x, node))
        
        self.node_map[x].append(node)
        

    def pop(self) -> int:
        node = self.tail.prev
        node.prev.next = node.next
        node.next.prev = node.prev
        
        self.node_map[node.val].pop()
        if not self.node_map[node.val]:
            del self.node_map[node.val]
        
        return node.val
        
    def top(self) -> int:
        return self.tail.prev.val

    def peekMax(self) -> int:
        # during the pop(), we didn't remove the element from heap
        # So here is to remove the the poped elements from heap
        while -self.max_heap[0][0] not in self.node_map:
            heappop(self.max_heap)
        return -self.max_heap[0][0]

    def popMax(self) -> int:
        #问题出在pop max把前面的给删了，需要在tuple里面再加一个顺序的index..
        num = self.peekMax()
        max_node = self.node_map[num].pop()
        if not self.node_map[num]:
            del self.node_map[num]
        
        max_node.prev.next = max_node.next
        max_node.next.prev = max_node.prev
        
        return num
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()