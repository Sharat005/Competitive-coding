# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        node = head
        count = 0
        
        while(node is not None and node.next is not None):
            if(node.val == node.next.val):
                if(node.next.next is not None):
                    node.next = node.next.next
                else:
                    node.next = None
            else:    
                node = node.next
            
        return head
        