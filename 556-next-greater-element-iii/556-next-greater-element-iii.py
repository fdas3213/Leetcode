class Solution:
    def nextGreaterElement(self, n: int) -> int:
        if n<10:
            return -1
        
        arr = list(str(n))
        arr = [int(digit) for digit in arr]
        
        #step 1. start from the right, and stop at the element where a[right]>a[right-1]
        right = len(arr)-1
        stop = False
        while not stop:
            if right==0 or arr[right]>arr[right-1]:
                stop = True
            else:
                right -= 1

        if right==0:
            return -1
        
        #step 2. find the first element that's greater than arr[right-1] on the right side of [right-1], and swap with arr[right-1]
        pivot = arr[right-1]
        end = len(arr)-1
        while end>right-1 and arr[end]<=pivot:
            end -= 1
        #step 3. swap
        arr[right-1] = arr[end]
        arr[end] = pivot
        
        #step 4. reverse numbers after right-1
        l, r = right, len(arr)-1
        while l<r:
            pivot = arr[r]
            arr[r] = arr[l]
            arr[l] = pivot
            l += 1
            r -= 1
        
        #step 5. construct the new number
        res = 0
        for digit in arr:
            res = res*10 + digit
        
        return res if res<pow(2,31) else -1
        
        # if res==n or res>=pow(2,31):
        #     return -1
        # else:
        #     return res
        
        