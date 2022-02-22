class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s)<=1:
            return s
        s = s.strip()
        queue = deque()
        res = []
        #return " ".join(s.split()[::-1])
        temp = ""
        for c in s[::-1]:
            if c != " ":
                queue.appendleft(c)
                continue
            if c==" " and len(queue)==0:
                continue
            while queue:
                temp += queue.popleft()
            res.append(temp)
            temp = ""
        
        while queue:
            temp += queue.popleft()
        res.append(temp)
        
        return " ".join(res)
            