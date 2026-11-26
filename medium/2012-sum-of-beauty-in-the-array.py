# LeetCode 2012. Sum of Beauty in the Array — Medium
# https://leetcode.com/problems/sum-of-beauty-in-the-array/
# Submission 2204127418 — Accepted, Python3
#
# My thinking: For each middle index i, beauty 2 needs nums[i] to be
# bigger than EVERYTHING before it and smaller than EVERYTHING after
# it, not just its two neighbours. So I precompute, for each i, the
# largest value to its left and the smallest value to its right.
# If max-left < nums[i] < min-right, it scores 2. Otherwise it can
# still score 1 if it is strictly bigger than its left neighbour and
# strictly smaller than its right neighbour. Anything else scores 0.
# One pass each way builds the two helper arrays, then one more pass
# adds up the scores, so the whole thing runs in linear time.

class Solution:
    def sumOfBeauties(self, nums: list[int]) -> int:
        n = len(nums)

        # max_left[i] = largest value among nums[0..i-1]
        max_left = [0] * n
        best = nums[0]
        for i in range(1, n):
            max_left[i] = best
            best = max(best, nums[i])

        # min_right[i] = smallest value among nums[i+1..n-1]
        min_right = [0] * n
        best = nums[-1]
        for i in range(n - 2, -1, -1):
            min_right[i] = best
            best = min(best, nums[i])

        total = 0
        for i in range(1, n - 1):
            if max_left[i] < nums[i] < min_right[i]:
                total += 2
            elif nums[i - 1] < nums[i] < nums[i + 1]:
                total += 1
        return total


if __name__ == "__main__":
    sol = Solution()
    # Sample 1: [1, 2, 3] -> 2
    assert sol.sumOfBeauties([1, 2, 3]) == 2
    # Sample 2: [2, 4, 6, 4] -> 1
    assert sol.sumOfBeauties([2, 4, 6, 4]) == 1
    # Sample 3: [3, 2, 1] -> 0
    assert sol.sumOfBeauties([3, 2, 1]) == 0
    # Extra checks: mixed case, duplicates never score 2 or 1
    assert sol.sumOfBeauties([1, 2, 3, 4, 5]) == 6  # 2 + 2 + 2
    assert sol.sumOfBeauties([5, 5, 5, 5]) == 0
    print("All sample tests passed.")
