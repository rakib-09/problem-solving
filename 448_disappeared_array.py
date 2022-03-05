from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        nums.sort()
        val = nums[0]
        i = 0
        while i < len(nums):
            print(nums[i], val)
            if nums[i] == val:
                val += 1
            elif nums[i - 1] != nums[i] and nums[i] != val:
                res.append(val)
                val += 1
            i += 1
        return res

