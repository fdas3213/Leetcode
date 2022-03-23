class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        """
        Two pointers
        """
        #edge case
        if len(abbr)>len(word):
            return False
        
        l1, l2 = len(word), len(abbr)
        p1, preSum = 0, 0
        for p2 in range(l2):
            c2 = abbr[p2]
            if c2.isdigit():
                if preSum==0 and c2=='0':
                    # in this case, '0' does not equal any letter, so return False
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
        
        #check that the total length of two words should match
        return p1+preSum==l1 
            