# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float('inf');
        maximum = 0;
        for i in range(len(prices)):
            if(prices[i] < minimum):
                minimum = prices[i];
            elif(prices[i]-minimum > maximum):
                maximum = prices[i]-minimum;
        return maximum;
            
        