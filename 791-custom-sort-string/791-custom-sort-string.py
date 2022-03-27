class Solution:
    def customSortString(self, order: str, s: str) -> str:
        charMap = defaultdict(int)
        for index, char in enumerate(order):
            charMap[char] = index
        
        return "".join(sorted(s, key=lambda x: charMap[x]))