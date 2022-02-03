class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        l = len(hand)
        #if not divisible by groupSize, return False
        if not hand or l%groupSize!=0:
            return False
        
        #use a dictionary to store the count of each card
        count = defaultdict(int)
        for card in hand:
            count[card] += 1
            
        #use a minHeap to find the starting number of each group
        heapify(hand)
        
        for i in range(l//groupSize):
            start = heappop(hand)
            while count[start] == 0:
                #pop again if the number if no longer available
                start = heappop(hand)
            
            for j in range(groupSize):
                count[start] -= 1
                if count[start] < 0:
                    return False
                start += 1
        
        return True