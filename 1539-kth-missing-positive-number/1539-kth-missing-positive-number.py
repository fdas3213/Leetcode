class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr)-1
        while left<=right:
            mid = left+(right-left)//2
            """
            The number of positive integers which are missing before the arr[idx] is equal to arr[idx] - idx - 1.
            check number of missing values before index "mid"
            """
            missing_count  = arr[mid]-(mid+1)
            # if k==missing_count:
            #     return arr[mid]-1
            # search on the right side if number of missing integers are less than
            # k before index "mid"
            if k>missing_count:
                left = mid+1
            else:
                right = mid-1
        """
        number of missing integers before "right" is "arr[right]-(right+1)"
        total number of missing integers after "right" is then k-(arr[right]-right+1)
        the actual value would then be arr[right] + k-(arr[right]-right+1)=k+right+1
        """
        return k+(right+1)