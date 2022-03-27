class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        #use a tuple to represent the difference between each letter
        mapping = defaultdict(list)
        
        for word in strings:
            cur_diff = []
            for i in range(1, len(word)):
                prev_char = word[i-1]
                cur_char = word[i]
                diff = (ord(cur_char)-ord(prev_char)+26)%26
                cur_diff.append(diff)
            mapping[tuple(cur_diff)].append(word)
        
        ans = []
        for diff, words in mapping.items():
            ans.append(words)
        
        return ans