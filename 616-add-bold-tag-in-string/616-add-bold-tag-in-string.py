class Solution:
    def addBoldTag(self, s: str, words: List[str]) -> str:
        
        def add_bold(s, start, end):
            return '<b>'+s[start:end]+'</b>'
        
        l = len(s)
        intervals = []
        #initialize intervals
        # this interval creation takes O(N^2 * len(s) * M) time, where
        # we iterate over 2 loops, compare each word of length `len(s)` with M words in words dict, which is not very efficient
        # for i in range(l):
        #     for j in range(i+1, l+1):
        #         if s[i:j] in words:
        #             intervals.append([i,j])
        
        for word in words:
            index = s.find(word)
            while index!=-1:
                intervals.append([index, index+len(word)])
                index = s.find(word, index+1)
        
        if not intervals:
            return s
        
        #sort the intervals
        intervals = sorted(intervals, key=lambda x:x[0])
        merged = []
        #merge intervals
        start, prevEnd = 0, intervals[0][1]
        for end in range(1, len(intervals)):
            """
            if current interval start < previous interval end, then
            this interval should be merged with the previous one, 
            however, the merged interval end should be the max of two.
            Example: [1,5],[3,6] -> [1,6].
            """
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
            
        
        
                
                