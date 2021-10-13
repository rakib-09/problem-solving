class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_num = 0
        prev_num = x
        while x > 0:
            z = int(x % 10)
            new_num = (new_num * 10) + z
            x //= 10
        return new_num == prev_num
