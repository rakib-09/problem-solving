from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        count = 1
        while j < len(nums):
            if nums[i] == nums[j]:
                nums.pop(j)
            elif nums[i] != nums[j]:
                count += 1
                i = j
                j += 1

        return count

        # cur_flag = None
        # for k, v in enumerate(nums):
        #     print("flag", cur_flag, k, v)
        #     if k == 0:
        #         cur_flag = v
        #     elif v == cur_flag:
        #         nums.pop(k)
        #     elif cur_flag != v:
        #         cur_flag = v
        # return len(nums)
