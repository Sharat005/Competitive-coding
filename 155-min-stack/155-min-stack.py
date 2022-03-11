class MinStack:

    def __init__(self):
        self.queue = []
        self.min = []

    def push(self, val: int) -> None:
        if not self.min or val <= self.min[-1]:
            self.min.append(val)
        self.queue.append(val)

    def pop(self) -> None:
        if self.min[-1] == self.queue[-1]:
            self.min.pop()
        self.queue.pop()

    def top(self) -> int:
        return self.queue[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()