class Solution:
    def maxNumberOfFamilies(self, n: int, reservedSeats: List[List[int]]) -> int:
        seats = defaultdict(list)
        for row, col in reservedSeats:
            seats[row].append(col)
            
        #number of rows not occupied at all
        count = (n-len(seats))*2
        
        # 3 groups: [2,3,4,5], [4,5,6,7], [6,7,8,9]
        for r in seats:
            cur_count = 0
            flag = False
            cols = seats[r]
            
            if 2 not in cols and 3 not in cols and 4 not in cols and 5 not in cols:
                cur_count += 1
                flag = True
            
            if 6 not in cols and 7 not in cols and 8 not in cols and 9 not in cols:
                cur_count += 1
                flag = True
            
            if not flag:
                if 4 not in cols and 5 not in cols and 6 not in cols and 7 not in cols:
                    cur_count += 1
            count += cur_count
        
        return count
            