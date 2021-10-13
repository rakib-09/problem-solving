from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        values = {}
        i = 0
        while i < len(numbers):
            remaining = target - numbers[i]
            if remaining in values:
                return [values[remaining], i+1]
            else:
                values[numbers[i]] = i+1
            i += 1
