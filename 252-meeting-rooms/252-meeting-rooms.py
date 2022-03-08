class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        
        sortedIntervals = sorted(intervals)
        print(sortedIntervals)
        
        for i in range(len(sortedIntervals)-1):
            if sortedIntervals[i][1] > sortedIntervals[i+1][0]:
                return False
            
        return True