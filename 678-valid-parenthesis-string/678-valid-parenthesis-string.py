class Solution:
    def checkValidString(self, s: str) -> bool:
        left_balance = 0
        for ch in s:
            if ch == '(' or ch == '*':
                left_balance += 1
            else:
                left_balance -= 1
            
            if left_balance < 0:
                #there're more right parenthesis than left parenthesis at this stage
                return False
        
        right_balance = 0
        for ch in s[::-1]:
            if ch == ')' or ch == '*':
                right_balance += 1
            else:
                right_balance -= 1
            
            if right_balance < 0:
                #there're more left parenthesis than right parenthesis at this stage. e.g. "*((()*". There're enough left parenthesis to cover right parenthesis, but not enough right parenthesis to match left parenthesis
                return False
        
        return True