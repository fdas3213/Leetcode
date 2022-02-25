class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        digit_map = defaultdict(int)
        
        stack = []
        for n in nums2:
            while stack and n>stack[-1]:
                digit_map[stack.pop()] = n
            stack.append(n)
        
        while stack:
            digit_map[stack.pop()] = -1
        
        res = []
        for n in nums1:
            res.append(digit_map[n])
        
        return res