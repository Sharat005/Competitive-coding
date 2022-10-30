class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        output = []
        
        def dfs(start, comb, total):
            if len(comb) == k and total == 0:
                output.append(list(comb))
                return
            elif total < 0 or len(comb) == k:
                return
            
            for i in range(start, 9):
                
                comb.append(i+1)
                dfs(i+1, comb, total-i-1)
                comb.pop()
                
        dfs(0, [], n)
        
        return output
            