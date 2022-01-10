class MinStack:
    arr = None
    l_arr = None

    def __init__(self):
        self.arr = list()
        self.l_arr = list()

    def push(self, val: int) -> None:
        self.arr.append(val)

    def pop(self) -> None:
        self.arr.pop()

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        lowest = self.arr[0]
        i = 0
        j = len(self.arr) - 1
        for i in self.arr:
            if i and lowest > i:
                lowest = i
        return lowest

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()