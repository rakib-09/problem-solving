from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit, min_a = 0, prices[0]
        for i in prices:
            if i < min_a:
                min_a = i
            if (i - min_a) > profit:
                print(i, min_a, profit)
                profit = (i - min_a)
        return profit
        # min_a, max_a, i, j = prices[0], prices[-1], 0, len(prices) - 1
        # while i <= j:
        #     if prices[i] < min_a:
        #         min_a = prices[i]
        #     else:
        #         i += 1
        #     if prices[j] > max_a:
        #         max_a = prices[j]
        #     else:
        #         j -= 1
        #     print(i, j)
        # print(i, j, min_a, max_a)
        # res = max_a - min_a
        # return res if res > 0 else 0

