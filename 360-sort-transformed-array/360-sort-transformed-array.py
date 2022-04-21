class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def calc(x, a, b, c):
            return a*x*x+b*x+c
        
        l = len(nums)
        ans = [0 for _ in range(l)]
        pointer = l-1 if a>=0 else 0
        left, right = 0, l-1
        
        while left<=right:
            left_v = calc(nums[left], a, b, c)
            right_v = calc(nums[right], a, b, c)
            if a>=0:
                if left_v>=right_v:
                    ans[pointer]=left_v
                    left += 1
                else:
                    ans[pointer]=right_v
                    right -= 1
                pointer -= 1
            else:
                if left_v<=right_v:
                    ans[pointer]=left_v
                    left += 1
                else:
                    ans[pointer]=right_v
                    right -= 1
                pointer += 1
            
        return ans