class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        left = 0
        right = len(nums) - 1
        mid = 0
        
        if(len(nums) == 1):
            if(nums[0] == target):
                return 0
            else:
                return -1
                        
        
        while left <= right:
            
            mid = left + (right - left) // 2
            
            if(nums[mid] == target):
                return mid
            
            if(nums[right] > nums[left]):
                if(nums[mid] > target):
                    right = mid - 1
                else:
                    left = mid + 1
                continue;
                
            if(nums[mid] >= nums[left]):
                if(target >= nums[left] and target < nums[mid]):
                    right = mid - 1
                else:
                    left = mid + 1
                    
            else:
                if(target <= nums[right] and target > nums[mid]):
                    left = mid + 1
                else:
                    right = mid - 1
            
        return -1
        
#         i, j = 0, len(nums) - 1
        
#         if(len(nums) == 1):
#             if(nums[0] == target):
#                 return 0
#             else:
#                 return -1
                
#         while i <= j:
            
#             mid = i + (j-i) // 2
            
#             if nums[mid] == target:
#                 return mid
            
#             if nums[mid] > nums[i]:
#                 if target >= nums[i] and target < nums[mid]:
#                     j = mid - 1
#                 else:
#                     i = mid + 1
                
#             else:
#                 if target > nums[mid] and target <= nums[j]:
#                     i = mid + 1
#                 else:
#                     j = mid - 1
                    
#         return -1