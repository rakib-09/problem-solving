from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        final_arr = {}
        i = 0
        while i < len(groupSizes):
            j = groupSizes[i]
            arr = []
            try:
                arr = final_arr[j]
            except KeyError:
                arr = []
            finally:
                arr.append(i)
                final_arr[j] = arr
                i += 1
        # return [x[1] for x in sorted(final_arr.items(), key=lambda x: int(x[0]))]
        # f_a = []
        # for i in final_arr:
        #     for j in range(0, len(final_arr[i]), i):
        #         f_a.append(final_arr[j:j+i])
        # return f_a
        return [final_arr[i][j:j + i] for i in final_arr for j in range(0, len(final_arr[i]), i)]