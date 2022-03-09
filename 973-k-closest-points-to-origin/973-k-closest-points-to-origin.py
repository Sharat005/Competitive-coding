class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        
        def distance(point):
            return sqrt(point[0]**2 + point[1]**2)
        
        
        
        minHeap = []
        
        for i in range(len(points)):
            dist = distance(points[i])
            heapq.heappush(minHeap, (dist, points[i]))
            
        output = []
        for i in range(k):
            output.append(heapq.heappop(minHeap)[1])
            
        print(output)
        return output