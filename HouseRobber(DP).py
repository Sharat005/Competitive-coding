# https://leetcode.com/explore/interview/card/top-interview-questions-easy/97/dynamic-programming/576/

class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if(n == 0): return 0
        if(n == 1): return nums[0]
        
        for i in range(2, n):
            if i == 2:
                nums[i] = nums[i] + nums[i-2]
            else:
                nums[i] = max((nums[i] + nums[i-2]), (nums[i] + nums[i-3]))

        return max(nums)
