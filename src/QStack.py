from collections import deque

class QStack:
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        return self.q.popleft() if self.q else -1

    def peek(self) -> int:
        return self.q[0] if self.q else -1

    def empty(self) -> bool:
        return not self.q
