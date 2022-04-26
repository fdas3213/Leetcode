class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        wordSet = set()
        for startWord in startWords:
            #step 1. sort every startWord by the lexicographical order
            sortedWord = "".join(sorted(startWord))
            wordSet.add(sortedWord)

        """
        step 2. iterate over targetWords, sort each targetWord, and remove one 
        character at a time. If the new string exists in startWord, then add 1
        """
        
        count = 0
        
        for target in targetWords:
            targetSorted = "".join(sorted(target))
            l = len(targetSorted)
            
            for i in range(l):
                newWord = targetSorted[:i] + targetSorted[i+1:]
                if newWord in wordSet:
                    count += 1
                    break
        
        return count
        
        