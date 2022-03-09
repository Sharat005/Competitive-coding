class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        if len(intervals) < 2:
            return intervals
        
        sortedIntervals = sorted(intervals, key=lambda x:x[0])
        
        print(sortedIntervals)
        mergedIntervals = []
        
        start, end = sortedIntervals[0][0], sortedIntervals[0][1]
        
        for i in range(1,len(sortedIntervals)):
            
            if sortedIntervals[i][0] <= end:
                end = max(end, sortedIntervals[i][1])
            else:
                mergedIntervals.append([start, end])
                start = sortedIntervals[i][0]
                end = sortedIntervals[i][1]
                
        mergedIntervals.append([start, end])
        return mergedIntervals
