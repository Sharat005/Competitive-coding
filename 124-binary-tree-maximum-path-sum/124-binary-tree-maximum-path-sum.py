# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def max_len(root):
            nonlocal maxSum
            if root is None:
                return 0

            leftSum = max(max_len(root.left), 0)
            rightSum = max(max_len(root.right), 0)

            newpath = root.val + leftSum + rightSum

            maxSum = max(maxSum, newpath)

            return root.val + max(leftSum, rightSum)

                
        maxSum = -math.inf        
        max_len(root)
        return maxSum