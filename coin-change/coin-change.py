import math
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        dp = [math.inf] * (amount + 1)
        print(dp)
        dp[0] = 0
        
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i-c]+1)
                
        if dp[amount] is not math.inf:
            return dp[amount]
        return -1