from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  if root is None:
    return None

  queue = deque()
  queue.append(root)

  while queue:
    for i in range(len(queue)):
      current = queue.popleft()
      
      if current.left is not None:
        queue.append(current.left)
      if current.right is not None:
        queue.append(current.right)
      
      if current.val == key:
        nextt = queue.popleft()
        return nextt

  return None


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  result = find_successor(root, 12)
  if result:
    print(result.val)
  result = find_successor(root, 9)
  if result:
    print(result.val)


main()
