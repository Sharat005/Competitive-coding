class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        if(len(s) is 1):
            return 0
        
        dict = {}
        
        for i in range(len(s)):
            if s[i] in dict:
                dict[s[i]] += 1
            else:
                dict[s[i]] = 1
            
        print(dict)
        for j in range(len(s)):
            if dict[s[j]] == 1:
                return j
            
        return -1