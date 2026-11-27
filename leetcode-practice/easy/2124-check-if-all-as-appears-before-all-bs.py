# LeetCode 2124. Check if All A's Appears Before All B's — Easy
# https://leetcode.com/problems/check-if-all-as-appears-before-all-bs/
# Submission 2197614071 — Accepted, Python3
#
# My thinking: all the a's come before all the b's
# exactly when the string never has a 'b' followed
# later by an 'a' — that is, when "ba" does not
# appear anywhere in it.

class Solution:
    def checkString(self, s: str) -> bool:
        return 'ba' not in s
