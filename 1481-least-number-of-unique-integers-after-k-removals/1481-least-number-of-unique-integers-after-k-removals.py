class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # c = collections.Counter(arr)
        # print(sorted( arr, key=lambda x: (c[x], x))[k:])
        # return len(set(sorted( arr, key=lambda x: (c[x], x))[k:]))
    
        # using heap strategy
        
        dictt = {}
        
        dictt = dict(Counter(arr))
        print(dictt)
        
        minHeap = list(dictt.values())
        heapq.heapify(minHeap)
        
        removal_count = 0
        while removal_count < k:
            removal_count += heapq.heappop(minHeap)
        
        if removal_count == k:
            return len(minHeap)
        
        return len(minHeap)+1
        
        
            
            
            