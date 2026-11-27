# LeetCode 2311. Longest Binary Subsequence Less Than or Equal to K — Medium
# https://leetcode.com/problems/longest-binary-subsequence-less-than-or-equal-to-k/
# Submission 2204675380 — Accepted, Python3
#
# My thinking: every '0' can always be taken for free, so they are all
# in. For the '1's, read the string from the right (least significant
# bit first) and take a '1' only while the running value stays <= k; the
# first '1' that would break the limit ends the scan, because every '1'
# further left is worth even more. Bits at position 30 or beyond always
# exceed k (k <= 10^9), so they are skipped too.
class Solution:
    def longestSubsequence(self, s: str, k: int) -> int:
        ans = s.count('0')
        val = 0
        for i, ch in enumerate(reversed(s)):
            if ch == '1':
                if i >= 30 or val + (1 << i) > k:
                    break
                val += 1 << i
                ans += 1
        return ans
