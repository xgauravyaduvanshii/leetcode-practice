# LeetCode 2217. Find Palindrome With Fixed Length — Medium
# https://leetcode.com/problems/find-palindrome-with-fixed-length/
# Submission 2204506036 — Accepted, Python3
#
# My thinking: a palindrome is fixed by its first half, so the k-th
# palindrome of a given length comes from the k-th first half. The first
# halves run from 10^(half-1) up to 9 * that count, and if k is beyond
# the count there is no such palindrome. I mirror the half — fully for
# even lengths, without repeating the middle digit for odd lengths.
class Solution:
    def kthPalindrome(self, queries: list[int], intLength: int) -> list[int]:
        half = (intLength + 1) // 2
        start = 10 ** (half - 1)
        count = 9 * start
        ans = []
        for k in queries:
            if k > count:
                ans.append(-1)
                continue
            s = str(start + k - 1)
            if intLength % 2 == 0:
                ans.append(int(s + s[::-1]))
            else:
                ans.append(int(s + s[-2::-1]))
        return ans
