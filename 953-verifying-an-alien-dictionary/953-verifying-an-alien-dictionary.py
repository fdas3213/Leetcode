class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        #use a hashmap to store the order
        charMap = defaultdict(int)
        for index, char in enumerate(order):
            charMap[char] = index
            
        #iterate over words list for comparison
        for i in range(1, len(words)):
            pre = words[i-1]
            cur = words[i]
            # need to know if the current word is longer than previous word
            longer = True if len(pre)>len(cur) else False
            min_len = min(len(pre), len(cur))
            #compare the first character that differs
            p = 0
            while p<min_len and pre[p]==cur[p]:
                p += 1
                
            if (p<min_len and charMap[pre[p]]>charMap[cur[p]]) or (p==min_len and longer):
                return False
            
        return True
    