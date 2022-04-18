class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        srcTgtMap = {}
        indexSrcMap = {}
        
        for i, (index, source, target) in enumerate(zip(indices, sources, targets)):
            if s[index:].startswith(source):
                srcTgtMap[index] = target
                indexSrcMap[index] = i
        
        ans = ""
        start = 0
        print(srcTgtMap)
        while start < len(s):
            if start not in srcTgtMap:
                ans += s[start]
                start += 1
            else:
                ans += srcTgtMap[start]
                prevLen = len(sources[indexSrcMap[start]])
                start += prevLen
        
        return ans