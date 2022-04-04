class Solution:
    def canTransform(self, start: str, end: str) -> bool:
        """
        Replacing XL with LX = move L to the left by one
        Replacing RX with XR = move R to the right by one
        If we remove all the X in both strings, the resulting strings should be the same.
        """
        if start.replace('X','') != end.replace('X', ''):
            return False
        
        #their relative positions should be correct. The index of L in the start string
        #should be >= its corresponding L index in the end string
        Lstart = [i for i,c in enumerate(start) if c=='L']
        Lend = [i for i,c in enumerate(end) if c=='L']
        
        Rstart = [i for i,c in enumerate(start) if c=='R']
        Rend = [i for i,c in enumerate(end) if c=='R']
        
        for s,e in zip(Lstart, Lend):
            if s<e:
                return False
        
        for s,e in zip(Rstart, Rend):
            if s>e:
                return False
        
        return True