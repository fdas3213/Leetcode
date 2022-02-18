class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []
        n = len(s)
        used = [False for _ in range(n)]
        
        def backtrack(curIp: List[int], pos:int):
            #terminal condition: when we reached the last element and there're four valid numbers in the ip list, then we add it to the solution
            if len(curIp) == 4 and pos==n:
                ip = '.'.join(curIp)
                res.append(ip)
            elif len(curIp)==4:
                return
            
            for i in range(pos, n):
                curr = s[pos:i+1]
                curr_val = int(curr)
                """
                constraints
                1: cannot have leading zeros
                2: number should be within [0,255]
                """
                if len(curr)>1 and curr[0]=='0':
                    return
                if curr_val>255:
                    return
                if curr_val>=0 and curr_val<=255:
                    curIp.append(curr)
                    backtrack(curIp, i+1, )
                    curIp.pop()
                
        backtrack([],0)
        
        return res
                
            