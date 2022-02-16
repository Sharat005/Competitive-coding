class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

# Brute force approach
#         if(nums[0]>nums[1]):
#             return 0
#         elif(nums[len(nums)-1]>nums[len(nums)-2]):
#             return len(nums) - 1
        
#         for i in range(1,len(nums)-1):
#             if(nums[i] > nums[i-1] and nums[i] > nums[i+1]):
#                 return i

# optimized approach
        left = 0
        right = len(nums) - 1
        
        if len(nums) == 0:
            return None
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            if(nums[0]>nums[1]):
                return 0
            else:
                return 1
        
        while(right >= left):
            
            mid = left + (right - left) // 2
            print(mid)
            if(mid == 0 and nums[mid] > nums[mid+1]):
                return 0
            
            if(mid == len(nums)-1 and nums[len(nums)-1] > len(nums)-2):
                return len(nums) - 1
            
            if (nums[mid] > nums[mid+1]) and (nums[mid] > nums[mid - 1]):
                return mid
            
            if(nums[mid+1] > nums[mid]):
                left = mid + 1
            else:
                right = mid - 1