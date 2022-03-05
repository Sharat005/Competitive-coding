# Definition for a binary tree node.
# class c:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        
        def recursiveFunc(left, right):
            nonlocal index
            
            if left > right:
                return None
            
            rootVal = preorder[index]
            root = TreeNode(rootVal)
            index += 1
            
            root.left = recursiveFunc(left, dictt[rootVal] - 1)
            root.right = recursiveFunc(dictt[rootVal] + 1, right)
            
            return root
            
        dictt = {}
        index = 0
        for i, val in enumerate(inorder):
            dictt[val] = i
        return recursiveFunc(0, len(preorder) - 1)
