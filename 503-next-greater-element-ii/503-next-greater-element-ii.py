class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        digit_map = {}
        max_num = max(nums)
        max_index = -1
        for idx, n in enumerate(nums):
            if n == max_num:
                max_index = idx
        
        n = len(nums)
        stack = []
        for i in range(max_index+1, max_index+1+n, 1):
            cur_index = i%n
            cur_num = nums[cur_index]
            while stack and stack[-1][-1] < cur_num:
                digit_map[stack.pop()] = cur_num
            stack.append((cur_index, cur_num))
        
        while stack:
            digit_map[stack.pop()] = -1
        
        res = [-1]*n
        for i, n in enumerate(nums):
            res[i] = digit_map[(i,n)]
        
        return res
        