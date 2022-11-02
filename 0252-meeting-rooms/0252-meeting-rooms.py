class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        sortedIntervals = sorted(intervals)
        
        print(sortedIntervals)
    
        for i in range(1,len(intervals)):
            prev = sortedIntervals[i-1]
            curr = sortedIntervals[i]
            print(prev[1], curr[0])
            if prev[1] > curr[0]:
                return False
            
        return True