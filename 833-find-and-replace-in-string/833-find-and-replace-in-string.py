class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ""
        
        strMap = defaultdict(int)
        
        # store the indices whose corresponding is found at s[index]. For example, index=0, source=a, s='abcd', then because source is found at s[0], we add index to the hashmap. The value of the hashmap is just the index of sources/targets, which is later used to replace the substring and retrieve substring length.
        for i, (index, source) in enumerate(zip(indices, sources)):
            if s[index:].startswith(source):
                strMap[index] = i
        
        start = 0
        while start<len(s):
            if start in strMap:
                ans += targets[strMap[start]]
                start += len(sources[strMap[start]])
            else:
                ans += s[start]
                start += 1
        
        return ans