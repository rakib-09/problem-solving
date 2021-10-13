import re


class Solution:
    def palindrome(self, s: str):
        s = s.lower()
        s = re.sub(r"[^a-zA-Z0-9]+", "", s)
        first = 0
        last = len(s) - 1
        while first <= last:
            if s[first] != s[last]:
                return False
            first += 1
            last -= 1
        return True
