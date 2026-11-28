# LeetCode 2653. Sliding Subarray Beauty — Medium
# https://leetcode.com/problems/sliding-subarray-beauty/
# Submission 2205111244 — Accepted, Python3
#
# My thinking: values only range from -50 to 50, so a small
# frequency table over the negative values is enough. Slide
# the window, updating two counts per step, and read the
# x-th smallest negative straight off the table (0 when the
# window holds fewer than x negatives).
class Solution:
    def getSubarrayBeauty(self, nums: list[int], k: int, x: int) -> list[int]:
        n = len(nums)
        freq = [0] * 51  # freq[v] counts value -v, v in 1..50
        for v in nums[:k]:
            if v < 0:
                freq[-v] += 1
        ans = []
        for i in range(n - k + 1):
            cnt = 0
            beauty = 0
            for v in range(50, 0, -1):
                cnt += freq[v]
                if cnt >= x:
                    beauty = -v
                    break
            ans.append(beauty)
            if i + k < n:
                if nums[i] < 0:
                    freq[-nums[i]] -= 1
                if nums[i + k] < 0:
                    freq[-nums[i + k]] += 1
        return ans
