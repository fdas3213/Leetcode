class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return s
        
        char_freq = defaultdict(int)
        for ch in s:
            char_freq[ch] += 1
        
        count = 0
        # if len(s)%2==0, then those odd-count characters must only have frequency of 1. Example: aaabbccc -> 3 appeared twice, not valid. aaabb -> baaab, 3 appeared once, valid.
        for k,v in char_freq.items():
            if v%2!=0:
                count += 1
            if count > 1:
                return False
    
        return True
        
            
        