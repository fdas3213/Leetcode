class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        res = []
        
        def backtrack(expression:List[str], start:int, value:int, prev_operand:int, current_operand:int):
            if start==len(num):
                if value==target and current_operand==0:
                    res.append("".join(expression[1:]))
                return
            
            #case 1. just extend the digits, no "+-*"
            current_operand = current_operand*10+int(num[start])
            str_op = str(current_operand)
            if current_operand>0:
                #avoid cases like 1+05, or 1*05 since 05 is not valid
                backtrack(expression, start+1, value, prev_operand, current_operand)
        
            #case 2. add
            expression.append('+')
            expression.append(str_op)
            backtrack(expression, start+1, value+current_operand, current_operand, 0)
            expression.pop()
            expression.pop()
            
            
            if expression:
                #case 3. minus
                expression.append('-')
                expression.append(str_op)
                backtrack(expression, start+1, value-current_operand, -current_operand, 0)
                expression.pop()
                expression.pop()
            
                #case 4. multiply
                expression.append("*")
                expression.append(str_op)
                backtrack(expression, start+1, value-prev_operand+(prev_operand*current_operand), 
                          current_operand*prev_operand, 0)
                expression.pop()
                expression.pop()
        
        backtrack([], 0, 0, 0, 0)            
        
        return res
            
            