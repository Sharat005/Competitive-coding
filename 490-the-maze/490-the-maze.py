class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        left, right, up, down = [0,-1], [0,1], [-1,0], [1,0]
        
        
#         # start for a matrix/lawn moving
#         start = [a,b] --> [a-1,b-1],[a,b-1],[a-1,b],[a+1,b+1],[a+1,b],[a,b+1]
        
#         #to move left
#         start[0], start[1] = start[0] + left[0], start[1] + left[1]
        
#         modR, modC = start[0] + left[0], start[1] + left[1]
        
        
        
        m, n, seen = len(maze), len(maze[0]), set()
        def dfs(i, j):
            if [i, j] == destination: return True
            for dx, dy in ((0,-1),(0,1),(-1,0),(1,0)):
                x, y = i, j
                while 0 <= x+dx < m and 0 <= y+dy < n and not maze[x+dx][y+dy]:
                    x, y = x+dx, y+dy
                if (x,y) not in seen: 
                    seen.add((x,y))
                    if dfs(x,y): return True
            return False
        return dfs(*start)