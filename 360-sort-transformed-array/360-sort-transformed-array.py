class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(x,a,b,c):
            return a*x*x + b*x + c
            
        #vertex is -2a/b
        n = len(nums)
        res = [0 for _ in range(n)]
        left, right = 0, n-1
        index = n-1 if a>=0 else 0
        
        while left<=right:
            # we do not need to care about a==0 because in that case the quadratic function becomes a linear line, where min/max must be on either end of the input list
            if a>=0:
                left_v, right_v = quad(nums[left], a, b, c), quad(nums[right],a,b,c)
                if left_v < right_v:
                    res[index] = right_v
                    right -= 1
                else:
                    res[index] = left_v
                    left += 1
                index -= 1
            else:
                left_v, right_v = quad(nums[left], a, b, c), quad(nums[right],a,b,c)
                if left_v < right_v:
                    res[index] = left_v
                    left += 1
                else:
                    res[index] = right_v
                    right -= 1
                index += 1
        
        return res