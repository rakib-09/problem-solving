from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        first = 0
        last = len(nums) - 1
        while first <= last:
            print(first, last, nums)
            if nums[first] == val:
                del nums[first]
                last -= 1
            elif nums[last] == val:
                del nums[last]
                first += 1
                last -= 1
            else:
                first += 1
                last -= 1
        return len(nums)
