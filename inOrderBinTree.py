#https://leetcode.com/problems/binary-tree-inorder-traversal/submissions/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        output = []
        def inOrder(node): 
            if(node is None):
                return;
            inOrder(node.left);
            output.append(node.val);
            inOrder(node.right);
        
        inOrder(root);
        return output;
        
    
