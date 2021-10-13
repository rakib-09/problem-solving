"""
Problem Link: https://leetcode.com/problems/design-a-stack-with-increment-operation/
"""


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.arr = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.inc) < self.max_size:
            self.arr.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if len(self.inc) > 0:
            self.inc[-2] += self.inc[-1]
            return self.arr.pop() + self.inc.pop()
        return -1

    def increment(self, k: int, val: int) -> None:
        if self.inc:
            self.inc[min(k, len(self.inc)) - 1] += val

    def print_arr(self):
        print(self.arr, self.inc)
