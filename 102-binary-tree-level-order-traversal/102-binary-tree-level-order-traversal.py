# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        queue = deque()
        if root is None:
            return None
        
        queue.append(root)
        output = []
        while queue:
            newArr = []
            for i in range(len(queue)):
                
                current = queue.popleft()
                
                newArr.append(current.val)
                
                if current.left is not None:
                    queue.append(current.left)
                if current.right is not None:
                    queue.append(current.right)
                    
                
            output.append(newArr)
            
        return output