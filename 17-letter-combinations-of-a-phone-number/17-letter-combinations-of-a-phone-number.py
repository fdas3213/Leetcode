class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #2. backtrack
        res = []
        if not digits:
            return res
        
        self.digit_map = {"1":"", "2":"abc","3":"def","4":"ghi",
                    "5":"jkl","6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}
        
        def backtrack(start: int, cur: str):
            if start==len(digits):
                res.append(cur)
                return
            
            for i in range(start, len(digits)):
                #to avoid cases like start=0, i=1, so "d" or "e" or "f" is added to the result list
                if i > start:
                    continue
                digit = digits[i]
                for letter in self.digit_map[digit]:
                    backtrack(i+1, cur+letter)
        
        backtrack(0, "")
        
        return res
                