# https://leetcode.com/problems/binary-tree-level-order-traversal/
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        if not root:
            return []
        def traversal(root, level):
            if(len(levels) == level):
                levels.append([])
                
            levels[level].append(root.val)
            
            if root.left:
                traversal(root.left, level+1)
            if root.right:
                traversal(root.right, level+1)
                
        traversal(root, 0)
        return levels
            
        
