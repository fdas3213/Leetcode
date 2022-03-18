class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1, l2 = len(nums1), len(nums2)
        if l2<l1:
            """
            put the longer array as the second input to avoid index out of range.
            Example: [1,3], [2]. i=1, j=1, index is out of range of [2]. But if
            [2], [1,3], then i=0, j=1, index is within the range of [1,3]
            """
            return self.findMedianSortedArrays(nums2, nums1)
        
        #edge case
        if l1==0:
            return nums2[l2//2] if l2%2!=0 else (nums2[(l2//2)-1]+nums2[l2//2])/2
        
        # partition
        left, right, size = 0, l1, (l1+l2+1)//2
        while left<=right:
            i = left+(right-left)//2
            j = size-i
            
            #maxLeft would have index of i-1/j-1
            if i>0 and nums1[i-1]>nums2[j]:
                # maxLeft1 > minRight2, need to move mid pointer to further left
                right = i-1
            elif i<l1 and nums2[j-1]>nums1[i]:
                # maxLeft2 > minRight1, need to move mid pointer to further right
                left = i+1
            else:
                if i==0:
                    #left side of nums1 is empty
                    maxLeft = nums2[j-1]
                elif j==0:
                    #left side of nums2 is empty
                    maxLeft = nums1[i-1]
                else:
                    #neither side is empty, so choose the max from two numbers
                    maxLeft = max(nums1[i-1], nums2[j-1])
                
                if i==l1:
                    #right side of nums1 is empty
                    minRight = nums2[j]
                elif j==l2:
                    #right side of nums2 is empty
                    minRight = nums1[i]
                else:
                    minRight = min(nums1[i], nums2[j])
            
                if (l1+l2)%2==0:
                    return (maxLeft+minRight)/2
                else:
                    return maxLeft
                
                    
        
        