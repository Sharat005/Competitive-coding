class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def recursiveSum(current, pathSum):
  if current is None:
    return 0

  pathSum = 10 * pathSum + current.val
  if current.left is None and current.right is None:
    return pathSum

  return recursiveSum(current.left, pathSum) + recursiveSum(current.right, pathSum)

def find_sum_of_path_numbers(root):
  # TODO: Write your code here
  return recursiveSum(root, 0)
  



def main():
  root = TreeNode(1)
  root.left = TreeNode(0)
  root.right = TreeNode(1)
  root.left.left = TreeNode(1)
  root.right.left = TreeNode(6)
  root.right.right = TreeNode(5)
  print("Total Sum of Path Numbers: " + str(find_sum_of_path_numbers(root)))


main()
