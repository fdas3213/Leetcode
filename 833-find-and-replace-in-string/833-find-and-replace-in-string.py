class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        ans = ""
        
        #need to sort the indices
        
        prev_index = 0
        for index, source, target in sorted(zip(indices, sources, targets)):
            dist = index-prev_index
            # add substrings that will not be replaced to the ans string
            if dist>0:
                ans += s[prev_index:index]
            
            if s[index:].startswith(source):
                ans += target
                prev_index = index+len(source)
            else:
                # reset prev_index to index, so at the next iteration, s[prev_index:index] will be added to the ans string
                prev_index = index
        
        #add final substring
        ans += s[prev_index:]
        
        return ans