class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dictt = {}
        output = []
        
        for ele in strs:
            if str(sorted(ele)) not in dictt:
                dictt[str(sorted(ele))] = []
            dictt[str(sorted(ele))].append(ele)
        
        for key, val in dictt.items():
            output.append(val)
            
        return output
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         anagramMap = {}
        
#         for s in strs:
#             ss = str(sorted(s))
#             if ss not in anagramMap:
#                 anagramMap[ss] = []
#             anagramMap[ss].append(s)
            
#         return anagramMap.values()
            
        