from typing import List


class Solution:
    def slowestKey(self, releaseTimes: List[int], keysPressed: str) -> str:
        res = keysPressed[0]
        max_d = 0
        for i in range(0, len(releaseTimes)):
            duration = releaseTimes[i] - releaseTimes[i - 1]
            if duration > max_d:
                max_d = duration
                res = keysPressed[i]
            if duration == max_d and ord(keysPressed[i]) > ord(res):
                res = keysPressed[i]
        return res

