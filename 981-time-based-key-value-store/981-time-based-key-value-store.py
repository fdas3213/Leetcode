class TimeMap:

    def __init__(self):
        self.timeMap = dict()
        self.timeMin = dict()

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMap:
            self.timeMap[key] = dict()
            self.timeMin[key] = float("inf")
            
        self.timeMap[key][timestamp] = self.timeMap[key].get(timestamp, value)
        self.timeMin[key] = min(timestamp, self.timeMin.get(key))
    
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        if timestamp < self.timeMin[key]:
            return ""
        
        while timestamp not in self.timeMap[key]:
            timestamp -= 1
        
        return self.timeMap[key][timestamp]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)