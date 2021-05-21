# https://leetcode.com/problems/two-sum/

# First solved it using brute force method then used hash map to make use of its constant time lookup

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #sortedNums = sorted(nums)
        
        map = {}
        for i, v in enumerate(nums):
            diff = target - v
            if diff in map:
                return [map[diff], i]
            map[v] = i
        return []
                
            
        
