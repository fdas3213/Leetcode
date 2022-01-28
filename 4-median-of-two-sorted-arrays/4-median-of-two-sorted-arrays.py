class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l2<l1:
            return self.findMedianSortedArrays(nums2, nums1)
        
        if l1==0:
            return nums2[l2//2] if l2%2!=0 else (nums2[(l2-1)//2]+nums2[l2//2])/2
        
        left, right, size = 0, l1, (l1+l2+1)//2
        while left <= right:
            pX = left+(right-left)//2
            pY = size-pX
            
            if pX>0 and nums1[pX-1] > nums2[pY]:
                right = pX-1
            elif pX<l1 and nums2[pY-1] > nums1[pX]:
                left = pX+1
            else:
                #if x left max < y right min and y left max < x right min, we found the answer
                if pX==0:
                    #left side of x is empty
                    max_left = nums2[pY-1]
                    #left side of y is empty
                elif pY==0:
                    max_left = nums1[pX-1]
                else:
                    max_left = max(nums1[pX-1], nums2[pY-1])
                
                if pX==l1:
                    #right side of x is empty
                    min_right = nums2[pY]
                elif pY==l2:
                    #right side of y is empty
                    min_right = nums1[pX]
                else:
                    min_right = min(nums1[pX], nums2[pY])
                
                if (l1+l2)%2==0:
                    return (max_left+min_right)/2
                else:
                    return max_left
            