# LeetCode 2193. Minimum Number of Moves to Make Palindrome — Hard
# https://leetcode.com/problems/minimum-number-of-moves-to-make-palindrome/
# Submission 2201612627 — Accepted, Python3
#
# My thinking: work from the two ends in —
# matching ends just close in, a letter with
# a partner further in gets walked over to
# its end, and the one letter with no partner
# shuffles one step toward the middle at a
# time.

from collections import Counter


class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        if sum(1 for c in Counter(s).values() if c % 2 == 1) > 1:
            return -1
        s = list(s)
        ans = 0
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                k = right
                while k > left and s[k] != s[left]:
                    k -= 1
                if k == left:
                    # s[left] is the odd one out; nudge it toward the middle.
                    s[left], s[left + 1] = s[left + 1], s[left]
                    ans += 1
                else:
                    while k < right:
                        s[k], s[k + 1] = s[k + 1], s[k]
                        k += 1
                        ans += 1
                    left += 1
                    right -= 1
        return ans
