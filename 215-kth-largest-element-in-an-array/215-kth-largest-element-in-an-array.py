class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        heapq._heapify_max(nums)
        for i in range(k):
            if i == k-1:
                return heapq._heappop_max(nums)
            heapq._heappop_max(nums)
                
        #pop_max = heapq._heappop_max(elements)
        
        # sortedNums = sorted(nums, reverse=True)
        # return sortedNums[k-1]
        