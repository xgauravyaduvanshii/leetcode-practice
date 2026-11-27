# LeetCode 1805. Number of Different Integers in a String — Easy
# https://leetcode.com/problems/number-of-different-integers-in-a-string/
# Submission 2197599221 — Accepted, Python3
#
# My thinking: I scan the string pulling out runs of
# digits. Leading zeros don't change a number's
# value, so I convert each run to an int and drop
# it in a set — the set size is the count of
# different integers.

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        nums = set()
        cur = ""
        for ch in word:
            if ch.isdigit():
                cur += ch
            elif cur:
                nums.add(int(cur))
                cur = ""
        if cur:
            nums.add(int(cur))
        return len(nums)
