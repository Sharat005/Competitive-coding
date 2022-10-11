class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        
        if not heights or not heights[0]:
            return []
        
        numRows = len(heights)
        numCols = len(heights[0])
        
        pacificQueue = deque()
        atlanticQueue = deque()
        
        for i in range(numRows):
            pacificQueue.append((i,0))
            atlanticQueue.append((i, numCols-1))
            
        for j in range(numCols):
            pacificQueue.append((0,j))
            atlanticQueue.append((numRows-1, j))
        
        def bfsTraversal(queue):
            
            reachable = set()
            arr = [(1,0),(0,1),(-1,0),(0,-1)]
            
            while queue:
                (left, right) = queue.popleft()
                reachable.add((left, right))
                
                for (i, j) in arr:
                    row, col = left + i, right + j
                    
                    if row < 0 or row >= numRows or col < 0 or col >= numCols:
                        continue
                        
                    if (row, col) in reachable:
                        continue
                        
                    if heights[row][col] < heights[left][right]:
                        continue
                        
                    queue.append((row,col))
                    
            return reachable
            
        
        pacific = bfsTraversal(pacificQueue)
        atlantic = bfsTraversal(atlanticQueue)
        
        return list(pacific.intersection(atlantic))