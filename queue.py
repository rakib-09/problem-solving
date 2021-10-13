class PrintQueue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        try:
            return self.items.pop()
        except:
            return None

    def peek(self):
        try:
            return self.items[-1]
        except:
            return None

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)
