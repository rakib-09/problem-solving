from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        s_list = list(s)
        start = len(s)
        for i in range(len(s)):
            if s[i] == c:
                start = i
            s_list[i] = abs(start - i)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                start = i
            if abs(start - i) < s_list[i]:
                s_list[i] = abs(start - i)
        return s_list
