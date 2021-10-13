from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        pivot = 0
        for k, v in enumerate(nums):
            print(k, v)