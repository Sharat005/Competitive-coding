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
        closes = [')','}',']']
        
        
        for strr in s:
            stack.append(strr)
            if strr in closes:
                temp = ''
                if(len(stack) < 2):
                    return False
                else:
                    temp = stack.pop()
                if(len(stack) > 0 and dict[temp] != stack.pop()):
                    return False
        print(stack)
        if len(stack) is 0:
            return True
                
                