class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Two pointers
        """
        #edge case
        if len(abbr)>len(word):
            return False
        
        l1, l2 = len(word), len(abbr)
        p1, p2 = 0,0
        preSum = 0
        while p1<l1 and p2<l2:
            c2 = abbr[p2]
            if c2.isdigit():
                if preSum==0 and int(c2)==0:
                    return False
                preSum = preSum*10 + int(c2)
            else:
                p1 += preSum
                if p1>=l1:
                    return False
                c1 = word[p1]
                preSum = 0
                # compare only when c2 is a letter
                if c1!=c2:
                    return False
                # increment p1 by 1
                p1 += 1
            p2 += 1
        
        return p1+preSum==l1 and p2==l2
            