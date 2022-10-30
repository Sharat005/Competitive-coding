class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        output = []
        
        def dfs(total, comb, start):
            
            if total == target:
                
                output.append(comb.copy())
                return
            
            elif total > target:
                return
            
            for i in range(start, len(candidates)):
                
                comb.append(candidates[i])
                dfs(total + candidates[i], comb, i)
                
                comb.pop()
                
        dfs(0, [], 0)
        
        return output
                
            
            