class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        
        p1, p2 = 0, 0
        l1, l2 = len(firstList), len(secondList)

        while p1<l1 and p2<l2:
            interval_1 = firstList[p1]
            interval_2 = secondList[p2]
            
            #two intervals intersect iff a[0]<=b[1] and b[0]<=a[1]
            if interval_1[0]<=interval_2[1] and interval_2[0]<=interval_1[1]:
                start = max(interval_1[0], interval_2[0])
                end = min(interval_1[1], interval_2[1])
                ans.append([start, end])
            
            #increment first interval if a[end]<b[end], vice versa
            if interval_1[1]<interval_2[1]:
                p1 += 1
            else:
                p2 += 1
        
        return ans
                