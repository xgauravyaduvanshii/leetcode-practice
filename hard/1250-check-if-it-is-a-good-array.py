import math


class Solution:
    def isGoodArray(self, nums: list[int]) -> bool:
        # My thinking: Bezout says 1 is a combination of the
        # numbers exactly when their greatest common divisor
        # is 1 — so just fold the gcd down.
        current = 0
        for num in nums:
            current = math.gcd(current, num)
            if current == 1:
                return True
        return current == 1
