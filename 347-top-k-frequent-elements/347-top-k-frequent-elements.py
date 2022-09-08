from queue import PriorityQueue
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if not nums:
	        return []

        if len(nums) == 1:
             return nums

        # first find freq - freq dict
        d = {}
        for num in nums:
            if num in d:
                d[num] -= 1 # reverse the sign on the freq for the heap's sake
            else:
                d[num] = -1

        h = []
        from heapq import heappush, heappop
        for key in d:
            heappush(h, (d[key], key))

        res = []
        count = 0
        while count < k:
            frq, item = heappop(h)
            res.append(item)
            count += 1
        return res
        
        
        # count = Counter(nums)
        # return heapq.nlargest(k, count.keys(), key=count.get)
            
        
#         dictt = {}
#         output = []
#         counter = 0
        
#         for i in range(len(nums)):
#             if nums[i] in dictt:
#                 dictt[nums[i]] += 1
#             else:
#                 dictt[nums[i]] = 1
                
#         dictt = dict(sorted(dictt.items(), key=lambda item: item[1], reverse=True))    
        
#         for key,val in dictt.items():
#             if counter < k:
#                 output.append(key)
#             else:
#                 break
#             counter += 1
                
#         return output