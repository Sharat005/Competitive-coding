class Node:
  def __init__(self, value, next=None):
    self.value = value
    self.next = next


def has_cycle(head):
  # TODO: Write your code here
  slowPtr, fastPtr = head, head
  while fastPtr is not None and fastPtr.next is not None:
    fastPtr = fastPtr.next.next
    slowPtr = slowPtr.next
    if slowPtr == fastPtr:
      return True
  return False
