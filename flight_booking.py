from typing import List


class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * (n + 1)
        print(res)
        for first, last, seat in bookings:
            print(first, last, seat)
            res[first - 1] += seat
            res[last] -= seat
            # res[last - 1] += seat
            print("here", res)
        for i in range(1, n):
            print("res[i]", res[i], res[i - 1])
            res[i] += res[i - 1]
        return res[:-1]
        # res = dict()
        # for i in range(1, n + 1):
        #     res[i] = 0
        # res_arr = list()
        # for booking_arr in bookings:
        #     for val in range(booking_arr[0], booking_arr[1] + 1):
        #         if val in res:
        #             res[val] = res[val] + booking_arr[2]
        #         else:
        #             res[val] = booking_arr[2]
        # # for k, v in sorted(res.items()):
        # #     res_arr.append(v)
        # return res_arr
