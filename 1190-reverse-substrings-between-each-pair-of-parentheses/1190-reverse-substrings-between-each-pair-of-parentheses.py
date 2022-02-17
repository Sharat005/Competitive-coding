class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        
        for i in s:
            if i == ')':
                strr = ''
                while stack and stack[-1] != '(':
                    strr += stack.pop()[::-1]
                
                stack.pop()
                stack.append(strr)
                
            else:
                stack.append(i)
                
        return "".join(stack)