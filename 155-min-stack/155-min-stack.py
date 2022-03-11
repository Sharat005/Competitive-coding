class MinStack:

    def __init__(self):
        self.queue = deque()

    def push(self, val: int) -> None:
        self.queue.append(val)

    def pop(self) -> None:
        self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return min(self.queue)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()