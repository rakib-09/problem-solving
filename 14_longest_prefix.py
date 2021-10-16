from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        d = {}
        for i in range(len(strs[0])):
            try:
                d[strs[0][i]] += 1
            except KeyError:
                d[strs[0][i]] = 1
        i = 1
        while i < len(strs):
            for j in range(len(strs[i])):
                if strs[i][j] in d:
                    pass