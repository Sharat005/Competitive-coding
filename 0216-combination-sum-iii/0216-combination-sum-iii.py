class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        
        
        results = []
        def backtrack(remain, comb, next_start):
            if remain == 0 and len(comb) == k:
                # make a copy of current combination
                # Otherwise the combination would be reverted in other branch of backtracking.
                results.append(list(comb))
                return
            elif remain < 0 or len(comb) == k:
                # exceed the scope, no need to explore further.
                return

            # Iterate through the reduced list of candidates.
            for i in range(next_start, 9):
                comb.append(i+1)
                backtrack(remain-i-1, comb, i+1)
                # backtrack the current choice
                comb.pop()

        backtrack(n, [], 0)

        return results
#         output = []
        
#         def dfs(i, comb, total):
#             if len(comb) == k and total == 0:
#                 output.append(list(comb))
#                 return
#             elif total < 0 or len(comb) == k:
#                 return
            
#             for i in range(i, n):
                
#                 comb.append(i+1)
#                 dfs(i+1, comb, total-i-1)
#                 comb.pop()
                
#         dfs(0, [], n)
        
#         return output
            