#https://leetcode.com/problems/symmetric-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        
        def isSymm(root1, root2):
            
            if(root1 is None and root2 is None):
                return True
            elif(root1 is None and root2 is not None):
                return False
            elif(root1 is not None and root2 is None):
                return False
            else:
                if(root1.val != root2.val):
                    return False
                else:
                    return isSymm(root1.left, root2.right) and isSymm(root1.right, root2.left)
            
        return root == None or isSymm(root.left, root.right)
        
