from typing import List


class BinarySearch:
    def __init__(self, arr: List, search_key: str):
        self.arr = arr
        self.key = search_key

    def search(self):
        low = 0
        high = len(self.arr) - 1
        step = 0
        while low <= high:
            step += 1
            number = int((low + high) / 2)
            if self.arr[number] == self.key:
                print(str(number))
                return
            elif self.arr[number] > self.key:
                high = number - 1
            elif self.arr[number] < self.key:
                low = number + 1
