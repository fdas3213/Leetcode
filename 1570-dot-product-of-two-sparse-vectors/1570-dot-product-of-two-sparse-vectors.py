class SparseVector:
    def __init__(self, nums: List[int]):
        self.numMap = defaultdict(int)
        for index, n in enumerate(nums):
            if n!=0:
                self.numMap[index] = n

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        ans = 0
        # optimization: iterate over the shorter hashmap
        if len(vec.numMap) < len(self.numMap):
            self.numMap, vec.numMap = vec.numMap, self.numMap
        for k in self.numMap:
            if k in vec.numMap:
                ans += self.numMap[k] * vec.numMap[k]
        
        return ans
# Your SparseVector object will be instantiated and called as such:
# v1 = SparseVector(nums1)
# v2 = SparseVector(nums2)
# ans = v1.dotProduct(v2)