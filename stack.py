class Stack:
    def __init__(self):
        self.items = []

    def push(self, item: int) -> None:
        self.items.append(item)

    def pop(self):
        try:
            return self.items.pop()
        except:
            return None

    def peek(self):
        try:
            return self.items[-1]
        except:
            return None

    def size(self):
        return len(self.items)

    def is_empty(self):
        return self.items == []
