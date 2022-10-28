# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        slowPtr = head
        fastPtr = head
        
        while slowPtr is not None and fastPtr is not None and fastPtr.next is not None:
            slowPtr = slowPtr.next
            fastPtr = fastPtr.next.next
            
            if (slowPtr == fastPtr):
                return True
            
        return False