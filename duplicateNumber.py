# https://leetcode.com/problems/contains-duplicate

# At first used brute force but the search takes a lot of time om top of a loop
# Later used concept of sets from python which makes sure there are no duplicate elements in it

# First basic way using loops
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)-1):
            if(sortedNums[i]==sortedNums[i+1]):
              return True
            elif(i==len(sortedNums)):
              return False

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
