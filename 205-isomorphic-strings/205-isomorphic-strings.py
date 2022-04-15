class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        charMap = defaultdict(str)
        reverseMap = defaultdict(str)
        for index, (c1, c2) in enumerate(zip(s,t)):
            # c1 is already mapped to another c2
            if c1 in charMap and charMap[c1] != c2:
                return False
            # no two characters can map to the same character -> if c2 exists in a reverse map, and current c1 != reverse_map[c2], also return False
            if c2 in reverseMap and reverseMap[c2] != c1:
                return False
            reverseMap[c2] = c1
            charMap[c1] = c2
        
        return True