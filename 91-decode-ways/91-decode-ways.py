class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0 for _ in range(len(s)+1)]
        
        dp[0] = 1
        # 1 way to decode a string of size 1 unless the string is '0'
        dp[1] = 0 if s[0]=='0' else 1
        
        for i in range(2, len(s)+1):
            if s[i-1]!='0':
                #"101" -> [1, 1, 1, 1]
                dp[i] = dp[i-1]
            
            if int(s[i-2:i])>=10 and int(s[i-2:i])<=26:
                dp[i] += dp[i-2]
        
        return dp[-1]