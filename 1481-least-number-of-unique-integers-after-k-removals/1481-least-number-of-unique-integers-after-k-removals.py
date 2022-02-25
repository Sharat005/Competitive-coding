class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        
#         if len(arr) == 1:
#             if k == 0:
#                 return 1
#             else:
#                 return 0
        
#         myMap = dict(Counter(arr))
#         myMap = dict(sorted(myMap.items(), key=lambda item: item[1]))
#         print(len(myMap))
        
#         remove = k
#         while remove > 0:
#             myMap[i] -= 
            
                
        # for key, val in list(myMap.items()):
        #     if k >= val:
        #         k = k - val
        #         del myMap[key]
        #     else:
        #         return len(set(myMap.keys()))
        #     if len(set(myMap.keys())) is 0:
        #         return 0
            
        freqs = Counter(arr)
        # the amount of distinct numbers
        distinctN = len(freqs)
        
        # Sort them by increasing frequency
        sortedFreqs = [(k,v) for k,v in sorted(freqs.items(), key=lambda item: item[1])]

        # Remove the least common numbers
        toRemove = k
        removed = 0
        while toRemove > 0:
            toRemove -= sortedFreqs[removed][1]
            removed += 1
            
        # We had some numbers left in the last purge
        if toRemove < 0: removed -= 1
        
        return distinctN - removed
            
            