class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        pairs = {'0':'0',
                '1':'1',
                '6':'9',
                '9':'6',
                '8':'8'}
        
        left, right = 0, len(num)-1
        while left<=right:
            left_c, right_c = num[left], num[right]
            if left_c not in pairs or right_c not in pairs:
                return False
            if pairs[left_c]!=right_c or pairs[right_c]!=left_c:
                return False
            left += 1
            right -= 1
            
        return True