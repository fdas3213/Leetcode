class Solution:
    def maxArea(self, height: List[int]) -> int:
        curmax = 0
        left, right = 0, len(height)-1
        
        while left<=right:
            w = right-left
            h = min(height[left], height[right])
            curmax = max(curmax, w*h)
            
            if height[left]<height[right]:
                left += 1
            else:
                right -= 1
        
        return curmax