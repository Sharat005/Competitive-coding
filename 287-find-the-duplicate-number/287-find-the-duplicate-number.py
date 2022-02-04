class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        dict = {}
        
        for i in range(len(nums)):
            if nums[i] in dict:
                return nums[i]
            dict[nums[i]] = 1
            
        return None