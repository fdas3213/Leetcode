class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = []
        if len(s)<10:
            return res
        
        #iterating over the string
        l = len(s)
        dnaMap = defaultdict(int)
        for i in range(l-9):
            cur = s[i:i+10]
            dnaMap[cur] += 1
            if dnaMap[cur]>1 and cur not in res:
                res.append(cur)
        
        return res