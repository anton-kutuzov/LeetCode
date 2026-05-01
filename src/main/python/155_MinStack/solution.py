class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        element = self.stack[-1][1] if self.stack else None
        if element is None or val < element:
            element = val
        self.stack.append([val, element])

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()

    def top(self) -> int:
        return self.stack[-1][0] if self.stack else None

    def getMin(self) -> int:
        return self.stack[-1][1] if self.stack else None


if __name__ == '__main__':
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    assert minStack.getMin() == -3
    minStack.pop()
    assert minStack.top() == 0
    assert minStack.getMin() == -2
