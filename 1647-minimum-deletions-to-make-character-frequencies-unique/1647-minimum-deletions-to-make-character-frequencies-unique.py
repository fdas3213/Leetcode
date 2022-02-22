class Solution:
    def minDeletions(self, s: str) -> int:
        if len(s)<=1:
            return 0
        count = 0
        freq_map = defaultdict(int)
        freq_set = set()
        for ch in s:
            freq_map[ch] += 1
        
        for ch, freq in freq_map.items():
            while freq>0 and freq in freq_set:
                freq -= 1
                count += 1
            freq_set.add(freq)
        
        return count
    
        
                        
        
        