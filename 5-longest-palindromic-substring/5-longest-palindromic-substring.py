class Solution:
    
    def helper(self, s, l, r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l+1:r]
    
    
    def longestPalindrome(self, s: str) -> str:
        
        l, r = 0, 0
        output = ''
        for i in range(len(s)):
            
            temp = self.helper(s, i, i)
            if len(temp) > len(output):
                output = temp
                
            temp = self.helper(s, i, i+1)
            if len(temp) > len(output):
                output = temp
                
        return output
            
               
        