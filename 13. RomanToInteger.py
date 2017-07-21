def romanToInt(self, s):
        roman_dict = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100,'D':500,'M':1000}
        result = roman_dict[s[0]]
        index = 1
        
        while index < len(s):
            if roman_dict[s[index]] > roman_dict[s[index - 1]]:
                result -= 2 * roman_dict[s[index - 1]]
                result += roman_dict[s[index]]
            else:
                result += roman_dict[s[index]]
            index += 1
        return result
