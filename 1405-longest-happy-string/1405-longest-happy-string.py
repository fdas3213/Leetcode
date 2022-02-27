class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maxHeap = []
        if a > 0:
            heappush(maxHeap, (-a, 'a'))
        if b > 0:
            heappush(maxHeap, (-b, 'b'))
        if c > 0:
            heappush(maxHeap, (-c, 'c'))
        
        res = ""
        while maxHeap:
            first, first_char = heappop(maxHeap)
            if len(res)>=2 and res[-1]==res[-2]==first_char:
                # if the highest count character appeared twice in a row, then we use the second highest count character
                if not maxHeap:
                    return res
                second, second_char = heappop(maxHeap)
                res += second_char
                second += 1
                if second != 0:
                    heappush(maxHeap, (second, second_char))
                #still need to add the highest count character back
                heappush(maxHeap, (first, first_char))
                continue
            #if that's not the case, then we add the highest count character
            res += first_char
            first += 1
            if first != 0:
                heappush(maxHeap, (first, first_char))
        
        return res