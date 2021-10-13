from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        i = 0
        final_arr = []
        while i < numRows:
            if i == 0:
                final_arr.append([1])
            elif i == 1:
                final_arr.append([1, 1])
            else:
                arr = []
                j = 0
                while j <= i:
                    if j == 0 or j == i:
                        arr.insert(j, 1)
                    else:
                        prev = i - 1
                        prev_arr = final_arr[prev]
                        val = prev_arr[j] + prev_arr[j-1]
                        arr.insert(j, val)
                    j += 1
                final_arr.append(arr)
            i += 1
        return final_arr
