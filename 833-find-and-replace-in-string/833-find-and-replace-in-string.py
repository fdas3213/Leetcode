class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        #a dictionary which has {index: target} structure
        indexTargetMap = defaultdict(str)
        #a dictionary which has {index: len(source)} structure
        indexSourceMap = defaultdict(int)
        for index, source, target in zip(indices, sources, targets):
            if s[index:].startswith(source):
                indexTargetMap[index] = target
                indexSourceMap[index] = len(source)
        
        start = 0
        ans = ""
        while start<len(s):
            if start not in indexTargetMap:
                ans += s[start]
                start += 1
            else:
                ans += indexTargetMap[start]
                start += indexSourceMap[start]
                
        return ans