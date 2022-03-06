class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        count = Counter(nums)
        return heapq.nlargest(k, count.keys(), key=count.get)
            
        
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