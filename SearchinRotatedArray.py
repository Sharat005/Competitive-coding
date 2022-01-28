# https://leetcode.com/problems/search-in-rotated-sorted-array/

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
