class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # when the size of the heap becomes greater than k, we pop the minimum element and
        # add it to the result list
        minHeap = []
        # we need this visited set because suppose we're now at (0, 1) and (1,0), then (1,1) will be added
        # twice if we do not use visited set
        visited = set()
        res = []
        l1, l2 = len(nums1), len(nums2)
        heappush(minHeap, (nums1[0]+nums2[0], 0, 0))
        
        while len(res)<k and minHeap:
            curSum, p1, p2 = heappop(minHeap)
            res.append([nums1[p1], nums2[p2]])

            if p1+1<l1 and (p1+1, p2) not in visited:
                heappush(minHeap, (nums1[p1+1]+nums2[p2], p1+1, p2))
                visited.add((p1+1,p2))
                
            if p2+1<l2 and (p1, p2+1) not in visited:
                heappush(minHeap, (nums1[p1]+nums2[p2+1], p1, p2+1))
                visited.add((p1, p2+1))
                
        return res