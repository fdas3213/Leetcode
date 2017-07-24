def lengthOfLongestSubstring(self, s):
        index = 0
        s1,s2 = "", ""
        while index < len(s):
            if s[index] not in s1:
                s1 += s[index]
            else:
                if len(s1) >= len(s2):
                    s2,s1 = s1, ""
                    ind = s2.index(s[index]) + 1

                    while ind < len(s2):
                        s1 += s2[ind]
                        ind += 1
                    
                else:
                    s1 = s1[s1.index(s[index]) + 1:]
                s1 += s[index]

            index += 1

        result = len(s1) if len(s1) > len(s2) else len(s2)
    
        return result
