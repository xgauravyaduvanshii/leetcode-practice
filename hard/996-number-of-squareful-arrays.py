import math
from collections import Counter


class Solution:
    def numSquarefulPerms(self, nums: list[int]) -> int:
        # My thinking: build the permutation one number at a time,
        # only placing a number next to the last one when their sum
        # is a perfect square — identical numbers are interchangeable.
        counts = Counter(nums)

        def is_square(x):
            root = math.isqrt(x)
            return root * root == x

        def dfs(last, remaining):
            if remaining == 0:
                return 1
            total = 0
            for num in counts:
                if counts[num] == 0:
                    continue
                if last is not None and not is_square(last + num):
                    continue
                counts[num] -= 1
                total += dfs(num, remaining - 1)
                counts[num] += 1
            return total

        return dfs(None, len(nums))
