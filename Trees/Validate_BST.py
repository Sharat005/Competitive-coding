# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def isValid(node, low=-math.inf, high=math.inf):
            
            if(node is None):
                return True
            
            if(node.val <= low or node.val >= high):
                return False
            
            return isValid(node.left, low, node.val) and isValid(node.right, node.val, high)
        
        return isValid(root)

# First try passing 40/80 testcases (Does not check in the range)
# if(root.left is None and root.right is not None):
#             return False
#         elif(root.left is not None and root.right is None):
#             return False
        
#         if(root.left is None and root.right is None):
#             return True
        
#         if(root.val > root.left.val):
#             self.isValidBST(root.left)
#         else:
#             return False
#         if(root.val < root.right.val):
#             self.isValidBST(root.right)
#         else: 
#             return False
        
#         return True
