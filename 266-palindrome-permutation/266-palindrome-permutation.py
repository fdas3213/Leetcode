class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        if len(s)<=1:
            return s
        
        char_freq = defaultdict(int)
        count_freq = defaultdict(int)
        for ch in s:
            char_freq[ch] += 1
        
        for k,v in char_freq.items():
            count_freq[v] += 1
       
        # if s%2==0, then those odd-count characters must only have frequency of 1.
        # example: aaabbccc -> 3 appeared twice, not valid. aaabb -> baaab, 3 appeared once, valid.
        odd_freq_total = len(s)
#         for count, freq in count_freq.items():
#             if count%2==0:
#                 odd_freq_total -= count*freq
#         # print(count_freq)
#         if odd_freq_total == 0:
#             return True
        
#         if count_freq[odd_freq_total]!=1:
#             return False
        for count, freq in count_freq.items():
            if count%2!=0 and freq!=1:
                return False
        
        return True
        
            
        