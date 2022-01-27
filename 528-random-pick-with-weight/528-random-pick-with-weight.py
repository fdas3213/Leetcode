class Solution:

    def __init__(self, w: List[int]):
        self.cum_sum = 0
        total = 0
        self.cum_weights = []
        
        for weight in w:
            total += weight
            self.cum_weights.append(total)
        
        self.cum_sum = total

    def pickIndex(self) -> int:
        if not self.cum_weights:
            return -1
        
        r = random.randint(1, self.cum_sum)
        
        left, right = 0, len(self.cum_weights)-1
        while left<=right:
            mid = left+(right-left)//2
            if self.cum_weights[mid]==r:
                return mid
            elif r>self.cum_weights[mid]:
                left=mid+1
            else:
                right = mid-1
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()