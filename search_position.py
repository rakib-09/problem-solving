from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target == 0:
            return 0
        low = 0
        high = len(nums) - 1
        while low <= high:
            number = int((low + high) / 2)
            print(low, high, number)
            if nums[number] == target:
                return number
            elif nums[number] > target:
                high = number - 1
            elif nums[number] < target:
                low = number + 1
        return high + 1
