def plusOne(self, digits):
        index = 0
        result = 0
        while index < len(digits):
            result = result * 10 + digits[index]
            index += 1
        
        return [int(i) for i in str(result+1)]  
