class Node:
    def __init__(self, val, cnt=0, pre=None, next=None):
        self.val = val
        self.cnt = cnt
        self.pre = pre
        self.next = next
        
class AllOne:

    def __init__(self):
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.pre = self.head
        #{str: node}
        self.keyMap = defaultdict(Node)
        #{cnt: list of strings with the same count}
        self.cntMap = defaultdict(list)
        # self.maxCnt = -1
        # self.minCnt = float("inf")
    
    def _insert(self, key):
        # insert a new key as the node next to the head node
        node = Node(key, 1)
        nxt = self.head.next
        nxt.pre, node.next = node, nxt
        self.head.next, node.pre = node, self.head
        # add the key to cntMap 
        self.cntMap[1].append(key)
        # add the key to keyMap
        self.keyMap[key] = node
        
        
    def _remove(self, node):
        #removes a node from the DList 
        prev, nxt = node.pre, node.next
        prev.next = nxt
        nxt.pre = prev
    
    def inc(self, key: str) -> None:
        if key not in self.keyMap:
            self._insert(key)
        else:
            #increment the count
            prevCnt = self.keyMap[key].cnt
            self.keyMap[key].cnt += 1
            # remove the node from previous count list
            self.cntMap[prevCnt].remove(key)
            if not self.cntMap[prevCnt]:
                del self.cntMap[prevCnt]
            # add the node to new count list
            self.cntMap[prevCnt+1].append(key)
        
        # print("function: inc", self.cntMap)
            
    def dec(self, key: str) -> None:
        # check if the key exists or not
        if key not in self.keyMap:
            return ""
        
        cnt = self.keyMap[key].cnt
        if cnt==1:
            #remove the key from both hashmap
            del self.keyMap[key]
            self.cntMap[cnt].remove(key)
        else:
            # decrement cnt of the node by 1
            self.keyMap[key].cnt -= 1
            # remove from prevCnt list
            self.cntMap[cnt].remove(key)
            # add to newCnt list
            self.cntMap[cnt-1].append(key)
        
        if not self.cntMap[cnt]:
            del self.cntMap[cnt]
        
        # print("function: dec", self.cntMap)

    def getMaxKey(self) -> str:
        if not self.keyMap:
            return ""
        
        maxCnt = max(self.cntMap)
        # print("function: getMax", self.cntMap)
        return self.cntMap[maxCnt][-1]
        
    def getMinKey(self) -> str:
        if not self.keyMap:
            return ""
        minCnt = min(self.cntMap)
        # print("function: getMin", self.cntMap)
        
        return self.cntMap[minCnt][-1]


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()