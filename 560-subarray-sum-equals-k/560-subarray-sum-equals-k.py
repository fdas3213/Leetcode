class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # we use a hashmap to store (cumsum(i), # of occurrences of cumsum(i))
        cumsumMap = defaultdict(int)
        cumsumMap[0] = 1
        runningSum, count = 0,0 
        for n in nums:
            runningSum += n
            #if the difference between current cumulative sum and previous culumative sum is k,
            #then the sum between is k. Example: cumsum[:i]=a, cumsum[:j]=b, a-b=k,
            #then cursum[i:j]=k
            count += cumsumMap.get(runningSum-k, 0)
            cumsumMap[runningSum] += 1
        
        return count