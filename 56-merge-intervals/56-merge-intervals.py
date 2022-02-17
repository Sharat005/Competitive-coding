class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort(key=lambda x:x[0])
        
        output = []
        
        for i in intervals:
            
            if not output or output[-1][1] < i[0]:
                output.append(i)
            else:
                output[-1][1] = max(output[-1][1], i[1])
                
        return output