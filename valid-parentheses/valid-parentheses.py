class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) is 1:
            return False
        
        stack = [ ]
        dict = {
            ')': '(',
            ']': '[',
            '}': '{'
        }        
        
        for strr in s:
            stack.append(strr)
            if strr in dict:
                temp = ''
                if(len(stack) < 2):
                    return False
                else:
                    temp = stack.pop()
                if(len(stack) > 0 and dict[temp] != stack.pop()):
                    return False
        if len(stack) is 0:
            return True
                
                