class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        i, j = 0, 0
        maxLen = 0
        maxFreq = 0
        charMap = {}
        
        while j < len(s):
            if s[j] not in charMap:
                charMap[s[j]] = 0
            charMap[s[j]] += 1
            
            maxFreq = max(maxFreq, charMap[s[j]])
            
            if (j-i+1) - maxFreq > k:
                charMap[s[i]] -= 1
                i += 1
            else:
                maxLen = max(maxLen, j-i+1)
                
            j += 1
                
        return maxLen
        