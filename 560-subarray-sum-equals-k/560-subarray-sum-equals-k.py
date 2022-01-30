class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        dict = {0:1}
        sum = 0
        count = 0
        
        for i in range(len(nums)):
            sum += nums[i]
            
            if (sum-k) in dict:
                count += dict[sum-k]
            
            dict[sum] = dict[sum] + 1 if sum in dict else 0 + 1
            
            # if(sum in dict):
            #     dict[sum] = dict[sum] + 1
            # else:
            #     dict[sum] = 0 + 1
        return count