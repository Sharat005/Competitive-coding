class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        
        new_start, new_end = newInterval
        idx, n = 0, len(intervals)
        output = []
        
        # add all intervals starting before newInterval
        while idx < n and new_start > intervals[idx][0]:
            output.append(intervals[idx])
            idx += 1
            
        # add newInterval
        # if there is no overlap, just add the interval
        if not output or output[-1][1] < new_start:
            output.append(newInterval)
        # if there is an overlap, merge with the last interval
        else:
            output[-1][1] = max(output[-1][1], new_end)
        
        # add next intervals, merge with newInterval if needed
        while idx < n:
            interval = intervals[idx]
            start, end = interval
            idx += 1
            # if there is no overlap, just add an interval
            if output[-1][1] < start:
                output.append(interval)
            # if there is an overlap, merge with the last interval
            else:
                output[-1][1] = max(output[-1][1], end)
        return output
        
        
        
        
        
        
        
        
#         output = []
#         i = 0
#         while i < len(intervals) and intervals[i][0] < newInterval[0]:
#             output.append(intervals[i])
#             i += 1
            
        
#         start, end = intervals[i-1][0], intervals[i-1][1]
        
#         if newInterval[0] <= end:
#             output[i-1][1] = max(end, newInterval[1])
#             end = output[i-1][1]
#         else:
#             output.append(newInterval)
#             start, end = newInterval
#             i += 1
            
#         print(i)
        
#         while i < len(intervals):
            
#             if intervals[i][0] <= end:
#                 end = max(end, intervals[i][1])
#             else:
#                 output.append([start, end])
#                 start = intervals[i][0]
#                 end = intervals[i][1]
                
#             i += 1
            
#             output.append([start, end])
#         return output