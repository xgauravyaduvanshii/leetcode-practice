import math


class Solution:
    def numOfWays(self, nums: list[int]) -> int:
        # My thinking: the first number is the root and the
        # smaller and larger numbers split left and right —
        # so interleave the two sides' orders in every way.
        MOD = 10 ** 9 + 7

        def ways(arr):
            if len(arr) <= 2:
                return 1
            root = arr[0]
            left = [x for x in arr if x < root]
            right = [x for x in arr if x > root]
            return (math.comb(len(arr) - 1, len(left)) * ways(left) % MOD) * ways(right) % MOD

        return (ways(nums) - 1) % MOD
