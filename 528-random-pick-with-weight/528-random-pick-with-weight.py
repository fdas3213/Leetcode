class Solution:

    def __init__(self, w: List[int]):
        self.weights = []
        cursum = 0
        for weight in w:
            cursum += weight
            self.weights.append(cursum)
        self.cumsum = cursum
        
    def pickIndex(self) -> int:
        r = random.randint(1, self.cumsum)
        left, right = 0, len(self.weights)-1
        while left<=right:
            mid = left + (right-left)//2
            if self.weights[mid]==r:
                return mid
            elif self.weights[mid]>r:
                right = mid-1
            else:
                left = mid+1
        
        return left
        

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()