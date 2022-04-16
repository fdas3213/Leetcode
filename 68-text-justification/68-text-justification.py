class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
    
        
        def findRight(left:int, maxWidth:int, words:List[str]) -> str:
            right = left
            width = len(words[right])
            right += 1
            
            while right<len(words) and width+1+len(words[right])<=maxWidth:
                width += (1+len(words[right]))
                right += 1
            
            #need to decrement right by 1 because right is the first index that goes out of boundary
            return right-1
        
        def padSpace(count:int):
            ans = ""
            for i in range(count, 0, -1):
                ans += " "
            return ans
        
        def padResult(word:str, maxWidth:int):
            return word+padSpace(maxWidth-len(word))
        
        def justify(words: List[str], left:int, right:int, maxWidth:int):
            #pad space if left==right because there's only one word
            if left==right:
                return padResult(words[right], maxWidth)
            
            # if right points to the last word, we just pad empty spaces to the right
            isLastline = right==len(words)-1
            
            # check length of sequence of words
            l = 0
            for i in range(left, right+1):
                l += len(words[i])
            
            # check how many spaces are needed
            numSpaces = maxWidth - l
            #check how many words need to be padded with spaces. Should not pad the last word
            numWordstoPad = right-left
            
            # spaces we need to pad to each word
            spaceStr = " " if isLastline else padSpace(numSpaces//numWordstoPad)
            # if spaces cannot be evenly distributed, then we continuously pad one space to each word
            spaceStrReminder = 0 if isLastline else numSpaces%numWordstoPad
            
            res = ""
            for i in range(left, right+1):
                res += words[i]
                res += spaceStr
                
                if spaceStrReminder > 0:
                    res += " "
                    spaceStrReminder -= 1
            
            # need to trim the last word because we padded extra space to the last word
            res = res.rstrip()
            return padResult(res, maxWidth)
        
        left, right = 0,0 
        ans = []
        while left<len(words):
            right = findRight(left, maxWidth, words)
            line = justify(words, left, right, maxWidth)
            
            ans.append(line)
            left = right+1
        
        return ans