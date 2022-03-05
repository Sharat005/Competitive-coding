class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        sortedNums = sorted(nums, reverse=True)
        
        return sortedNums[k-1]
        