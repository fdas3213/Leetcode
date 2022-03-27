    
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #quickselect O(N)
    
        def dist(point):
            x, y =point[0],point[1]
            return x**2+y**2
        
        def partition(left, right):
            r = random.randint(left,right)
            i, j = left, right
            pivot = points[r]
            #swap pivot with the first element
            points[i], points[r] = points[r], points[i]
            
            while i<j:
                while i<len(points) and dist(points[i])<=dist(pivot):
                    i += 1
                while j>0 and dist(points[j])>dist(pivot):
                    j -= 1
                if i<j:
                    #swap 
                    points[i], points[j] = points[j], points[i]
            
            #swap j with pivot element
            points[j], points[left] = points[left], points[j]
            return j
        
        left, right = 0, len(points)-1
        while left<=right:
            pivot_index = partition(left, right)
            if pivot_index==k-1:
                return points[:k]
            elif pivot_index>k:
                right = pivot_index-1
            else:
                left = pivot_index+1
        
        return points[:k]