# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, root, subRoot):
            if root is None and subRoot is None:
                return True
            elif root is None or subRoot is None:
                return False
            
            if root.val != subRoot.val:
                return False
                  
            return self.dfs(root.left, subRoot.left) and self.dfs(root.right, subRoot.right)
        
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
            if root:
                return self.dfs(root, subRoot) or self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)