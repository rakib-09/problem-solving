from typing import List


class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        i = 0
        j = len(nums) - 1
        while i <= j:
            print(i, j)
            x = 'even' if i % 2 == 0 else 'odd'
            num_x = 'even' if nums[i] % 2 == 0 else 'odd'
            y = 'even' if j % 2 == 0 else 'odd'
            num_y = 'even' if i % 2 == 0 else 'odd'
            if x == num_y and y == num_x:
                temp = nums[i]
                nums[i] = nums[j]
                nums[j] = temp
                i += 1
                j -= 1
            if x == num_x:
                i += 1
            if y == num_y:
                j -= 1
        return nums
