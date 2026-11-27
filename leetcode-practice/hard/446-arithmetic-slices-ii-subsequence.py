from collections import defaultdict


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        # My thinking: for each pair, the difference extends every
        # shorter sequence ending at the first index — those
        # extensions of length 3 or more are what we count.
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total = 0
        for j in range(n):
            for i in range(j):
                diff = nums[j] - nums[i]
                count = dp[i][diff]
                total += count
                dp[j][diff] += count + 1
        return total
