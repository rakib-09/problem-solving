from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        i = 0
        arr = []
        # j = 1
        if len(flowerbed) == 1 and flowerbed[0] == 0 and n == 1:
            return True

        while i < len(flowerbed):
            if flowerbed[i] == 0:
                arr.append(0)
            if flowerbed[i] == 1:
                res = (len(arr) - 1)/2
                n -= res
                arr = []
            i += 1
        if len(arr) >= 2:
            n -= 1
        if n <= 0:
            return True
        return False
