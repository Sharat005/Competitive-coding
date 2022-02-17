class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        dict = {}
        
        for i in s:
            if i not in dict:
                dict[i] = 0
            dict[i] += 1
            
        for j in t:
            if j in dict:
                dict[j] -= 1
                if(dict[j] == 0):
                    del dict[j]
            else:
                return False
        if(dict):
            return False
        return True