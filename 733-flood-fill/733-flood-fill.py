class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        
        l, r, u, d = [0,-1], [0, 1], [-1,0], [1,0]
        start = image[sr][sc]
        if start == newColor: return image
        m = len(image) - 1
        n = len(image[0]) - 1
        
        def dfs(image, start, sr, sc):
            
            print(sr, sc, m, n)
            if sr == -1 or sc == -1 or sr > m or sc > n:
                return
            
            if image[sr][sc] != start:
                return
            
            image[sr][sc] = newColor
            
            if image[sr][sc-1] == start:
                dfs(image, start, sr, sc-1)

            if sc+1 <= n and image[sr][sc+1] == start:
                dfs(image, start, sr, sc+1)

            if image[sr-1][sc] == start:
                dfs(image, start, sr-1, sc)

            if sr+1 <= m and image[sr+1][sc] == start:
                dfs(image, start, sr+1, sc)
         
        dfs(image, start, sr, sc)
        return image
    