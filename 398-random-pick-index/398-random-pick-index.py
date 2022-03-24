class Solution:

    def __init__(self, nums: List[int]):
        self.numMap = defaultdict(list)
        for index, n in enumerate(nums):
            self.numMap[n].append(index)

    def pick(self, target: int) -> int:
        freq = len(self.numMap[target])
        # no need to add this case since r will always be 0 if freq is 1
        # if freq==1:
        #     return self.numMap[target]
        
        r = random.randint(0, freq-1)
        return self.numMap[target][r]


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)