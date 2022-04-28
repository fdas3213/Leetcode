class Solution:
    def differByOne(self, dict: List[str]) -> bool:
        """
        Time Complexity: O(M^2 * N). We iterate over the entire dict, 
        we then iterate over the length of every word(M), we then create a new string (O(M))
        """
        
        l = len(dict[0])
        for i in range(l):
            wordSet = set()
            for word in dict:
                newWord = word[:i]+'*'+word[i+1:]
                if newWord in wordSet:
                    return True
                wordSet.add(newWord)
        
        return False