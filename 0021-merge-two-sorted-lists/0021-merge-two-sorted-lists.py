# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        sortedListt = ListNode()
        sortedList = sortedListt
        
        while list1 is not None and list2 is not None:
            if list1.val <= list2.val:
                sortedList.next = list1
                list1 = list1.next
            else:
                sortedList.next = list2
                list2 = list2.next
                
            sortedList = sortedList.next
            
        if list1 is not None:
            sortedList.next = list1
        else:
            sortedList.next = list2
        
        return sortedListt.next
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
#         res = ListNode()
#         p = res
        
#         while list1 and list2:
#             if list1.val < list2.val:
#                 p.next = list1
#                 list1 = list1.next
#             else:
#                 p.next = list2
#                 list2 = list2.next
#             p = p.next
#         p.next = list1 if list1 else list2
#         return res.next