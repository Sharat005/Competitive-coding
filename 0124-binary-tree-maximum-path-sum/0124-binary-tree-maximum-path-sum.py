# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def maxPath(root):
            nonlocal maxSum
            
            if root is None:
                return 0
            
            leftmaxSum = max(maxPath(root.left), 0)
            rightmaxSum = max(maxPath(root.right), 0)

            newSum = root.val + leftmaxSum + rightmaxSum

            maxSum = max(maxSum, newSum)
            
            return root.val + max(leftmaxSum, rightmaxSum)
    
        maxSum = -math.inf        
        maxPath(root)
        return maxSum
        