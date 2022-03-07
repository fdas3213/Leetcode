class RandomizedSet:

    def __init__(self):
        # val map to the position it gets added to the hashmap
        self.randomSet = defaultdict(int)
        # position map to val
        self.valMap = defaultdict(int)
        self.count = 0
        
    def insert(self, val: int) -> bool:
        if val in self.randomSet:
            return False
        self.randomSet[val] = self.count
        self.valMap[self.count] = val
        self.count += 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.randomSet:
            return False
        pos = self.randomSet[val]
        del self.randomSet[val]
        del self.valMap[pos]
        
        self.count -= 1
        if not self.valMap:
            return True
        
        last_element = self.valMap[self.count]
        self.valMap[pos] = last_element
        self.randomSet[last_element] = pos
        
        
        return True

    def getRandom(self) -> int:
        pos = random.randint(0, self.count-1)
        return self.valMap[pos]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()