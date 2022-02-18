class Solution:
    def countArrangement(self, n: int) -> int:
        self.res = 0
        used = [False for _ in range(n+1)]
        
        
        def backtrack(pos:int):
            if pos>n:
                #position reached n implies that numbers from [1,n] are all beautiful arrangements
                self.res += 1
                return
            
            for i in range(1, n+1):
                if not used[i] and (i%pos==0 or pos%i==0):
                    used[i] = True
                    backtrack(pos+1)
                    used[i] = False
        
        backtrack(1)
        
        return self.res