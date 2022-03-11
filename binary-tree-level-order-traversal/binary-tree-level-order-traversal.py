# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        output = []
        
        while queue:
            levelOrder = []
            for i in range(len(queue)):
                current = queue.popleft()
                levelOrder.append(current.val)
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            output.append(levelOrder)
            
        return output
        