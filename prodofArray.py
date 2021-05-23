# https://leetcode.com/problems/product-of-array-except-self

# Since we could not use division and had to find solution in O(n), used this approach of DP by using memory allocation for
# these two extra arrays

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left = [0]*len(nums);
        right = [0]*len(nums);
        output = [0]*len(nums);
        
        left[0] = 1;
        right[len(nums) - 1] = 1;
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] * nums[i-1];
            
        for i in range(len(nums)-2,-1,-1):
            right[i] = right[i+1] * nums[i+1];
            
        for i in range(len(nums)):
            output[i] = left[i] * right[i];
            
        return output
            
        