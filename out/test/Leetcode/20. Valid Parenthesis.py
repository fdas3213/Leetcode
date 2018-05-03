#use of stack data structure could be better
def isValid(s):
	stack = []
        dic = {"{":"}", "[":"]", "(":")"}
        for char in s:
            if char in dic:
                stack.append(dic[char])
            elif char in dic.values():
                if len(stack) == 0 or char != stack.pop():
                    return False
            else:
                return False
        return len(stack) == 0     
