# https://leetcode.com/problems/coin-change/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Starting approach used at solving the problem, -1 case is not covered. Basic testcases passed

        # coinsSorted = sorted(coins, reverse=True);
        # count = -1;
        # for i in range(len(coinsSorted)+1):
        #     if(amount==0):
        #         return count + 1;
        #         break;
        #     elif(amount<coinsSorted[i]):
        #         continue;
        #     else:
        #         count = count + (amount/coinsSorted[i]);
        #         amount = amount - (coinsSorted[i] * (amount/coinsSorted[i]))
        
        # Final approach which passed all the test cases
        
        # to understand draw a matrix with rows as coins available and columns as value incrementing 1 each time

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for c in coins:
            for x in range(c, amount + 1):
                dp[x] = min(dp[x], dp[x - c] + 1);
                
        if(dp[amount] != float('inf')):
            return dp[amount];
        else:
            return -1;
        
