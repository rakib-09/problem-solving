class Solution:
    def percent(self, marks: dict, q: str):
        arr = marks[q]
        res = sum(arr) / len(arr)
        return format(res, '.2f')
