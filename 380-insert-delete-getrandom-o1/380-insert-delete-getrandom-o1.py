class RandomizedSet:

    def __init__(self):
        #maps the index of the number to the number. 
        #index is the sequence in which the number is added to the RandomizedSet
        self.indexNumMap = defaultdict(int)
        self.numIndexMap = defaultdict(int)
        self.index = 0
        
    def insert(self, val: int) -> bool:
        if val in self.numIndexMap:
            return False
        self.indexNumMap[self.index] = val
        self.numIndexMap[val] = self.index
        self.index += 1
        
        return True

    def remove(self, val: int) -> bool:
        if val not in self.numIndexMap:
            return False
        
        curIdx = self.numIndexMap[val]
        lastVal = self.indexNumMap[self.index-1]
        # put the last element to the index of the removed element
        self.indexNumMap[curIdx] = self.indexNumMap[self.index-1]
        # also update index-to-num mapping
        self.numIndexMap[lastVal] = curIdx
        
        #remove val from num-to-index mapping 
        del self.numIndexMap[val]
        del self.indexNumMap[self.index-1]
    
        # decrement count by 1
        self.index -= 1
        
        return True
        
    def getRandom(self) -> int:
        r = random.randint(0, self.index-1)
        return self.indexNumMap[r]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()