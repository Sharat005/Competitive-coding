class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        dict = {}
        
        i = 0
        maxC = 0
        
        if(len(s) == 0):
            return 0
        
        for j in range(len(s)):
            
            if s[j] in dict:
                i = max(dict[s[j]], i)
            
            maxC = max(maxC, j-i+1)
            dict[s[j]] = j + 1
            
        return maxC
