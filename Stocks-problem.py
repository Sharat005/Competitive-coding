# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

# First solved it using brute force method of looping through two arrays and keeping track of max difference, It takes O(n) time
# Using Dynamic programming concept and just through one traversion we can find max value by keeping track of them

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
            
        
