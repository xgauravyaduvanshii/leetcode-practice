# LeetCode 2155. All Divisions With the Highest Score of a Binary Array — Medium
# https://leetcode.com/problems/all-divisions-with-the-highest-score-of-a-binary-array/
# Submission 2204477346 — Accepted, Python3
#
# My thinking: the score of a split is the zeros on the left plus the
# ones on the right. I sweep the split from left to right, updating the
# running counts of zeros and ones seen so far, and record every split
# whose score ties or beats the best found.
class Solution:
    def maxScoreIndices(self, nums: list[int]) -> list[int]:
        total_ones = sum(nums)
        left_zeros = 0
        left_ones = 0
        best = -1
        ans = []
        n = len(nums)
        for i in range(n + 1):
            score = left_zeros + (total_ones - left_ones)
            if score > best:
                best = score
                ans = [i]
            elif score == best:
                ans.append(i)
            if i < n:
                if nums[i] == 0:
                    left_zeros += 1
                else:
                    left_ones += 1
        return ans
