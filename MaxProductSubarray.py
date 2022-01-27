# https://leetcode.com/problems/maximum-product-subarray/
# initial solution similar to maximum sum subarray which passes basic testcases but does not pass testcase with negative values in the array

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        dp = [1] * len(nums)
        
        for n in range(len(nums)):
            
            dp[n] = max(nums[n]*dp[n-1], nums[n])
            
        return max(dp)
      
      
# Final solution with handling negative numbers by keeping track of minimum as well and taking max of it at every turn if its multipled neg is multiplied with neg      
      
class Solution:
  def maxProduct(self, nums: List[int]) -> int:

      mini = nums[0]
      maxi = nums[0]
      output = nums[0]

      for i in range(1, len(nums)):

          temp_max = max(nums[i], maxi * nums[i], mini * nums[i])
          mini = min(nums[i], mini * nums[i], maxi * nums[i])

          maxi = temp_max
          output = max(maxi, output)

      return output
      
  
