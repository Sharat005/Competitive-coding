# https://leetcode.com/problems/contains-duplicate

# At first used brute force but the search takes a lot of time om top of a loop
# Later used concept of sets from python which makes sure there are no duplicate elements in it

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        print(set(nums))
        return True if len(set(nums)) < len(nums) else False

#OR
# Using hash map or dictionary

class Solution:
	def containsDuplicate(self, nums: List[int]) -> bool:
		dictt = {}
		        for n in nums:
		            if n in dictt: return True
		            else: dictt[n] = 1
		        return False