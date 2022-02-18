class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        if not needle:
            return 0
        
        hl, nl = len(haystack), len(needle)
        pos = 0
        while pos<=hl-nl:
            if haystack[pos]==needle[0] and haystack[pos:pos+nl]==needle:
                return pos
            pos += 1
            
        return -1