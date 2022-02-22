class Solution:
    def reverseWords(self, s: str) -> str:
        if not s or len(s)<=1:
            return s
        s = s.strip()
        return " ".join(s.split()[::-1])