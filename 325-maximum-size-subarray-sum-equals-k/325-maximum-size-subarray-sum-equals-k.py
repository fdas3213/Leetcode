class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        runningSum = 0
        # {running_sum_up_to_index_i: index}
        sumMap = defaultdict(int)
        sumMap[0] = -1
        ans = 0
        for index, n in enumerate(nums):
            runningSum += n
            if runningSum-k in sumMap:
                ans = max(ans, index-sumMap[runningSum-k])
            
            sumMap[runningSum]=index if runningSum not in sumMap else min(index, sumMap[runningSum])
        return ans