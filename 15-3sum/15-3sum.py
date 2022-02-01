class Solution:        
        
#         output = []
        
#         if(len(nums) is 0 or len(nums) is 1):
#             return []
        
#         dict = { 
#             nums[0] : 1
#         }
        
#         for i in range(1, len(nums)):
#             [-1,0,1,2,-1,-4]
#             # nums[i]+nums[i-1]+nums[i-2] = 0
#             # 0 - nums[i-2]
#             sum = 0 - (nums[i]+nums[i-1])
            
#             if(sum in dict and dict[sum] == 1):
#                 if(len(nums)>2):
#                     output.append([sum, nums[i-1], nums[i]])
#                     output.sort()
#                     dict[sum] = 0
                
#             dict[sum] = 1
            
#         return output
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i == 0 or nums[i - 1] != nums[i]:
                self.twoSum(nums, i, res)
        return res

    def twoSum(self, nums: List[int], i: int, res: List[List[int]]):
        seen = set()
        j = i + 1
        while j < len(nums):
            complement = -nums[i] - nums[j]
            if complement in seen:
                res.append([nums[i], nums[j], complement])
                while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                    j += 1
            seen.add(nums[j])
            j += 1
