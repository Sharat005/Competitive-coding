from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):
  result = deque()
  # TODO: Write your code here
  if root is None:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    currentLevel = []
    for i in range(len(queue)):
      currentVal = queue.popleft()
      currentLevel.append(currentVal.val)

      if currentVal.left is not None:
        queue.append(currentVal.left)
      if currentVal.right is not None:
        queue.append(currentVal.right)

    result.appendleft(currentLevel)
    
  return result

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Reverse level order traversal: " + str(traverse(root)))


main()
