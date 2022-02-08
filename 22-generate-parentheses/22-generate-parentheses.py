class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(left:int, right:int, cur: str):
            if left == 0 and right == 0:
                res.append(cur)
                return 
            
            if left > right:
                #this should not happend
                return
            
            if left>0:
                backtrack(left-1, right, cur+"(")
                
            if right>0:
                backtrack(left, right-1, cur+")")
        
        backtrack(n, n, "")
        
        return res
            
            