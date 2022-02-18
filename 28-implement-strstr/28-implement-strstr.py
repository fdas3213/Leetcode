class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        if not needle:
            return 0
        
        hl, nl = len(haystack), len(needle)
        pos = 0
        for pos in range(hl-nl+1):
            if haystack[pos]==needle[0] and haystack[pos:pos+nl]==needle:
                return pos
            
        return -1