class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #1. bfs
        res = []
        if not digits:
            return res
        queue = deque([""])
        digit_map = {"1":"", "2":"abc","3":"def","4":"ghi",
                    "5":"jkl","6":"mno","7":"pqrs","8":"tuv", "9":"wxyz"}
        
        for i, digit in enumerate(digits):
            l = len(queue)
            for j in range(l):
                prev = queue.popleft()
                for letter in digit_map[digit]:
                    cur = prev+letter
                    if i<len(digits)-1:
                        queue.append(cur)
                    else:
                        res.append(cur)
        
        return res
                
        
        