class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ans = []
        visited = set()
        minHeap = []
        visited.add((0,0))
        heappush(minHeap, (nums1[0]+nums2[0], 0, 0))
        
        while len(ans)<k and minHeap:
            preSum, p1, p2 = heappop(minHeap)
            ans.append([nums1[p1], nums2[p2]])
            
            if p1+1<len(nums1) and (p1+1, p2) not in visited:
                heappush(minHeap, (nums1[p1+1]+nums2[p2], p1+1, p2))
                visited.add((p1+1, p2))
            
            if p2+1<len(nums2) and (p1, p2+1) not in visited:
                heappush(minHeap, (nums1[p1]+nums2[p2+1], p1, p2+1))
                visited.add((p1, p2+1))
        
        return ans
        
        