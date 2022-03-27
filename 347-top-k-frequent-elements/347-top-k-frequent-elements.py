class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for v in nums:
            freq[v] = freq.get(v, 0) + 1
        
        buckets = [[] for _ in range(len(nums)+1)]
        res = []
        
        for n,frequency in freq.items():
            buckets[frequency].append(n)
        
        for bucket in buckets[::-1]:
            if len(res)>=k:
                break
            if bucket:
                res += bucket

        return res