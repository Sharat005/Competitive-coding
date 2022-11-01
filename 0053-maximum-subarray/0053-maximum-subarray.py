class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i], nums[i])
            
        return max(dp)
        
#         if(len(nums)==1):
#             return nums[0];
         
#         n = len(nums);
#         dp = [0] * n;
#         dp[0] = nums[0];
        
#         for i in range(1, len(nums)):
#             dp[i] = max(nums[i], dp[i-1]+nums[i]);
            
#         return max(dp);