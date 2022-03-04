class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        word_index = defaultdict(list)
        n = 0
        for index, word in enumerate(wordsDict):
            word_index[word].append(index)
            n += 1
        
        min_dist, p1, p2 = n, 0, 0
        arr1, arr2 = word_index[word1], word_index[word2]
        l1, l2 = len(arr1), len(arr2)
        
        while p1<l1 and p2<l2:
            #if one pointer reaches the end, then moving another pointer will only create a larger distance due to the sorted nature of these two arrays
            min_dist = min(min_dist, abs(arr1[p1]-arr2[p2]))
            if arr1[p1]<arr2[p2]:
                p1 += 1
            else:
                p2 += 1
        
        return min_dist
        