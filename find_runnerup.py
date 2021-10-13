from typing import List


class Solution:
    def find(self, arr: List):
        i = 0
        top = runner_up = -100
        while i < len(arr):
            if i == 0:
                top = arr[i]
            elif i > 0 and arr[i] > top:
                runner_up = top
                top = arr[i]
            elif i > 0 and top > arr[i] > runner_up:
                runner_up = arr[i]
            i += 1
        print(runner_up)
