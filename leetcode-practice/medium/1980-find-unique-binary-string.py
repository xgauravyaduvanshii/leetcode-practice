# LeetCode 1980. Find Unique Binary String — Medium
# https://leetcode.com/problems/find-unique-binary-string/
# Submission 2197607262 — Accepted, Python3
#
# My thinking: I use Cantor's diagonal trick — the
# i-th character of my answer is the opposite of the
# i-th character of the i-th string. That guarantees
# my string differs from every string in the list.
# (The run output "11" differed from the example's
# "00", but any valid string not in the list is
# accepted.)

class Solution:
    def findDifferentBinaryString(self, nums: list[str]) -> str:
        return "".join('1' if nums[i][i] == '0' else '0' for i in range(len(nums)))
