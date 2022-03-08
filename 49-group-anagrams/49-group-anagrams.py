class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagramMap = {}
        
        for s in strs:
            ss = str(sorted(s))
            if ss not in anagramMap:
                anagramMap[ss] = []
            anagramMap[ss].append(s)
            
        return anagramMap.values()
            
        