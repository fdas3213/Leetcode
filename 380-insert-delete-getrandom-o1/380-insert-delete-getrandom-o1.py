class RandomizedSet:

    def __init__(self):
        # val map to the position it gets added to the hashmap
        self.valMap = defaultdict(int)
        # position map to val
        self.posMap = defaultdict(int)
        self.count = 0
        
    def insert(self, val: int) -> bool:
        if val in self.valMap:
            return False
        self.valMap[val] = self.count
        self.posMap[self.count] = val
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.valMap:
            return False
        pos = self.valMap[val]
        del self.valMap[val]
        del self.posMap[pos]
        
        self.count -= 1
        if not self.posMap:
            return True
        
        last_element = self.posMap[self.count]
        self.posMap[pos] = last_element
        self.valMap[last_element] = pos
        
        
        return True

    def getRandom(self) -> int:
        pos = random.randint(0, self.count-1)
        return self.posMap[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()