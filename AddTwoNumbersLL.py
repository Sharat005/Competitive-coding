# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        def helper(l1, l2, carry):
            
            if(l1 is None and l2 is None and carry == 0):
                return None
            if(l2 is None):
                l2 = ListNode(0)
            if(l1 is None):
                l1 = ListNode(0)

            l3 = ListNode()
            
            sharat = l1.val + l2.val + carry
            l3.val = sharat % 10  # gives us the last digit in 10's place
            carry = sharat // 10  # gives us the main digit to carry to next
            
            l3.next = helper(l1.next, l2.next, carry)
            return l3
        
        return helper(l1, l2, 0)
        
        
            
# first try with iterative approach        
        
#         l3 = ListNode()
#         carry = 0
#         while(l1.next or l2.next):
            
#             temp = l1.val + l2.val
            
#             if(carry):
#                 temp += 1
#                 carry = 0
#             arr = []
#             print(l3)
#             if(temp > 9):
#                 arr = list(map(int,str(temp)))
#                 l3.val = arr[1]
#                 carry = 1
#             else:
#                 l3.val = temp
#             l3.next = ListNode()
#             l3 = l3.next
#             l1 = l1.next
#             l2 = l2.next
            
#         return l3
