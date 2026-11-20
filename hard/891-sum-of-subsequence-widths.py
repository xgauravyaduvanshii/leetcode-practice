class Solution:
    def sumSubseqWidths(self, nums: list[int]) -> int:
        # My thinking: once sorted, each number is the biggest in
        # 2^i subsequences and the smallest in 2^(n-1-i) — the width
        # is the difference of those two counts.
        MOD = 10 ** 9 + 7
        nums.sort()
        n = len(nums)
        powers = [1] * n
        for i in range(1, n):
            powers[i] = powers[i - 1] * 2 % MOD
        total = 0
        for i, num in enumerate(nums):
            total = (total + num * (powers[i] - powers[n - 1 - i])) % MOD
        return total
