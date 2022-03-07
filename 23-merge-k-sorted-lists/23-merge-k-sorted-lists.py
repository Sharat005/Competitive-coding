# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
        
#     def __lt__(self, other):    -  This func lets you add custom less than operation which is done durong minHeap process
#         return self.value < other.value


from queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        ListNode.__lt__=lambda self,y:self.val<=y.val
        minHeap = PriorityQueue()
        for root in lists:
            if root is not None:
                minHeap.put((root.val, root))
                            
        head = tail = ListNode(0)
        
        while not minHeap.empty():
            val, node = minHeap.get()
                
            tail.next = ListNode(val)
            tail = tail.next
            node = node.next
            
            if node is not None:
                minHeap.put((node.val, node))
                
        return head.next
            
            
        
        # self.nodes = []
        # head = point = ListNode(0)
        # for l in lists:
        #     while l:
        #         self.nodes.append(l.val)
        #         l = l.next
        # for x in sorted(self.nodes):
        #     point.next = ListNode(x)
        #     point = point.next
        # return head.next