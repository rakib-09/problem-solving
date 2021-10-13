class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        # d = {i: 0 for i in 'balloon'}
        d = {"b": 0, "a": 0, "l": 0, "o": 0, "n": 0}

        for c in text:
            if c in d:
                d[c] += 1

        d['l'] = int(d['l'] / 2)
        d['o'] = int(d['o'] / 2)

        return min(d.values())
