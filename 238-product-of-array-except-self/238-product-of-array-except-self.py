class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        leftDP = [0] * len(nums)
        leftDP[0] = 1
        
        rightDP = [0] * len(nums)
        rightDP[len(nums)-1] = 1
        
        output = [0] * len(nums)
        
        for i in range(1,len(nums)):
            leftDP[i] = leftDP[i-1] * nums[i-1]
            
        for j in range(len(nums)-2, -1, -1):
            rightDP[j] = rightDP[j+1] * nums[j+1]
            
        for i in range(len(nums)):
            output[i] = leftDP[i] * rightDP[i]
            
        return output