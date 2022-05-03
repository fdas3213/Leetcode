class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        numSet = set()
        for n in nums1:
            if n not in numSet:
                numSet.add(n)
        
        res = []
        for n in nums2:
            if n in numSet:
                res.append(n)
                numSet.remove(n)
        
        return res