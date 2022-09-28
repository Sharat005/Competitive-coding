# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def isSubtreeHelper(self, left: Optional[TreeNode], right: Optional[TreeNode]):
        
        if left is None and right is None:
            return True
        elif left is None or right is None:
            return False
        
        if left.val != right.val:
            return False
        
        return self.isSubtreeHelper(left.left, right.left) and self.isSubtreeHelper(left.right, right.right)
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root:
            return self.isSubtreeHelper(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)