class CustomStack:

    def __init__(self, maxSize: int):
        self.maxSize = maxSize
        self.size = 0
        self.increment_val = 0
        self.buffer = []

    def push(self, x: int) -> None:
        if len(self.buffer) < self.maxSize:
            self.buffer.append(x)

    def pop(self) -> int:
        if self.buffer:
            return self.buffer.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(0, min(k, len(self.buffer))):
            self.buffer[i] += val


if __name__ == '__main__':
    obj = CustomStack(3)
    obj.push(1)
    obj.push(2)
    obj.push(3)
    obj.push(4)
    obj.increment(5, 100)
    assert obj.pop() == 103
