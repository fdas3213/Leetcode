class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i, n in enumerate(numbers):
            temp = target-n
            left, right = i+1, len(numbers)-1
            while left<=right:
                mid = left+(right-left)//2
                if numbers[mid]==temp:
                    return [i+1, mid+1]
                elif numbers[mid]<temp:
                    left=mid+1
                else:
                    right = mid-1