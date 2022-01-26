class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        self.timeMin = dict()
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.timeMin:
            self.timeMin[key] = float("inf")
        self.timeMap[key].append((timestamp, value)) 
        self.timeMin[key] = min(self.timeMin[key], timestamp)

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.timeMap:
            return ""
        
        if timestamp < self.timeMin[key]:
            return ""
        
        #binary search to find the maximum timestamp less than the input timestamp
        arr = self.timeMap[key]
        left, right = 0, len(arr)
        
        while left<right:
            mid = left+(right-left)//2
            if arr[mid][0]<=timestamp:
                left = mid+1
            else:
                right=mid
       
        return arr[right-1][1]
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)