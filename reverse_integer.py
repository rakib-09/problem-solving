import math


class Solution:
    def reverse(self, x: int) -> int:
        neg = False
        res = 0
        if x < 0:
            neg = True
            x = x * -1
        if x == 0:
            return 0
        while x > 0:
            z = int(x % 10)
            x //= 10
            res = (res * 10) + z
        if (res > 2 ** 31 - 1) or (-res < -2 ** 31):
            return 0
        return -res if neg else res
