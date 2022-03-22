class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        
        def compute(x):
            return a*x*x+b*x+c
        
        l = len(nums)
        #initialize result
        res = [0 for _ in range(l)]
        
        p = 0 if a<0 else l-1
        left, right = 0, l-1
        
        while left<=right:
            left_n, right_n = nums[left], nums[right]
            left_v, right_v = compute(left_n), compute(right_n)
            if a>=0:
                #in this case, we fill out the result array from the tail
                if left_v>=right_v:
                    res[p] = left_v
                    left += 1
                else:
                    res[p] = right_v
                    right -= 1
                #decrement p since we're filling in bigger values first
                p -= 1
            else:
                #in this case, we fill out the result array from the head
                if left_v<=right_v:
                    res[p] = left_v
                    left += 1
                else:
                    res[p] = right_v
                    right -= 1
                #increment p since we're filling in smaller values first
                p += 1
        
        return res