# The knows API is already defined for you.
# return a bool, whether a knows b
# def knows(a: int, b: int) -> bool:

class Solution:
    def findCelebrity(self, n: int) -> int:
        """
        Build a graph O(N^2), then check if there's a node that has indegree of n-1,
        and outerdegree of 0
        """
        candidate = 0
        
        for i in range(1, n):
            #if candidate knows another person, then candidate must not be the celebrity, 
            #if the candidate does not know the other person, then the other person must not be the celebrity
            if knows(candidate, i):
                candidate = i
        
        #now we have a candidate, but we still need to know whether everyone knows him, which is not
        #checked in the first call
        for j in range(n):
            if j == candidate:
                continue
            if knows(candidate, j) or not knows(j, candidate):
                return -1
        
        return candidate
            