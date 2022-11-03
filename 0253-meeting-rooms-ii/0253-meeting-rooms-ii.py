class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
    
        
        if not intervals:
            return 0
        
        intervals = sorted(intervals, key=lambda x:x[0])
        #print(sortedIntervals)
        
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        
        for room in intervals[1:]:
            print(rooms)
            if rooms[0] <= room[0]:
                heapq.heappop(rooms)
                
            
            heapq.heappush(rooms, room[1])
            
        return len(rooms)