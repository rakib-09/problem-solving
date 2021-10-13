from typing import List


class Solution:
    def list_comp(self, x: int, y: int, z: int, n: int) -> List:
        arr = list()
        for i in range(x+1):
            for j in range(y+1):
                for k in range(z+1):
                    if i + j + k != n:
                        arr.append([i, j, k])

        # while i <= x or j <= y or k <= z:
        #     print(f"i: {i} {x} j: {j} {y} k: {k} {z}")
        #     if i <= x:
        #         i += 1
        #     elif j <= y:
        #         j += 1
        #     elif k <= z:
        #         k += 1
        #     if i + j + k != n:
        #         arr.append([i, j, k])
        return arr
# x, y, z, n = (int(raw_input())+1 for _ in range(4))
# print [[a,b,c] for a in range(x) for b in range(y) for c in range(z) if a+b+c!=n-1]