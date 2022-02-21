import math
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        
        sortedArr = sorted(arr)
        
        diff = math.inf
        output = []
        
        for i in range(1,len(sortedArr)):
            if(sortedArr[i]-sortedArr[i-1] < diff):
                diff = sortedArr[i]-sortedArr[i-1]
        
        for i in range(1,len(sortedArr)):
            if(sortedArr[i]-sortedArr[i-1] == diff):
                output.append([sortedArr[i-1], sortedArr[i]])
                
        return output
        