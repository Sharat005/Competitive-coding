class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def path_exists(root, sequence, size):
  if root is None:
    return False
  
  if root.val != sequence[0]:
    return False

  if root.left is None and root.right is None and size == 0:
    return True

  return path_exists(root.left, sequence[1:], size - 1) or path_exists(root.right, sequence[1:], size - 1)

def find_path(root, sequence):
  # TODO: Write your code here
  
  return path_exists(root, sequence, len(sequence)-1)


def main():

  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)

  print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
  print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))


main()
