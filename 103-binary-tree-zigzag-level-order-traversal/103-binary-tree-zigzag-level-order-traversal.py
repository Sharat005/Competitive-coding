# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return None
        
        queue = deque()
        queue.append(root)
        output = []
        # lets consider forward direction as 1 and backward direction as 0
        direction = True
        
        while queue:
            zigzagOrder = deque()
            for i in range(len(queue)):
                current = queue.popleft()
                
                if direction:
                    zigzagOrder.append(current.val)
                else:
                    zigzagOrder.appendleft(current.val)
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
            direction = not direction                   
            output.append(zigzagOrder)
            
        return output
                
                
        