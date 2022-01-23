# https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
                
        dict = {}
        left = 0
        output = 0
        
        for right in range(len(s)):
            if s[right] in dict:
                left = max(dict[s[right]], left)
            
            output = max(output, right - left + 1)
            dict[s[right]] = right + 1
            
        return output
