# two pointer approach

# https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        output1 = []
        output2 = []
        for i in s:
            if(i!='#'):
                output1.append(i)
            elif(output1):
                output1.pop()
        output1 = ''.join(output1)
        for i in t:
            if(i!='#'):
                output2.append(i)
            elif(output2):
                output2.pop()
        output2 = ''.join(output2)
        
        return output1 == output2
