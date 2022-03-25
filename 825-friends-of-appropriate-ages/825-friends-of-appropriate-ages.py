class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:

        def search_lower_bound(left:int, right:int, target:int):
            while left < right:
                mid = left + (right-left)//2
                if ages[mid]<target:
                    left = mid + 1
                else:
                    # right could be in the answer range since range could equal target
                    right = mid
            
            return left
        
        def search_upper_bound(left:int, right:int, target:int):
            while left<right:
                mid = left+(right-left)//2
                if ages[mid]>target:
                    right = mid
                else:
                    # left could be in the answer range since left could equal target
                    left = mid+1
            
            return left-1
        
        ages = sorted(ages)
        l, count = len(ages), 0
        
        for i, age in enumerate(ages):
            if age<15:
                continue
            lowTarget = int(0.5*age+8)
            
            lowIndex = search_lower_bound(0, i, lowTarget)
            highIndex = search_upper_bound(i, l, age)
            count += max(highIndex-lowIndex, 0)
        
        return count