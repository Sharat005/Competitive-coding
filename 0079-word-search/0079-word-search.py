class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        
        dirr = [[0,1],[1,0],[0,-1],[-1,0]]
        rowLen = len(board)
        colLen = len(board[0])
        visited = [[False for i in range(len(board[0]))] for j in range(len(board))]
        
        def dfs(board, row, col, i):
            
            # print(i)
            
            if i == len(word):
                # print("returning")
                return True
            
            if row >= rowLen or row < 0 or col >= colLen or col < 0:
                return False
            
            if visited[row][col] == True:
                return False
            
            if board[row][col] == word[i]:
                
                visited[row][col] = True
                
                retval = False
                for d in dirr:
                    retval = retval or dfs(board, row+d[0], col+d[1], i+1)
                    if retval == True:
                        break
                visited[row][col] = False
                # print("return:", retval)
                return retval
            else:
                return False
            
        def helper():            
            
            for i in range(rowLen):
                for j in range(colLen):
                    
                    if dfs(board, i, j, 0) == True:
                        # print("match")
                        return True
            # print("outside")     
            return False
                    
                
        return helper()