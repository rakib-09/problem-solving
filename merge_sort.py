from typing import List


class Solution:
    fin_arr = list()
    def merge_sort(self, arr: List):
        if len(arr) > 1:
            mid = len(arr) // 2
            le = arr[:mid]
            ri = arr[mid:]
            self.merge_sort(le)
            self.merge_sort(ri)
            if len(le) == 1 and len(ri) == 1:
                if le > ri:
                    self.fin_arr.insert(0, le[0])
                    self.fin_arr.insert(0, ri[0])
                else:
                    self.fin_arr.insert(0, ri[0])
                    self.fin_arr.insert(0, le[0])
            return self.fin_arr
