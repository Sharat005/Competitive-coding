# https://leetcode.com/problems/merge-two-sorted-lists/
# Comes under two pointers approach

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res = ListNode()
        p = res
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next
        p.next = l1 if l1 else l2
        return res.next
    
#Attempt2

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        first = list1
        second = list2
        output = ListNode()
        final = output
        while(first and second):
            if(first.val < second.val):
                final.next = first
                first = first.next
            else:
                final.next = second
                second = second.next
            final = final.next
        if first is None:
            final.next=second
        else:
            final.next=first
        return output.next
