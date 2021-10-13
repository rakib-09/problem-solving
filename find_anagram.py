import collections


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        # cnt1, cnt2 = map(collections.Counter, (s, t))
        # return sum((cnt1 - cnt2).values())
        d = dict()
        length = 0
        for k, v in enumerate(s):
            if v in d:
                d[v] += 1
            else:
                d[v] = 1
        print(d)
        for v in t:
            if v in d:
                d[v] -= 1
            else:
                length += 1
        print(sum(d.values()))
        return sum(d.values()) + length
        # f_a = list()
        # f_a[:0] = s
        # length = len(f_a)
        # for v in t:
        #     if v in f_a:
        #         f_a.remove(v)
        #         length -= 1
        # return length
