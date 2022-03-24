class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        def add_bold(s, start, end):
            return '<b>'+s[start:end]+'</b>'
        
        l = len(s)
        intervals = []
        #create an interval
        for i in range(l):
            for j in range(i+1, l+1):
                if s[i:j] in words:
                    intervals.append([i,j])
        if not intervals:
            return s
        
        merged = []
        #merge intervals
        start, prevEnd = 0, intervals[0][1]
        for end in range(1, len(intervals)):
            if intervals[end][0]<=prevEnd:
                prevEnd = max(prevEnd, intervals[end][1])
            else:
                merged.append([intervals[start][0], prevEnd])
                start = end
                prevEnd = intervals[start][1]
        
        # add the last interval
        merged.append([intervals[start][0], prevEnd])
        
        # create output
        # print(merged)
        prev_start = 0
        res = ""
        for interval in merged:
            cur_start, cur_end = interval[0], interval[1]
            prev_end = cur_start
            res += s[prev_start:prev_end]
            res += add_bold(s, cur_start, cur_end)
            
            prev_start = cur_end
        
        res += s[prev_start:l+1]
        
        return res
            
        
        
                
                