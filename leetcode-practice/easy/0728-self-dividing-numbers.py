# LeetCode 728. Self Dividing Numbers — Easy
# https://leetcode.com/problems/self-dividing-numbers/
# Submission 2197522651 — Accepted, Python3
#
# My thinking: a number is self-dividing if every
# one of its digits divides it. I pull the digits
# off one by one from the right — a zero digit
# fails straight away, and so does any digit that
# does not divide the number evenly.

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        result = []
        for num in range(left, right + 1):
            n = num
            ok = True
            while n > 0:
                digit = n % 10
                if digit == 0 or num % digit != 0:
                    ok = False
                    break
                n //= 10
            if ok:
                result.append(num)
        return result
